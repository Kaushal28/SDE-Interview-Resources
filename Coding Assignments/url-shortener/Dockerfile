FROM python:3.9-alpine3.13

# install uvicorn and gunicorn
RUN apk add --no-cache --virtual .build-deps gcc libc-dev make \
    && pip install uvicorn==0.14.0 gunicorn==20.1.0 \
    && apk del .build-deps gcc libc-dev make

RUN apk add --update --no-cache g++ gcc libxslt-dev \
    libressl libressl-dev libxml2-dev xmlsec-dev xmlsec

# set working directory
WORKDIR /opt

COPY ./requirements.txt ./requirements.txt
# install python requirements
RUN pip install -r ./requirements.txt
COPY ./start.sh ./start.sh
COPY ./src ./src

# gunicorn runs on port 80
EXPOSE 80

ENTRYPOINT  [ "/bin/sh", "start.sh" ]
