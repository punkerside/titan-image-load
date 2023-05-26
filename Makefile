PROJECT = punkerside
SERVICE = load

build:
	docker build -t ${PROJECT}-${SERVICE} .

run: build
	export PROJECT=${PROJECT} && export SERVICE=${SERVICE} && docker compose up -d

stop:
	export PROJECT=${PROJECT} && export SERVICE=${SERVICE} && docker compose down