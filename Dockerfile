FROM debian:wheezy

RUN  apt-get update && apt-get upgrade && apt-get install -y minidlna
COPY files/run.sh /run.sh

ENTRYPOINT ["/run.sh"]
