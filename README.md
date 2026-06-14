## Project Phoenix

**Autonomous Multi-Agent Disaster Response System**

Project Phoenix is an AI-powered disaster response platform that assists rescue teams during floods, earthquakes, landslides, and other emergency situations.

The system uses computer vision, mission planning, route optimization, and resource allocation agents to analyze disaster imagery and generate actionable rescue missions in real time.

---

## Problem Statement

During natural disasters, rescue teams often face:

* Limited situational awareness
* Delayed decision making
* Resource allocation challenges
* Inefficient rescue routing

Project Phoenix aims to reduce response time by automatically analyzing disaster scenes and generating optimized rescue plans.

---

## Features

### AI Survivor Detection

* Detects survivors from aerial disaster imagery using YOLOv8
* Estimates the number of people requiring assistance

### Mission Planning Agent

* Generates rescue missions based on detected survivor count
* Assigns mission priority levels

### Route Optimization Agent

* Computes the optimal rescue route
* Minimizes travel distance and rescue time

### Resource Allocation Agent

* Allocates surveillance and medical drones
* Estimates battery requirements
* Predicts mission success probability

### Phoenix Command Center Dashboard

* Interactive disaster response dashboard
* Displays mission intelligence in real time

---

## System Architecture

```text
Disaster Image
       ↓
YOLO Detection Agent
       ↓
Mission Planning Agent
       ↓
Route Optimization Agent
       ↓
Resource Allocation Agent
       ↓
Phoenix Command Center Dashboard
```

---

## Tech Stack

### Backend

* Python
* FastAPI

### AI & Computer Vision

* YOLOv8
* OpenCV

### Optimization

* NetworkX

### Frontend

* HTML
* CSS
* JavaScript

### Version Control

* Git
* GitHub

---

## Project Structure

```text
project-phoenix/

├── backend/
│   ├── api/
│   │   ├── mission_planner.py
│   │   ├── route_optimizer.py
│   │   └── resource_allocator.py
│   │
│   ├── detection/
│   │   └── detector.py
│   │
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

## Workflow

1. Upload a disaster image
2. AI detects survivors
3. Mission planner generates a rescue mission
4. Route optimizer computes the best route
5. Resource allocator assigns drones
6. Dashboard displays mission intelligence

---

## Future Scope

* Live drone integration
* Real-time video analysis
* Multi-drone coordination
* GIS map integration
* Satellite imagery processing
* Autonomous rescue swarm deployment

---

## Team

| Member                  | Contribution                                                             |
| ----------------------- | ------------------------------------------------------------------------ |
| Swarnim Sahu            | AI Development, Backend Engineering, Computer Vision, System Integration |
| Vidisha Choudhary       | Research, Idea Finalization, Presentation Design, Demo Video Production  |

```
```
