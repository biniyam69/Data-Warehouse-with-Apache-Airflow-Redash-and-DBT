FROM apache/airflow:2.3.3
COPY requirements.txt /requirements.txt
COPY dbt_project.yml /dbt_project.yml
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /requirements.txt --use-deprecated=legacy-resolver
