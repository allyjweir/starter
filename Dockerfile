FROM python:3.9.6-slim

RUN pip install poetry==1.1.7

RUN adduser --disabled-password nonroot
USER nonroot
WORKDIR /home/nonroot/starter

COPY --chown=nonroot:nonroot poetry.lock pyproject.toml .

RUN poetry install --no-interaction --no-ansi --no-root

COPY --chown=nonroot:nonroot . .

ENTRYPOINT ["/bin/bash", "/starter/entrypoint.sh"]