# \# ***Project Phoenix***

# 

# \### *Autonomous Multi-Agent Disaster Response System*

# 

# Project Phoenix is an AI-powered disaster response platform that assists rescue teams during floods, earthquakes, landslides, and other emergency situations.

# 

# The system uses computer vision, mission planning, route optimization, and resource allocation agents to analyze disaster imagery and generate actionable rescue missions in real time.

# 

# 

# \## **Problem Statement**

# 

# During natural disasters, rescue teams often face:

# 

# \- Limited situational awareness

# \- Delayed decision making

# \- Resource allocation challenges

# \- Inefficient rescue routing

# 

# Project Phoenix aims to reduce response time by automatically analyzing disaster scenes and generating optimized rescue plans.

# 

# 

# \## **Features**

# 

# \### AI Survivor Detection

# \- Detects survivors from aerial disaster imagery using YOLOv8.

# \- Estimates the number of people requiring assistance.

# 

# \### Mission Planning Agent

# \- Generates rescue missions based on detected survivor count.

# \- Assigns mission priority levels.

# 

# \### Route Optimization Agent

# \- Computes the optimal rescue route.

# \- Minimizes travel distance and rescue time.

# 

# \### Resource Allocation Agent

# \- Allocates surveillance and medical drones.

# \- Estimates battery requirements.

# \- Predicts mission success probability.

# 

# \### Phoenix Command Center Dashboard

# \- Interactive disaster response dashboard.

# \- Displays mission intelligence in real time.

# 

# 

# \## **System Architecture**

# 

# Disaster Image

# &#x20;      ↓

# YOLO Detection Agent

# &#x20;      ↓

# Mission Planning Agent

# &#x20;      ↓

# Route Optimization Agent

# &#x20;      ↓

# Resource Allocation Agent

# &#x20;      ↓

# Phoenix Command Center Dashboard

# 

# 

# 

# \## **Tech Stack**

# 

# \### Backend

# \- FastAPI

# \- Python

# 

# \### AI \& Computer Vision

# \- YOLOv8

# \- OpenCV

# 

# \### Optimization

# \- NetworkX

# 

# \### Frontend

# \- HTML

# \- CSS

# \- JavaScript

# 

# \### Version Control

# \- Git

# \- GitHub

# 

# 

# \## **Project Structure**

# 

# project-phoenix/

# │

# ├── backend/

# │   ├── api/

# │   │   ├── mission\_planner.py

# │   │   ├── route\_optimizer.py

# │   │   └── resource\_allocator.py

# │   │

# │   ├── detection/

# │   │   └── detector.py

# │   │

# │   ├── main.py

# │   └── requirements.txt

# │

# ├── frontend/

# │   ├── index.html

# │   ├── style.css

# │   └── script.js

# │

# └── README.md

# 

# 

# \## **Workflow**

# 

# 1\. Upload disaster image.

# 2\. AI detects survivors.

# 3\. Mission planner generates rescue mission.

# 4\. Route optimizer computes best path.

# 5\. Resource allocator assigns drones.

# 6\. Dashboard displays mission intelligence.

# 

# 

# \## **Future Scope**

# 

# ***- Live drone integration***

# ***- Real-time video analysis***

# ***- Multi-drone coordination***

# ***- GIS map integration***

# ***- Satellite imagery processing***

# ***- Autonomous rescue swarm deployment***

# 

# 

# \## **Team Phoenix**

# 

# \### Swarnim Kumar Sahu

# \- AI Development

# \- FastAPI Backend

# \- YOLOv8 Integration

# \- Route Optimization

# \- Resource Allocation System

# 

# \### Vidisha Choudhary

# \- Research \& Problem Analysis

# \- Idea Finalization

# \- Presentation Design

# \- Demo Video Production

# 

# Project Phoenix - Building AI-powered disaster response systems for faster and smarter rescue operations.

