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


def read_log(filename):
	tp = []
	i = 0
	with open(filename) as f:
		for line in f:
			i+=1
			tp.append(float(line)/1000000)
			if i==50 :
				break
	return tp 
def read_data():
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
def draw(l1, l2):

	lines = [l1,l2]
	
	plt.style.use('ggplot')#seaborn-white')
	plt.style.use('ggplot')#seaborn-white')
	fig,ax1 = plt.subplots()

	fig = plt.figure(1)
	length=len(l1)
	timeline = np.linspace(1,150,length)
	colors = ['r','b','y','m','c','g','r','b','y']
	styles = ['-.', '--', ':', '-', 'D:', 'p:', 'x:','*:']
	linelabels = ["with \nLive Update", "without \nLive Update", "dynamic","HP,FW","FM,FW","FM,HP,FW"]
	ax1.plot(timeline, l1,  'r-.', label=linelabels[0], linewidth=3)
	ax1.plot(timeline, l2,  'b--', label=linelabels[1], linewidth=3)
	
	ax1.set_ylabel('Throughput(Mpps)', fontsize=25, style='normal', color='black')
	ax1.set_xlabel('Time (s)', fontsize=25, style="normal", color='black')

	# Now add the legend with some customizations.
	legend = ax1.legend(loc='lower left', shadow=False)
	

	# Set the fontsize
	for label in legend.get_texts():
		label.set_fontsize(17)

	for label in legend.get_lines():
		label.set_linewidth(3)  # the legend line width

	for tl in ax1.get_xticklabels():
		tl.set_fontsize(20)
		tl.set_fontstyle('normal')
	for tl in ax1.get_yticklabels():
		tl.set_fontsize(20)
		tl.set_fontstyle('normal')
	
	plt.gcf().subplots_adjust(bottom=0.18)
	plt.gcf().subplots_adjust(left=0.15)

	fig.savefig('Dynamic.pdf')
	plt.show()
	

	return lines

def main():

	#tp1 = read_log("data_1")
	#tp2 = read_log("data_2")
	tp1,tp2=read_data()

	draw(tp1,tp2) 



if __name__ == "__main__" :
	main()
