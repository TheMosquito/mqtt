
.PHONY: all
all:
	make broker
	sleep 5
	make pub &
	make sub &

.PHONY: broker
broker:
	make -C broker

.PHONY: pub
pub:
	make -C pub

.PHONY: sub
sub:
	make -C sub

.PHONY: stoprm
stoprm:
	make -C sub stoprm
	make -C pub stoprm
	make -C broker stoprm

.PHONY: clean
clean:
	make -C sub clean
	make -C pub clean
	make -C broker clean

