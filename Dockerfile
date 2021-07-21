FROM python:3.9.6-slim

WORKDIR /starter

RUN pip install poetry==1.1.7

COPY poetry.lock pyproject.toml .

RUN poetry install --no-interaction --no-ansi --no-root

COPY . .

ENTRYPOINT ["/bin/bash", "/starter/entrypoint.sh"]