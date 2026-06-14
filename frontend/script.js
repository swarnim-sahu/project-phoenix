// Image Preview

document
.getElementById("imageInput")
.addEventListener("change", function () {

    const file = this.files[0];

    if (file) {

        document
        .getElementById("preview")
        .src = URL.createObjectURL(file);

    }

});


// Analyze Button

document
.getElementById("analyzeBtn")
.addEventListener("click", async () => {

    const file =
        document.getElementById("imageInput").files[0];

    if (!file) {

        alert("Please select an image first.");

        return;
    }

    const button =
        document.getElementById("analyzeBtn");

    button.innerText = "Analyzing...";

    const formData = new FormData();

    formData.append("file", file);

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/detect",
            {
                method: "POST",
                body: formData
            }
        );

        const data = await response.json();

        button.innerText = "Analyze Disaster";

        // KPI Cards

        document.getElementById("survivors").innerText =
            data.survivors_found;

        document.getElementById("priority").innerText =
            data.priority;

        document.getElementById("total-drones").innerText =
            data.recommended_drones;

        document.getElementById("success").innerText =
            data.mission_success_probability;


        // Mission Summary

        document.getElementById("mission-summary").innerText =
            data.mission_id;

        document.getElementById("priority-summary").innerText =
            data.priority;

        document.getElementById("eta-summary").innerText =
            data.estimated_rescue_time;

        document.getElementById("distance").innerText =
            data.distance_km + " km";


        // Resources

        document.getElementById("surveillance").innerText =
            data.surveillance_drones;

        document.getElementById("medical").innerText =
            data.medical_drones;

        document.getElementById("battery").innerText =
            data.battery_estimate;


        // Route

        document.getElementById("route").innerHTML =
            data.best_route.join("<br>↓<br>");


        // Progress Bar

        const percentage =
            parseInt(data.mission_success_probability);

        const progress =
            document.getElementById("progress-bar");

        progress.style.width =
            percentage + "%";

        progress.innerText =
            percentage + "%";


        // Activity Log

        document.getElementById("log").innerHTML = `
            [OK] Image Received<br>
            [OK] Survivors Detected: ${data.survivors_found}<br>
            [OK] Mission Created: ${data.mission_id}<br>
            [OK] Route Optimized<br>
            [OK] Resources Allocated
        `;

    }

    catch (error) {

        console.error(error);

        button.innerText = "Analyze Disaster";

        alert("Could not connect to Phoenix backend.");

    }

});