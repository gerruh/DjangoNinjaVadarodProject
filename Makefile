.PHONY: install run migrate makemigrations test lint format shell

PYTHON = python
MANAGE = ${PYTHON} manage.py
DC = docker compose
APP = web

# Python
mm:
	${MANAGE} makemigrations

m:
	${MANAGE} migrate

# Docker

bd:
	${DC} up --build -d


up:
	${DC} up


dn:
	${DC} down


dnv:
	${DC} down -v