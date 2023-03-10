import nmap
import nmap3
from urllib.request import urlopen
from urllib.parse import urlparse
def subdomain(url):
    response = urlopen(url)
    parsed_url = urlparse(url)
    nmap = nmap3.Nmap()
    results = nmap.nmap_dns_brute_script(parsed_url.netloc)
    for i in results:
        for b in i:
            print(b,':\t\t\t',i[b])