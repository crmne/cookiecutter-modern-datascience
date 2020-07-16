# Docker multistage build to reduce image size
FROM python:3.7 AS build
RUN python -m venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install mlflow psycopg2 mysqlclient boto3

FROM python:3.7-slim
COPY --from=build /opt/venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"
EXPOSE 5000/tcp
ENTRYPOINT [ "mlflow", "server", "--host", "0.0.0.0"]
CMD [ "--backend-store-uri", "sqlite:////mlruns/mlruns.db", \
      "--default-artifact-root", "/mlartifacts"]
