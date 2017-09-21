#!/usr/bin/env python2.7
import os
import optparse
import sys
import subprocess
import signal
import time
import matplotlib
matplotlib.use("Pdf")
import numpy as np
import matplotlib.pyplot as plt


def read_log():
	gpu = []
	memory = []
	r1=0
	r2=0
	i=0
	
	while i<20:
		time.sleep(0.1)
		p=os.popen('nvidia-smi -i 1 --query-gpu=utilization.gpu --format=csv,noheader','r')
		line=p.readlines()[0]
		r1=int(line.split('%')[0])
		gpu.append(r1)
			
		q=os.popen('nvidia-smi -i 1 --query-gpu=utilization.memory --format=csv,noheader','r')
		line=q.readlines()[0]
		r2=int(line.split('%')[0])
		memory.append(r2)
		i=i+1
	return gpu,memory
def main():

	#runtimes,received,dropped,time = read_log("temp")

	print read_log() 



if __name__ == "__main__" :
	main()
