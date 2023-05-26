FROM ubuntu:22.04

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
  build-essential \
  make \
  gcc \
  jq \
  python3 \
  python3-dev \
  python3-pip

RUN pip install flask flask_restful multiprocess

COPY app/main.py /app/main.py
WORKDIR /app
CMD [ "/app/main.py" ]