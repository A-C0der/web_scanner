import ssl
import socket
from urllib.request import urlopen
from urllib.parse import urlparse
def ssld(url):
    response = urlopen(url)
    parsed_url = urlparse(url)
    port = 443

    context = ssl.create_default_context()
    with socket.create_connection((parsed_url.netloc, port)) as sock:
        with context.wrap_socket(sock, server_hostname=parsed_url.netloc) as ssock:
            cert = ssock.getpeercert()

    print("\n\t\t\t#### SSL INFO ####")
    for info in cert:
        print(info,':\t\t\t',cert[info])