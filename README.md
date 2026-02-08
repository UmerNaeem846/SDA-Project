# SDA Project – Phase 1  
## Functional & Data-Driven GDP Analysis System

## 📌 Overview
This project is developed as **Phase 1 of the Software Design & Architecture (SDA) course project**.  
The system performs **data-driven GDP analysis** using **functional programming principles in Python**, strictly following the **Single Responsibility Principle (SRP)** and **configuration-based behavior**.

The application processes **World Bank GDP data**, applies filters and statistical operations based on a `config.json` file, and presents the results through a **dashboard with visualizations**.

---

## 🎯 Objectives
- Apply **functional programming concepts** in Python
- Enforce **Single Responsibility Principle (SRP)**
- Implement **configuration-driven logic** (no hardcoding)
- Analyze GDP data using **statistical operations**
- Visualize results using **multiple chart types**

---

## 🛠 Tech Stack
- **Programming Language:** Python
- **Libraries Used:**
  - `matplotlib` – Data visualization
  - `json` – Configuration handling
- **Data Source:** World Bank GDP CSV Dataset

---

## 📂 Project Structure
```
SDA-Project/
│
├── data/
│ └── world_bank_gdp.csv
│
├── config/
│ └── config.json
│
├── data_loader.py
├── data_processor.py
├── dashboard.py
├── main.py
│
├── requirements.txt
└── README.md
```
---

## ⚙️ Functional Programming Usage
The project extensively uses:
- `map()`
- `filter()`
- `lambda` functions
- List & dictionary comprehensions  

Traditional loop-based implementations are **minimized**, as per project constraints.

---

## ⚙️ Configuration-Driven Behavior
All logic is controlled via **`config.json`**, including:
- Selected **Region**
- Selected **Year**
- Statistical **Operation** (Average or Sum)
- Dashboard output preferences

⚠️ **No hardcoded values** for region, year, or operation exist in the source code.

---

## 📄 Sample `config.json`
```json
{
  "region": "South Asia",
  "year": 2019,
  "operation": "average",
  "dashboard": "output"
}
```
---
## ▶️ How to Run the Project

1. Clone the repository

       git clone https://github.com/UmerNaeem846/SDA-Project.git


2. Navigate to the project directory

       cd SDA-Project


3. Install dependencies

       pip install -r requirements.txt


4. Update config.json as needed

5. Run the dashboard

       python main.py

## ✅ Functional Requirements Implemented

- Load GDP data from CSV

- Data cleaning and type validation

- **Filtering by:**
  - Region
  
  - Year
  
  - Country

- **Statistical computations:**

  - Average GDP of a Region
  
  - Average GDP of a Country
  
  - Sum of GDP of a Region

- Configuration-based execution

- Dashboard visualization

---


## 📊 Visualizations

The dashboard generates multiple visualizations, including:

**Region-wise GDP plots**

  - Bar Chart
  
  - Pie Chart

**Year-specific GDP plots**

  - Line Graph

  - Histogram / Scatter Plot

**✔ Each graph includes:**

  - Title

  - Axis labels

---
## 🧩 Architecture & Design

The system follows modular design with clear responsibilities:

**1. Data Loader**
  
 - Loads CSV files
  
 - Handles missing or invalid files

**2. Data Processor**

 - Cleans and filters data
  
 - Performs statistical calculations
  
 - Uses functional programming constructs

**3. Dashboard / Presentation Layer**

 - Displays configuration values
  
 - Shows computed results
  
 - Generates charts and visualizations

---




