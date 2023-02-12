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

1) Перейдите в папку проекта

2) Создайте виртуальное окружение командой:
```console
foo@bar:~$ python3 -m venv ./venv/
```

3) Установите библиотеки
```console
foo@bar:~$ pip install -r requirements.txt
```
4) Запускайте приложение!
```console
foo@bar:~$ python -m app
```

## ENV-file description

`AUTH_URL` – url корня API авторизации профкома, по умолчанию `https://auth.api.test.profcomff.com/`
