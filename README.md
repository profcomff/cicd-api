# ci-api

API для запуска CI тасков на серверах.
Для использования сделайте запрос следующего вида по адресу, на котором настроено CI API для вашего сервера

```
curl -X 'POST' \
  'https://ci.api.profcomff.com/{action}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token {token}' \
  -d '{
  "repo_url": "string",
  "commit_hash": "string"
}'
```

## Запуск

На проде запуск производится через Docker Compose

```docker-compose
version: '3'

services:
  ci-api:
    image: ghcr.io/profcomff/ci-api:latest
    restart: always
    environment:
      - AUTH_URL=https://auth.api.profcomff.com/
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    networks:
      web:
        aliases:
          - ci_api

networks:
  web:
    external: true
    name: web
```

## ENV-file description

`AUTH_URL` – url корня API авторизации профкома, по умолчанию `https://auth.api.test.profcomff.com/`
