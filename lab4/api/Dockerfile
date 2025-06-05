FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

ENV \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.7.1 \
    POETRY_HOME=/opt/poetry

RUN curl -sSL https://install.python-poetry.org | python3 - --version ${POETRY_VERSION} && \
    ln -s ${POETRY_HOME}/bin/poetry /usr/local/bin/poetry && \
    poetry config virtualenvs.create false

WORKDIR /app
COPY pyproject.toml poetry.lock* /app/

RUN poetry install --no-root --no-dev

COPY service /app/service