
# 🌏 Air Pollution China - ETL Data Pipeline Project

This project is an end-to-end ETL (Extract, Transform, Load) data pipeline that processes air pollution data from China using **Kestra**, stores it in a **PostgreSQL** database, and visualizes it in **Power BI** for analysis.

---

## 📁 Folder Structure

```
Air-Pollution-China/
├── Dataset/
│   └── air_pollution_china.csv           # Raw dataset
│   └── processed.csv                     # Transformed dataset
├── ETL Tasks/
│   └── task_1(extract).py                 # Download raw CSV using Python
│   └── task_2(transform).py               # Data Cleaning + Feature Engineering
│   └── task_3(load).py                    # Load to PostgreSQL
│   └── verify.py                          # Fetch count from DB
├── Flows/
│   └── air_pollution_china.yaml
├── AirPollutionDashboard.pbix              # Power BI dashboard
├── commands.txt
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── sql_commands.sql
├── README.md                             # 📄 Project documentation
```

---

## 🛠️ Tech Stack Used

| Layer        | Tools / Tech                                  |
|--------------|-----------------------------------------------|
| Orchestration | 🟦 Kestra (Docker-based)                      |
| Language     | 🐍 Python (pandas, SQLAlchemy)                 |
| Storage      | 🐘 PostgreSQL                                  |
| Visualization| 📊 Power BI                                    |
| Versioning   | 🔁 Git / GitHub                                |

---

## ⚙️ How to Run This Project Locally

### 1. Clone the repo
```bash
git clone https://github.com/tippu45/air-pollution-china.git
cd air-pollution-china
```

### 2. Start Kestra with Docker
```bash
docker compose up -d
```

### 3. Run ETL Flows (inside Kestra UI)
- Visit `http://localhost:8080`
- Upload and execute flows in this order:
  1. `extract_task.yaml`
  2. `transform_task.yaml`
  3. `load_task.yaml`
  4. `count_query_task.yaml` *(Optional verification)*

---

## 🔄 Techniques Used in `transform_task.yaml`

- **Handling Missing Values**: Removed or imputed null values in weather or pollutant fields.
- **Encoding**:
  - Converted categorical fields: `Weather Condition`, `Season`, `City`, `Day of Week` to string types.
- **Scaling**:
  - Applied **PowerTransformer** on columns like `PM2.5`, `Temperature`, `Humidity`.
- **Feature Engineering**:
  - Created `Is_Weekend`, `Pollution_Category`, `AQI_Level`, and `Day_Time_Slot` columns.
- **Outlier Treatment**: Identified outliers using IQR/boxplot logic (optional).

---

## 🧠 Sample SQL Query (Used in `count_query_task.yaml`)

```sql
SELECT COUNT(*) FROM "Air_Pollution_Data";
```

---

## 📊 Visualizations (Power BI)

> The visualizations below are created using `processed.csv`.

| Chart Type | Insight |
|------------|---------|
| 📈 Line Chart | Pollutant levels vs Time |
| 📊 Bar Chart | City-wise comparison of AQI |
| 🌍 Map View | Pollution spread based on Latitude/Longitude |
| ☁️ Weather-Pollution | How weather affects pollutant levels |

### Screenshots 📸

Add actual screenshots after you build your dashboard:
```
PowerBI/
├── viz1_line_chart.png
├── viz2_map.png
├── viz3_heatmap.png
```
