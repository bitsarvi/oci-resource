FROM python:2-alpine

COPY dist/ocios-resource-*.tar.gz .

RUN pip install ocios-resource-*.tar.gz

RUN mkdir /opt/resource

RUN for script in check in out; do ln -s $(which script) /opt/resource/; done