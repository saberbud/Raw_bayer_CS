
# -*- coding: utf-8 -*-


import numpy as np
import struct


class Encoder:
	def __init__(self):
		self.low=0
		self.high=0xffffffff
		self.byte_list=[]

	def end(self,strs):
		for _ in range(4):
			self.byte_list.append((self.low>>24)&0xff)
			self.low=self.low<<8
		#for i in self.byte_list:
		#	print(i)

		fn='/home/lhj/JPEGXL/'+strs+'.txt'
		print(fn)
		f=open('/home/lhj/JPEGXL/'+strs+'.txt','w')
		for i in self.byte_list:
			i = bin(i)
			f.write(str(i))
			f.write("\n")
		f.close()


	def end2binary(self,strs):
		for _ in range(4):
			self.byte_list.append((self.low >> 24) & 0xff)
			self.low = self.low << 8
		with open('/home/lhj/JPEGXL/'+strs+'.dat','w') as g:

			for x in self.byte_list:
				xHEx = struct.pack('B',x)

				g.write(xHEx)

	def get_list(self):
		return self.byte_list

	def encode(self,bit,prob):
		x=self.low+((int((self.high-self.low)*prob))>>12)

		if bit==1:
			self.high=x
		else:
			self.low=x+1

		while (self.low^self.high)<(1<<24):
			self.byte_list.append(self.low>>24)
			self.low=self.low<<8
			self.low=self.low&0xffffffff

			self.high=(self.high<<8)|0xff
			self.high=self.high&0xffffffff

def encode(encoder,bit,float_prob):
	int_prob=int(float_prob*4096)
	encoder.encode(bit,int_prob)

class Decoder:
	def __init__(self,comp):
		self.code=0
		self.low=0
		self.high=0xffffffff
		self.de_num=0
		self.read_pos=0

		self.byte_list=comp#[]

		self.rec_list=[]

		for _ in range(4):
			self.code=(self.code<<8)|self.byte_list[self.read_pos]
			self.read_pos+=1

	def get_list(self):
		return self.rec_list

	def decode(self,prob):
		bit=0
		x=self.low+((int((self.high-self.low)*prob))>>12)

		if self.code<=x:
			self.high=x
			bit=1
		else:
			self.low=x+1
			bit=0#shenglue

		while (self.low^self.high)<(1<<24):
                        #print(self.read_pos)
			self.code=(self.code<<8)|self.byte_list[self.read_pos]
			self.code=self.code&0xffffffff

			self.read_pos+=1
			self.low=self.low<<8
			self.low=self.low&0xffffffff

			self.high=(self.high<<8)|0xff
			self.high=self.high&0xffffffff
		self.rec_list.append(bit)
		return bit

def decode(decoder,float_prob):
	int_prob=int(float_prob*4096)
	bit=decoder.decode(int_prob)
	return bit


