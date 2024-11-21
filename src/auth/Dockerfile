# Dockerfile must be layer efficient
# Ex: If any changes occure in requirements.txt (COPY ./requirements.txt /app),
# the commands above to it will not run but all the command
# following to that (COPY ./requirements.txt /app) commands will run.
# This is called layer efficient Dockerfile

FROM Pyton:3.10-slim-bullseye

RUN apt-get-update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
    build-essential default-limmysqlclient-dev \
    && pip install --no-cache-dir --upgrade pip

WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --no-cahce-dir /app/requirements.txt
COPY . /app

EXPOSE 5000

CMD [ "python3", "server.py"]
