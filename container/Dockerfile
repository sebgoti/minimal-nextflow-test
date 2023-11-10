FROM python:3.10-slim as python-base

WORKDIR /app
RUN apt-get update && \
    apt-get clean
COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.10-slim
WORKDIR /app
COPY --from=python-base /root/.cache /root/.cache
COPY --from=python-base /app/requirements.txt .
RUN pip install -r requirements.txt && rm -rf /root/.cache