import numpy as np
import struct
import bz2
import h5py
import os
import ArithEncode
#import torch
import arcode
import bitfile
class bitstream(object):
    """docstring for ."""
    def __init__(self, dat):
        super(bitstream, self).__init__()
        self.dat = dat
        self.h = None
        self.w = None
        self.c = None
        self.model = None

class entropy_codec(object):
    """docstring for ."""
    def __init__(self, Mode='BPAQ',action='r'):
        super(entropy_codec, self).__init__()
        self.Mode = Mode

    def bpaq(self,dat,filename):
        dat_b = np.reshape(dat.dat, (-1,1))

        #Image Info
        bfile = open(filename+'dat','wb')
        bytes = struct.pack('3i',dat.h,dat.w,dat.c)
        bfile.write(bytes)
        for i in dat_b:
            #for j in range(6)
            #print i[0]
            #bitmap.append(i[0] - (i[0] >> 1) << 1)
            #print i[0] - (i[0] >> 1) << 1
            bytes = struct.pack('b',int(i))
            bfile.write(bytes)

        bfile.close()

        datfile = '"'+filename+'dat" '
        paqfile = '"'+filename+'bpaq" '

        os.system(" /home/lhj/JPEGXL/zpaq/zpaq a "+paqfile+datfile+"-method 5")
        #os.system("rm "+datfile)
    def arith(self,dat,filename):
        dat_b = np.reshape(dat.dat, (-1,1))

        #Image Info
        bfile = open(filename+'dat','wb')
        bytes = struct.pack('3i',dat.h,dat.w,dat.c)
        bfile.write(bytes)
        for i in dat_b:
            #for j in range(6)
            #print i[0]
            #bitmap.append(i[0] - (i[0] >> 1) << 1)
            #print i[0] - (i[0] >> 1) << 1
            bytes = struct.pack('b',int(i))
            bfile.write(bytes)

        bfile.close()

        datfile = filename+'dat'
        arithfile = filename+'arith'

        ar = arcode.ArithmeticCode(False)
        #ar = arcode.ArithmeticCode(True)
        ar.encode_file(datfile,arithfile)


    def encode(self,dat,filename):
        if self.Mode is 'BPAQ':
            self.bpaq(dat,filename)
        if self.Mode is 'Arith':
            self.arith(dat,filename)
        if self.Mode is 'BZ2':
            self.bz2(dat,filename)

    def decode(self):
        pass

