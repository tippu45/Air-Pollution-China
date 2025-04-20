---

```markdown
# 🌏 Air Pollution China - ETL Data Pipeline Project

This project is an end-to-end ETL (Extract, Transform, Load) data pipeline that processes air pollution data from China using **Kestra**, stores it in a **PostgreSQL** database, and visualizes it in **Power BI** for analysis.

---

## 📁 Folder Structure

```
Air-Pollution-China/
├── Dataset/
│   └── air_pollution_china.csv           # Raw dataset
│   └── processed.csv                     # Transformed dataset
├── Kestra-Flows/
│   └── extract_task.yaml                 # Download raw CSV using Python
│   └── transform_task.yaml               # Data Cleaning + Feature Engineering
│   └── load_task.yaml                    # Load to PostgreSQL
│   └── count_query_task.yaml             # Fetch count from DB
├── PowerBI/
│   └── AirPollutionDashboard.pbix        # Power BI dashboard
├── Scripts/
│   └── load_to_postgres.py               # Alternative local load script
├── README.md                             # 📄 Project documentation
└── .env                                  # Optional: environment config
```

---

## 🛠️ Tech Stack Used

| Layer        | Tools / Tech                                  |
|--------------|-----------------------------------------------|
| Orchestration | 🟦 Kestra (Docker-based)                      |
| Language     | 🐍 Python (pandas, SQLAlchemy)                 |
| Storage      | 🐘 PostgreSQL (Docker)                         |
| Visualization| 📊 Power BI                                    |
| Versioning   | 🔁 Git / GitHub                                |
| Others       | 🐳 Docker, psycopg2, pymysql, pip, SQLAlchemy  |

---

## ⚙️ How to Run This Project Locally

### 1. Clone the repo
```bash
git clone https://github.com/your-username/air-pollution-etl-pipeline.git
cd air-pollution-etl-pipeline
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

### 4. Load data manually (Optional - Python)
```bash
cd Scripts/
python load_to_postgres.py
```

---

## 🔄 Techniques Used in `transform_task.yaml`

- **Handling Missing Values**: Removed or imputed null values in weather or pollutant fields.
- **Encoding**:
  - Converted categorical fields: `Weather Condition`, `Season`, `City`, `Day of Week` to string types.
- **Scaling**:
  - Applied **MinMaxScaler** on columns like `PM2.5`, `Temperature`, `Humidity`.
- **Feature Engineering**:
  - Created `Is_Weekend`, `Pollution_Category`, `AQI_Level`, and `Day_Time_Slot` columns.
- **Outlier Treatment**: Identified outliers using IQR/boxplot logic (optional).
- **Normalization**: For better ML-readiness and consistency.

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
| 📅 Heatmap | Pollution by Day of Week & Hour |
| ☁️ Weather-Pollution | How weather affects pollutant levels |

### Screenshots 📸

Add actual screenshots after you build your dashboard:
```
PowerBI/
├── viz1_line_chart.png
├── viz2_map.png
├── viz3_heatmap.png
```

Or embed them in markdown:

```markdown
![Line Chart](PowerBI/viz1_line_chart.png)
![Map View](PowerBI/viz2_map.png)
```

---

## 🧪 Sample Kestra Flow: `load_task.yaml`

```yaml
id: load_to_postgres
type: io.kestra.plugin.scripts.python.Script
taskRunner:
  type: io.kestra.plugin.core.runner.Process
beforeCommands:
  - python3 -m venv .venv
  - . .venv/bin/activate
  - pip install pandas sqlalchemy psycopg2
script: |
  import pandas as pd
  from sqlalchemy import create_engine
  df = pd.read_csv('processed.csv')
  engine = create_engine("postgresql+psycopg2://postgres:2002@host.docker.internal:5432/ETL_Pipeline")
  df.to_sql("Air_Pollution_Data", engine, if_exists='replace', index=False)
  print("Loaded data into PostgreSQL")
```

---

## 🧾 Future Work

- Add **machine learning models** to predict AQI.
- Automate scheduling using **Kestra triggers**.
- Stream real-time data using **Kafka or APIs**.

---

## 🤝 Contributors

- 👤 [Your Name] - Developer & Analyst

---

## 📄 License

This project is open-sourced under the MIT License.

---

```

Let me know if you want me to:

- Add image links
- Turn this into a `README.md` file and save it
- Create GIFs of dashboard interaction
- Help you publish it on GitHub or Power BI Service

Happy documenting! 📝
