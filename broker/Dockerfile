FROM ubuntu

RUN apt-get update
RUN apt-get install -y mosquitto

CMD /bin/sh -c 'service mosquitto start; sleep 10; tail -f /var/log/mosquitto/mosquitto.log'

