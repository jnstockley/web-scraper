FROM python:3.13.1-slim AS build

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    mkdir /web-scrapper

WORKDIR /web-scrapper

COPY poetry.lock /web-scrapper

COPY pyproject.toml /web-scrapper

RUN poetry install

COPY  src /web-scrapper/src

FROM python:3.13.1-slim

COPY --from=build /usr/local/ /usr/local/

COPY --from=build /root/.cache/pypoetry/virtualenvs  /root/.cache/pypoetry/virtualenvs

COPY --from=build /web-scrapper /web-scrapper

WORKDIR /web-scrapper

ENV PATH="/root/.local/bin:${PATH}"

ENV PYTHONPATH=/web-scrapper:$PYTHONPATH

HEALTHCHECK --interval=60s --timeout=10s --start-period=20s --retries=3 CMD [ "poetry", "run", "python3", "src/healthcheck.py" ]

ENTRYPOINT ["poetry", "run", "python3", "src/main.py"]
