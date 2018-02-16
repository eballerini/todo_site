# this image works but is HUGE and there may be vulnerabilities
FROM python:3.4

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY . /src
WORKDIR /src

RUN pip install -r requirements.txt

# exposes the port 8000
EXPOSE 8000

# CMD specifcies the command to execute to start the server running.
#CMD ["./start.sh"]
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# running in https
CMD ["python", "manage.py", "runserver_plus", "0.0.0.0:8000", "--cert-file", "tmp-cert.crt"]