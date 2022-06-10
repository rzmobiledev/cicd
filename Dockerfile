FROM python:3.9-alpine
LABEL maintainer="rzmobiledev@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./scripts /scripts
COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN python -m venv /env && \
    /env/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
    build-base postgresql-dev musl-dev && \
    /env/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && apk del .tmp-build-deps && \
    chmod -R +x /scripts && \
    adduser \
        --disabled-password \
        --no-create-home \
        rizal

ENV PATH="/env/bin:$PATH"

USER rizal

# CMD [ "executable.sh" ]



