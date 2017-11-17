
.PHONY: all
all:
	make build
	make run

.PHONY: build
build:
	docker build -t sub .

.PHONY: stoprm
stoprm:
	-docker stop sub
	-docker rm sub


.PHONY: run
# Leaving the terminal output on for the subscriber so you can see it working
run: stoprm
	docker run -t --link broker:broker --name sub sub

.PHONY: dev
dev: stoprm
	docker run -it --rm --link broker:broker --name sub sub /bin/bash

.PHONY: clean
clean: stoprm
	-docker rmi sub

