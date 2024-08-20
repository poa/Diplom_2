# Дипломный проект. Задание 2: Тестирование REST API

❗ АКТУАЛИЗИРОВАТЬ ПО ЗАВЕРШЕНИИ

## Автотесты для REST API сервиса Stellar Burgers

## Реализованные сценарии


## Структура проекта

- `api`
- `tests` - пакет, содержащий тесты, разделенные по классам. Например, `bun_test.py`, `burger_test.py` и т.д.

## Запуск автотестов

Установка зависимостей

```shell
pip install -r requirements.txt
```

Запуск тестов с подробным выводом в консоль

```shell
pytest -v
```

Запуск тестов с формированием отчёта allure

```shell
pytest -v --alluredir=allure-results
```

Просмотра отчёта allure (allure предварительно должен быть [установлен](https://allurereport.org/docs/install/))

```shell
allure serve allure-results
```
