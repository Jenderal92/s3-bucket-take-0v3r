import json
import re
import os
import sys
import subprocess
import requests
import threading

def banner():
    print """

   AWS S3 Takeover Scanner  - Educational Use Only
         By: Shin Code | For legal testing only!
"""
banner()

def run_scan(url, domain):
    print("[*] Scanning {}...".format(url))
    try:
        response = requests.get(url, timeout=4, verify=False)
    except requests.exceptions.RequestException:
        print("[-] Unable to connect to: {}".format(url))
        return ""
    
    if response.status_code == 404 and "The specified bucket does not exist" in response.text:
        cnames = lookup_cname(domain)
        region = extract_region_from_cname(cnames[0]) if cnames else "Unknown"
        save_vulnerable_bucket(domain, region)
        return domain
    return ""

def lookup_cname(domain):
    try:
        with open(os.devnull, 'w') as devnull:
            process = subprocess.Popen(["dig", "+short", domain, "CNAME"], stdout=subprocess.PIPE, stderr=devnull)
            output, _ = process.communicate()
        
        result = output.decode("utf-8") if isinstance(output, bytes) else output
        cnames = result.strip().split("\n")
        return [cname.strip(".") for cname in cnames if cname]  
    except Exception as e:
        print("\033[94m[-] Failed to lookup CNAME record: {}\033[0m".format(e))  # Warna biru
        return []

def extract_region_from_cname(cname):
    print("\033[92mCNAME: {}\033[0m".format(cname))
    
    match = re.search(r'(?:eu|ap|us|ca|sa)-(?:north|south|west|east|central|northeast|southeast)?-\d+', cname)
    
    if match:
        region = match.group(0)
        print("[+] Found Region: {}".format(region))
        return region
    
    print("[*] Defaulting to us-east-1")
    return "us-east-1"



def save_vulnerable_bucket(domain, region):
    with open("vulnerable_buckets.txt", "a") as file:
        file.write("{} | {}\n".format(domain, region))
    print("[+] Saved vulnerable bucket: {} | {}".format(domain, region))


def scan_domain(domain):
    bucket = run_scan("https://{}".format(domain), domain)
    if not bucket:
        print("[*] Failed to connect over HTTPS, trying HTTP...")
        bucket = run_scan("http://{}".format(domain), domain)
    
    if bucket:
        print("[+] Bucket is vulnerable!")
    else:
        print("\033[91m[-] Bucket does not appear to be vulnerable\033[0m")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <file_with_domains>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    try:
        with open(file_path, "r") as f:
            domains = [line.strip() for line in f.readlines() if line.strip()]
    except Exception as e:
        print("[-] Error reading file: {}".format(e))
        sys.exit(1)
    
    threads = []
    for domain in domains:
        thread = threading.Thread(target=scan_domain, args=(domain,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()

