def create_mission(survivor_count):

    if survivor_count >= 5:
        priority = "CRITICAL"
        drones = 3

    elif survivor_count >= 2:
        priority = "HIGH"
        drones = 2

    else:
        priority = "MEDIUM"
        drones = 1

    return {
        "mission_id": "PHX-001",
        "priority": priority,
        "recommended_drones": drones,
        "estimated_rescue_time": f"{survivor_count * 4} minutes"
    }
