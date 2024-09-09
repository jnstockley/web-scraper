FROM python:3.12.6-alpine3.20

ENV PATH="/root/.local/bin:$PATH"

ENV PYTHONPATH="/web-scrapper"

ENV PYTHONUNBUFFERED=1

RUN apk update

RUN apk add --no-cache curl gcc libressl-dev musl-dev libffi-dev

RUN python3 -m pip install --upgrade pip

RUN pip install --user pipx

RUN pipx install poetry

RUN apk del curl gcc libressl-dev musl-dev libffi-dev

RUN mkdir /web-scrapper

COPY . /web-scrapper

WORKDIR /web-scrapper

ENV SLEEP_TIME_SEC=21600

RUN poetry install --no-root

ENTRYPOINT ["poetry", "run", "python3", "src/main.py"]