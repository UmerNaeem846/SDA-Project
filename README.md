# Generic Concurrent Real-Time Data Processing Pipeline

## Project Overview

This project implements a **generic concurrent real-time data processing pipeline** built using Python's multiprocessing framework. The system dynamically processes unseen datasets using a configuration-driven architecture and provides real-time visualization of both processed data and pipeline telemetry.

The pipeline is designed to be **dataset-agnostic**, meaning it can process completely different datasets without changing the code, simply by updating the configuration file.

---

# Architecture

The system follows a **modular pipeline architecture** consisting of three independent modules:

Input Module → Core Processing Module → Output Dashboard

The pipeline also includes a **Telemetry Monitor** for observing pipeline health.

---

# Key Features

- Configuration-driven architecture
- Generic dataset processing
- Multiprocessing pipeline
- Producer–Consumer queues
- Scatter–Gather worker pattern
- Cryptographic signature verification
- Functional Core + Imperative Shell design
- Sliding window running average
- Real-time dashboard visualization
- Pipeline telemetry monitoring
- Backpressure handling using bounded queues

---

# System Architecture

Pipeline flow:
Dataset
↓
Input Module
↓
Raw Queue
↓
Worker Processes (Parallel)
↓
Verified Queue
↓
Aggregator
↓
Processed Queue
↓
Dashboard Visualization

Telemetry Monitor observes all queues and provides **live pipeline health indicators**.

---

# Modules Description

## Input Module

Responsible for:

- Reading dataset rows
- Applying schema mapping
- Converting raw dataset columns to internal generic format
- Streaming packets into the pipeline

File:
input_module/input_reader.py


---

## Schema Mapper

Maps dataset columns to internal pipeline variables based on the configuration file.

File:
utils/schema_mapper.py


---

## Core Processing Module

### Worker Processes

Workers perform **stateless cryptographic verification** of incoming packets.

File:
core_module/worker.py


---

### Verifier

Uses PBKDF2-HMAC hashing to verify packet authenticity.

File:
core_module/verifier.py


---

### Aggregator

Implements the **Functional Core pattern** to compute a sliding window running average.

File:
core_module/aggregator.py


---

## Output Dashboard

Displays:

- Real-time sensor values
- Running average visualization
- Pipeline telemetry indicators

File:
output_module/dashboard.py


---

## Telemetry Monitor

Monitors queue usage and publishes telemetry data to the dashboard.

File:
telemetry/telemetry_monitor.py


---

# Configuration File

The pipeline behavior is controlled entirely by:
config/config.json


Key sections include:

### Dataset Path
dataset_path


### Pipeline Dynamics
input_delay_seconds
core_parallelism
stream_queue_max_size


### Schema Mapping

Defines how dataset columns map to internal pipeline variables.

### Processing

Defines stateless and stateful operations.

### Visualizations

Defines which charts appear on the dashboard.

---

# Functional Programming Concepts Used

- Pure functions
- Map and Reduce operations
- Immutable transformations
- Functional core for calculations

---

# Concurrency Model

The system uses **Python multiprocessing** with two main data streams:

### Raw Data Stream
Input → Raw Queue → Workers


### Processed Data Stream
Workers → Verified Queue → Aggregator → Processed Queue


Queues are bounded to create **automatic backpressure control**.

---

# Telemetry Dashboard

The dashboard shows three queue states:

- Raw Queue
- Verified Queue
- Processed Queue

Color indicators:

| Usage | Color |
|------|------|
| 0–30% | Green |
| 30–70% | Yellow |
| 70–100% | Red |

---

# Running the Project

Install dependencies:
pip install matplotlib


Run the system:
python main.py


---

# Project Structure

SDA-Project/
│
├── data/
│ └── sample_sensor_data.csv
│
├── config/
│ └── config.json
│
├── core/
│ └── aggregator.py
│ └── verifier.py
│ └── worker.py
│
├── input/
│ └── input_reader.py
│
├── output/
│ └── dashboard.py
│
├── telemetry/
│ └── telemetry_monitor.py
│
├── utils/
│ └── schema_mapper.py
│
├── main.py
│
└── README.md


---

# Design Patterns Used

- Producer–Consumer
- Scatter–Gather
- Observer Pattern
- Functional Core / Imperative Shell
- Configuration-Driven Architecture

---

# Deliverables

This repository contains:

- Complete runnable Python pipeline
- Configuration file
- Class diagram (PlantUML)
- Sequence diagram (PlantUML)
- README documentation

---

# Authors

**Waleed Omer**  
Core Processing Module

**Umar Naeem**  
Input Module, Output Dashboard, Telemetry System