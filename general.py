import os

def create_dir(directory):
    #makes sure the directory doesn't exist already
    if not os.path.exists(directory):
        os.makedirs(directory)

def write_file(path, data):
    f = open(path,'w')
    f.write(data)
    f.close()