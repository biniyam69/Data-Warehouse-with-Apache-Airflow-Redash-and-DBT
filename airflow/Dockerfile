FROM apache/airflow:2.2.0

COPY . /opt/airflow/project

WORKDIR /opt/airflow/project


COPY run.sh /
RUN chmod +x /run.sh

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Specify the entrypoint or command to execute when the container starts
CMD ["/run.sh"]
