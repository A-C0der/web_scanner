from urllib.request import urlopen
from urllib.parse import urlparse
import socket
import whois
def info(url):
    response = urlopen(url)
    parsed_url = urlparse(url)
    ip_address = socket.gethostbyname(parsed_url.netloc)
    print(f"Target Site\t\t\t{url}")
    print(f"IP Address\t\t\t{ip_address}")

    ##whois
    w = whois.query(url)
    print(f'Email:\t\t\t\t{w.emails}')
    print(f'Name Server:\t\t\t{w.name_servers}')
    print(f'Creation date:\t\t\t{w.creation_date}')
    print(f'Expiration_date:\t\t{w.expiration_date}')

