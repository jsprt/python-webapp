FROM python:3.8.6-alpine

COPY . /app
WORKDIR /app
RUN \
    apk add --no-cache python3 postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps

ENTRYPOINT ["python3"]
CMD ["app.py"]