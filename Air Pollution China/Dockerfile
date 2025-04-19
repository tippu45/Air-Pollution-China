FROM kestra/kestra:latest

USER root

# Install Python and pip packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    pip3 install --upgrade pip && \
    pip3 install pandas numpy scikit-learn sqlalchemy psycopg2-binary pymysql cryptography geopandas shapely

# Optional: Clean cache to reduce image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
