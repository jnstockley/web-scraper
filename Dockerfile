FROM jnstockley/poetry:1.8.5-python3.13.1 AS build

RUN apk update && \
    apk upgrade && \
    apk add alpine-sdk python3-dev musl-dev libffi-dev gcc curl openssl-dev cargo pkgconfig && \
    mkdir /web-scrapper

WORKDIR /web-scrapper

COPY poetry.lock /web-scrapper

COPY pyproject.toml /web-scrapper

RUN poetry install --no-root

COPY src /web-scrapper/src

FROM jnstockley/poetry:1.8.5-python3.13.1

COPY --from=build /root/.cache/pypoetry/virtualenvs  /root/.cache/pypoetry/virtualenvs

COPY --from=build /web-scrapper /web-scrapper

WORKDIR /web-scrapper

ENV PYTHONPATH=/web-scrapper:$PYTHONPATH

ENTRYPOINT ["poetry", "run", "python3", "src/main.py"]