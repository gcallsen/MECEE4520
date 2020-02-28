FROM python:3.6-slim

USER root

RUN mkdir /etc/demo
COPY predict.sh /etc/demo/predict.sh

COPY class_demo-0.1.0.tar.gz /tmp
RUN pip3 install "file:///tmp/class_demo-0.1.0.tar.gz#egg=class-demo"
RUN rm -f /tmp/class_demo-0.1.0.tar.gz

# change this to invoke predict every 5 seconds
CMD bash -C '/etc/demo/predict.sh'
