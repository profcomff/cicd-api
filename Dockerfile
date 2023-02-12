FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11
ENV APP_NAME=app
ENV APP_MODULE=${APP_NAME}.routes.base:app

# Docker installation
RUN apt-get update \
    && apt-get install -y ca-certificates curl gnupg lsb-release \
    && mkdir -m 0755 -p /etc/apt/keyrings \
    && (curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg) \
    && echo \
        "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
        $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null \
    && apt-get update \
    && apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

COPY ./requirements.txt /app/
RUN pip install -U -r /app/requirements.txt

COPY ./alembic.ini /alembic.ini
COPY ./migrations /migrations/

COPY ./${APP_NAME} /app/${APP_NAME}

COPY ./scripts /app/scripts
