FROM debian:wheezy

RUN  apt-get update -y && apt-get upgrade -y && apt-get install -y minidlna
COPY files/run.sh /run.sh

ENTRYPOINT ["/run.sh"]
