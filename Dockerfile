FROM python:3.9-alpine
LABEL maintainer="rzmobiledev@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./scripts /scripts
COPY ./app /app

WORKDIR /app
EXPOSE 8000

RUN python -m venv /env && \
    /env/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev linux-headers && \
    /env/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /env/bin/pip install -r /tmp/requirements.dev.txt; \
    fi && \
    rm -rf /tmp && apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        rizal && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R rizal:rizal /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts


ENV PATH="/scripts:/env/bin:$PATH"

USER rizal

CMD [ "executable.sh" ]



