FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 --no-cache-dir install --upgrade pip \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /home/wattx

COPY ./wattx/requirements.txt .
RUN pip install -r requirements.txt

COPY wattx/ .

WORKDIR /home/wattx/wattx

CMD ["/bin/bash", "start.sh"]