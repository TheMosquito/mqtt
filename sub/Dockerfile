FROM ubuntu

RUN apt-get update
RUN apt-get install -y python-pip
RUN pip install paho-mqtt

COPY sub.py /

CMD python /sub.py

