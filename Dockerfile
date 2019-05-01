FROM python:3.7 AS base
WORKDIR /app
RUN pip install sqlalchemy psycopg2 pandas numpy flask
# etc.

FROM base AS dev
RUN pip install pytest pytest-watch pytest-testmon pytest-cov ipython

FROM base as prod
# Copy stuff

