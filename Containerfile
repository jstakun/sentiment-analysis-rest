FROM registry.access.redhat.com/ubi8/ubi-minimal
MAINTAINER Jaroslaw Stakun jstakun@redhat.com
ARG PIP_INDEX_URL
ARG PIP_TRUSTED_HOST
ENV APP_ROOT=/app
WORKDIR ${APP_ROOT}
COPY ./requirements.txt ./*.py ${APP_ROOT}/
RUN microdnf install -y python39 && \
    python3.9 -m pip install --upgrade pip --no-cache-dir -r requirements.txt && \
    chown -R 1001:root $APP_ROOT && \
    chmod g+rw $APP_ROOT 
USER 1001
EXPOSE 8080
CMD ["gunicorn", "wsgi", "--config", "gunicorn_config.py"]
