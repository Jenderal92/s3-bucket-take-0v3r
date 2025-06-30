# s3-bucket-take-0v3r
S3 Bucket Takeover Scanner &amp; Claim Tool


## 📌 Description

**S3 Bucket Takeover Scanner & Claim Tool** is a Python 2.7-based utility that:

1. **Scans domain names to identify potential Amazon S3 bucket takeover vulnerabilities.**
2. **Automatically claims unregistered S3 buckets and uploads a test HTML page.**

This tool is ideal for bug bounty hunting, cloud asset auditing, or legal penetration testing within authorized environments.

## ⚙️ Features

- ✅ Scan multiple domains to identify vulnerable S3 bucket links
- ✅ Extract and resolve domain CNAME records
- ✅ Automatically detect AWS region from CNAME
- ✅ Identify takeover vulnerabilities via `The specified bucket does not exist` response
- ✅ Automatically create (claim) the bucket if vulnerable
- ✅ Upload an `index.html` file to the bucket and enable static hosting
- ✅ Log vulnerable domains into `vulnerable_buckets.txt`
- ✅ Supports multi-threading for faster scanning
- ✅ Color-coded console output and banner for clarity


## 🧠 Tool Function Overview

| Function | Purpose |
|---------|---------|
| `run_scan()` | Checks if the target domain points to a non-existent S3 bucket |
| `lookup_cname()` | Resolves CNAME to identify AWS-hosted targets |
| `extract_region_from_cname()` | Extracts AWS region info for bucket creation |
| `takeover_bucket()` | Automatically creates & configures a claimed bucket |
| `scan_domain()` | Attempts HTTPS and HTTP scanning |
| `main()` | Reads domain list and starts threaded scanning |


## 🚀 How to Use

### 1. Requirements
- Python 2.7
- `boto3`, `requests` libraries
- `dig` (Linux-based DNS utility)
- A file named `domains.txt` containing a list of target domains:


example1.com
example2.com



### 2. Run the Tool

```bash
python2 script.py domains.txt

```

### 3. Output

* Results will be printed in the terminal
* Vulnerable domains will be saved to `vulnerable_buckets.txt`
* Claimed buckets will be created and hosted with an index page

---

## ⚠️ Legal Disclaimer

🟥 **IMPORTANT: This tool must only be used for:**

* Testing your **own AWS S3 resources**
* **Authorized** bug bounty programs
* **Written permission** from the domain or asset owner

Unauthorized use of this tool for exploitation or data manipulation is **illegal** and may result in **criminal prosecution** under international cybersecurity laws.

---
 
**Another Disclaimer:**  

I have written the disclaimer on the cover of Jenderal92. You can check it [HERE !!!](https://github.com/Jenderal92/)

