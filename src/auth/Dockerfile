# Dockerfile must be layer efficient
# Ex: If any changes occure in requirements.txt (COPY ./requirements.txt /app),
# the commands above to it will not run but all the command
# following to that (COPY ./requirements.txt /app) commands will run.
# This is called layer efficient Dockerfile

FROM python:3.10-slim-bullseye

RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
    build-essential default-libmysqlclient-dev \
    && pip install --no-cache-dir --upgrade pip

# creates /app in container if it does not already exist
# copy requirements.txt into /app
WORKDIR /app
COPY ./requirements.txt /app
# installing requirements.txt
RUN pip install --no-cahce-dir /app/requirements.txt
# copy rest of the code into /app
COPY . /app

# exposing port 5000
EXPOSE 5000

# commands to run e.g. python3 server.py
CMD [ "python3", "server.py"]
