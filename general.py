#!/usr/bin/python

import os
import io
import shutil


def create_dir(directory):
    #makes sure the directory doesn't exist already
    if not os.path.exists(directory):
        os.makedirs(directory)

def write_file(path, data):
    f = open(path,'w')
    f.write(data)
    f.close()

###Returns an array with a list of all the companies to scan
def read_file(path):
    f = open(path,'r')
    out = []
    lines = 0
    for line in f:
        url_marker = line.find("http")
        out.append([(line),url_marker])
        #print(lines+1, ": " + str(out[lines]))
        lines += 1
    f.close
    #print(out)
    return out

def remove_dir(folder):
    shutil.rmtree(folder)

#read_file("companiestoscan.txt")
