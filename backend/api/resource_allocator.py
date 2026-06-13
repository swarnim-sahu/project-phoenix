def allocate_resources(survivor_count, priority):

    if priority == "CRITICAL":

        return {
            "surveillance_drones": 2,
            "medical_drones": 2,
            "battery_estimate": "70%",
            "mission_success_probability": "95%"
        }

    elif priority == "HIGH":

        return {
            "surveillance_drones": 1,
            "medical_drones": 1,
            "battery_estimate": "35%",
            "mission_success_probability": "91%"
        }

    else:

        return {
            "surveillance_drones": 1,
            "medical_drones": 0,
            "battery_estimate": "20%",
            "mission_success_probability": "85%"
        }
