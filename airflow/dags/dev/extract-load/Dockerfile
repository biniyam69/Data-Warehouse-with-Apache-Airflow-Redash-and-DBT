FROM python:3.10.2

ADD . /scripts
WORKDIR /scripts

# RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /scripts
# USER appuser

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

RUN ls -la
ENTRYPOINT [ "./run.sh" ]