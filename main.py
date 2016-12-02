#!/usr/bin/python

from domain_name import *
from general import *
from ip_address import *
from nmap import *
from robots_txt import *
from whois import *
import sys

ROOT_DIR = 'companies'
create_dir(ROOT_DIR)

def gather_info(name, url):
    try:
        domain_name = get_domain_name(url)
        ip_address = get_ip_address(domain_name)
        print(ip_address)
        nmap = get_nmap('-F', ip_address)
        robots_txt = get_robots_txt(url)
        whois = get_whois(url)
        create_report(name, url, domain_name, ip_address, nmap, robots_txt, whois)
    except:
        print("Unexpected Error: \"", sys.exc_info()[0],"\"")


def create_report(name, full_url, domain_name, ip_address, nmap, robots_txt, whois):
    print ("Creating Report")
    project_dir = ROOT_DIR + '/' + name
    create_dir(project_dir)
    write_file(project_dir + "/full_url.txt", full_url)
    write_file(project_dir + "/domain_name.txt", domain_name)
    write_file(project_dir + "/nmap.txt", nmap)
    write_file(project_dir + "/robots_txt.txt", robots_txt)
    write_file(project_dir + "/whois.txt", whois)


def scan_sites_in_file(file_path):
    print ("Scanning Sites In: \"" + file_path +"\"\n\n")
    data = read_file(file_path)
    for company in data:
        info = company[0]
        name = info[:company[1] - 1]
        url = info[company[1]:len(company[0])].rstrip("\n")
        gather_info(name, url)
        print("\n\n")
    print("\nComplete")

def get_site():
    site = input("Please enter the file path for the file containing the list of files to scan.")
    try:
        scan_sites_in_file(site)
    except:
        try:
            scan_sites_in_file("companies_to_scan.txt")
        except:
            print("No file was found for scanning the files.")

get_site()
