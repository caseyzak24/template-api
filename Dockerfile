FROM python:3.7 AS prod
RUN pip install sqlalchemy psycopg2 pandas numpy flask
# etc.

FROM prod AS dev
RUN pip install pytest pytest-watch pytest-testmon pytest-cov ipython
