FROM jupyter/datascience-notebook:ubuntu-20.04

RUN mamba install --quiet --yes \
    'boto3'

ADD cd4ml/ /cd4ml
WORKDIR /cd4ml

EXPOSE 8888
ENTRYPOINT ["start.sh", "jupyter", "lab"]
