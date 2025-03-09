FROM ghcr.io/astral-sh/uv:0.6.5-python3.13-alpine

ADD . /app

WORKDIR /app

RUN uv sync --frozen --no-dev

ENTRYPOINT ["uv", "run", "main.py"]
