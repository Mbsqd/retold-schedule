FROM python:3.14.2-trixie

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# install uv
RUN pip install --no-cache-dir uv

# copy dependency files first (for cache)
COPY pyproject.toml uv.lock ./

# install dependencies
RUN uv sync --frozen --no-dev

# copy project
COPY src ./src

# runtime command
CMD ["uv", "run", "python", "-m", "src.main"]