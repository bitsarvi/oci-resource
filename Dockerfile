FROM python:2-alpine

COPY dist/ocios-resource-*.tar.gz .

RUN apk add --no-cache gcc g++ libffi-dev openssl-dev

RUN pip install ocios-resource-*.tar.gz

RUN mkdir -p /opt/resource

RUN for script in check in out; do ln -s `which $script` /opt/resource/; done
