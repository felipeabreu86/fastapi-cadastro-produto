FROM python:3.12.3-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH='/'

COPY ./poetry.lock /
COPY ./pyproject.toml /

RUN apt-get update -y \
    && apt-get install curl -y \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.create false \
    && poetry install --no-root --no-dev \
    && apt-get remove curl -y

COPY ./app /app
WORKDIR /app
