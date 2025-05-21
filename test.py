import pandas as pd
from urllib.parse import urlparse

data = pd.read_csv("malicious_phish.csv")
data["url"].duplicated().sum()

def add_protocol(url):
    if not url.startswith(('http://', 'https://')):
        return 'http://' + url
    return url

def extract_domain_length(url):
    print(url)
    parsed_url = urlparse(url)
    return len(parsed_url.netloc)

def extract_domain_num(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc.count('.')

data["url"] = data["url"].apply(add_protocol)
data["domain_length"] = data["url"].apply(extract_domain_length)
# data["domain_num"] = data["url"].apply(extract_domain_num)


data.head()