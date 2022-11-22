FROM python:3.10-slim-buster AS build

RUN apt-get update && \
    apt-get install -y --no-install-recommends git
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir --user

FROM python:3.10-slim-buster

WORKDIR /opt/device_map_api

COPY --from=build /root/.local /usr/local
COPY app app

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "5000", "app.main:app"]