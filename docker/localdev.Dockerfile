FROM python:2.7.18-buster as builder

RUN python -m virtualenv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY ./requirements/dev.txt requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt

FROM python:2.7.18-buster as base

COPY --from=builder /opt/venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app/

COPY src/ ./src
COPY tests/ ./tests

CMD []
