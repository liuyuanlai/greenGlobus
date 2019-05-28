#!/bin/bash

for f in $(seq 1.2 0.1 3.0)
do
	echo $f >> result_cc48_10t_05_28_v2
	cpupower frequency-set -f ${f}Ghz
	ssh -f uc2 "cpupower frequency-set -f ${f}Ghz"
	sleep 5
	for i in $(seq 10)
	do
		./a.out 1>> result_cc48_10t_05_28_v2
	done
done
