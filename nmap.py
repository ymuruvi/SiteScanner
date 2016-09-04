import os

def get_nmap(options, ip):
    print("Getting NMAP")
    command = "nmap "+ options + " " + ip
    process = os.popen(command)
    results = str(process.read())
    return results
