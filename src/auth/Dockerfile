# Dockerfile must be layer efficient
# Ex: If any changes occure in requirements.txt (COPY ./requirements.txt /app) step,
# the commands above to this step will not run, but all the commands
# after/following to that step (COPY ./requirements.txt /app), commands will run.
# This is called layer efficient Dockerfile

FROM python:3.10-slim-bullseye

# install system dependencies needed
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    pkg-config \
    libmariadb-dev \
    && pip install --no-cache-dir --upgrade pip

# creates /app in container if it does not already exist
# copy requirements.txt into /app
WORKDIR /app
COPY ./requirements.txt /app
# installing requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
# copy rest of the code into /app
COPY . /app

# exposing port 5000
EXPOSE 5000

# commands to run e.g. python3 server.py
CMD ["python3", "server.py"]
