import os

def get_nmap(options, ip):
    command = "nmap "+options+" "+ip
    