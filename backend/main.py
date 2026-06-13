from fastapi import FastAPI, UploadFile, File
from detection.detector import detect_survivors
from api.mission_planner import create_mission
from api.route_optimizer import find_best_route
from api.resource_allocator import allocate_resources
import shutil

app = FastAPI()


@app.get("/")
def home():
    return {
        "project": "Phoenix",
        "status": "Running"
    }


@app.post("/detect")
async def detect(file: UploadFile = File(...)):

    filepath = f"temp_{file.filename}"

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = detect_survivors(filepath)

    mission = create_mission(
      result["survivors_found"])
    route = find_best_route()
    resources = allocate_resources(
        result["survivors_found"],
        mission["priority"])

    return {
        **result,
        **mission,
        **route,
        **resources
        }
