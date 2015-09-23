FROM debian:wheezy

RUN  apt-get update && apt-get upgrade && apt-get install -y minidlna
COPY ./run.sh /run.sh

ENTRYPOINT ["/run.sh"]
