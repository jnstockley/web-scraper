FROM jnstockley/poetry:1.8.5

USER root

RUN mkdir /web-scrapper

RUN chown -R python3:python3 /web-scrapper

USER python3

COPY . /web-scrapper

WORKDIR /web-scrapper

ENV SLEEP_TIME_SEC=21600

RUN poetry install --no-root

ENTRYPOINT ["poetry", "run", "python3", "src/main.py"]
