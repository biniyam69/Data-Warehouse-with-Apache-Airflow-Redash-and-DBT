# Data Pipeline and Reporting Automation


Welcome to a project focused on deploying sensors to businesses and collecting data to provide critical intelligence. In this guide, I'll walk you through deploying our data warehouse, orchestration service, ELT tool, and setting up Redash for data visualization.

## Core Tasks

### Data Warehouse Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/biniyam69/Data-Warehouse-with-Apache-Airflow-Redash-and-DBT-.git datawarehouse
   cd datawarehouse
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Navigate to the Airflow directory and build Docker containers:
   ```bash
   cd airflow
   docker-compose build
   ```

4. Start Airflow and the associated services:
   ```bash
   docker-compose up -d
   ```

5. Access Airflow web server at http://localhost:8080.

### Redash Setup

1. Navigate to the Redash directory:
   ```bash
   cd redash
   ```

2. Create an environment file named `.env` with the following contents:
   ```
   REDASH_HOST=http://localhost/redash
   PYTHONUNBUFFERED=0
   REDASH_LOG_LEVEL=INFO
   REDASH_REDIS_URL=redis://redis:6379/0
   POSTGRES_PASSWORD=password
   REDASH_COOKIE_SECRET=redash-selfhosted
   REDASH_SECRET_KEY=redash-selfhosted
   REDASH_DATABASE_URL={postgresql+psycopg2://username:password@host/dbname}
   ```

   Replace `{postgresql+psycopg2://username:password@host/dbname}` with your PostgreSQL database URL.

3. Create and initialize the Redash database:
   ```bash
   docker-compose run --rm server create_db
   ```

4. Start Redash:
   ```bash
   docker-compose up -d
   ```

5. Access Redash dashboard at http://localhost:5000.

## Dataset
---
We will be using the pNEUMA drone dataset and do analysis on it

![Screenshot from 2024-03-20 15-59-43](https://github.com/biniyam69/Data-Warehouse-with-Apache-Airflow-Redash-and-DBT-/assets/91191700/47077a79-7021-4f43-bd4b-62371a1b3a1c)
---

![Screenshot from 2024-03-20 15-59-29](https://github.com/biniyam69/Data-Warehouse-with-Apache-Airflow-Redash-and-DBT-/assets/91191700/19827817-5ba8-43fd-8c11-4077db0836c1)

---

## Screenshots

### Airflow & DBT
- Two Dags App Screenshot
  ---
![DAGs](https://github.com/biniyam69/AI-Contract-Lawyer/assets/91191700/bbb4dd87-65e0-4786-b33b-bac7c5fec2d9)
  ---
- The Actual Acyclic Graph
  ---
  ![Directed Asyclic Graph](https://github.com/biniyam69/AI-Contract-Lawyer/assets/91191700/beab22bd-bdb5-48ce-8893-ca6a5b2294a7)
  ---
- DBT tasks with graph App Screenshot
  ---
  ![dbt-dags](https://github.com/biniyam69/AI-Contract-Lawyer/assets/91191700/853090c9-3d97-4f99-9213-b9e01d752dcd)
  ---

### Redash Dashboard
- Redash Dashboard 1
  ---
  ![redash-board I](https://github.com/biniyam69/AI-Contract-Lawyer/assets/91191700/d75249b6-d737-4442-8baa-17ffd0365cba)
  ---

- Redash Dashboard 2
  ---
  ![redash-board II](https://github.com/biniyam69/AI-Contract-Lawyer/assets/91191700/69ec2e3e-b7c6-4864-908e-eda9e01a2f79)
  ---

## Tech Stacks
- PostgreSQL
- Docker
- Redash
- Airflow
- DBT

## Authors
- [@Biniyam69](https://github.com/biniyam69)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
---
