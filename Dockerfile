FROM continuumio/miniconda3:latest AS production
# I like conda so I often start with it
RUN conda install sqlalchemy psycopg2 pandas numpy --yes

FROM production AS development
RUN pip install pytest pytest-watch ipython
