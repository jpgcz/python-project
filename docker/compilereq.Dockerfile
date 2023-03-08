FROM python:2.7.18-buster

RUN pip install -U --no-cache-dir pip pip-tools

ENTRYPOINT ["pip-compile", "/requirements/dev.in" ,"-o", "/requirements/dev.txt"]
