import os
import io

def create_dir(directory):
    #makes sure the directory doesn't exist already
    if not os.path.exists(directory):
        os.makedirs(directory)

def write_file(path, data):
    f = open(path,'w')
    f.write(data)
    f.close()

def read_file(path):
    f = open(path,'r')
    out = []
    lines = 0
    for line in f:
        lines+=1
        out.append(line)
        print(lines+ ": " +out[lines])
    f.close
    print(out)
    return out

read_file("companiestoscan.txt")