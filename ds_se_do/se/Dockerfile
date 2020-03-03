FROM python:3.6-slim

USER root

RUN mkdir /etc/demo
COPY predict.sh /etc/demo/predict.sh

ARG PKG_FILENAME

COPY $PKG_FILENAME /tmp

#RUN ls -alh
#RUN python setup.py sdist
#COPY ds_se_do-0.2.0.tar.gz /tmp
#RUN pip3 install "file:///tmp/ds_se_do-0.2.0.tar.gz#egg=class-demo"
#RUN rm -f /tmp/ds_se_do-0.2.0.tar.gz
#RUN pip3 install $PKG_FILENAME
RUN pip3 install /tmp/$PKG_FILENAME

RUN rm -f /tmp/$PKG_FILENAME

CMD bash -C '/etc/demo/predict.sh'
