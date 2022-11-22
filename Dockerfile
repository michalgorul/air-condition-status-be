FROM python:3.10-slim-buster AS build

RUN apt-get update && \
    apt-get install -y --no-install-recommends git
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir --user

FROM python:3.10-slim-buster

WORKDIR /opt/air-status

COPY --from=build /root/.local /usr/local
COPY app app

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "app.main:app"]