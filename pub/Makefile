
.PHONY: all
all:
	make build
	make run

.PHONY: build
build:
	docker build -t pub .

.PHONY: stoprm
stoprm:
	-docker stop pub
	-docker rm pub

.PHONY: run
# Leaving the terminal output on for the publisher so you can see it working
run: stoprm
	docker run -t --link broker:broker --name pub pub

.PHONY: dev
dev: stoprm
	docker run -it --rm --link broker:broker --name pub pub /bin/bash

.PHONY: clean
clean: stoprm
	-docker rmi pub

