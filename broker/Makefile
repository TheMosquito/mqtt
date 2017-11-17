
.PHONY: all
all:
	make build
	make run

.PHONY: build
build:
	docker build -t broker .

.PHONY: stoprm
stoprm:
	-docker stop broker
	-docker rm broker

.PHONY: run
run: stoprm
	docker run -d -p 1883:1883 --hostname broker --name broker broker

.PHONY: dev
dev: stoprm
	docker run -it --rm -p 1883:1883 --hostname broker --name broker broker /bin/bash

.PHONY: clean
clean: stoprm
	-docker rmi broker

