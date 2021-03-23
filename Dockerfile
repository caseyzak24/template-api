FROM python:3.7 AS base
WORKDIR /app
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
ENV PATH="${PATH}:/root/.poetry/bin"
RUN poetry config settings.virtualenvs.create false
COPY poetry.lock pyproject.toml /app/
RUN poetry install --no-dev
EXPOSE 80

FROM base AS dev
RUN poetry install

FROM base as prod
COPY src src
COPY alembic alembic
COPY wsgi.py server.ini alembic.ini app.py /app/
CMD uwsgi --ini server.ini

FROM dev as test
COPY src src
COPY test test
COPY migrations migrations
COPY alembic.ini alembic.ini
