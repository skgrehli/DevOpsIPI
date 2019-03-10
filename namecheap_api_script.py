from namecheap import Api
from config import (NAMECHEAP_API_KEY, NAMECHEAP_USERNAME,
                    NAMECHEAP_IP_ADDRESS, NAMECHEAP_SANDBOX)


namecheap_api = Api(NAMECHEAP_USERNAME, NAMECHEAP_API_KEY,
                    NAMECHEAP_USERNAME, NAMECHEAP_IP_ADDRESS, sandbox=NAMECHEAP_SANDBOX)


def update_name_server(domain, name_servers):
    """Sets the domain to use the supplied set of nameservers.
    Example:
    update_name_server('example.com', 'ns1.example.com,ns2.example.com')"""

    response = namecheap_api.domains_dns_setCustom(
        domain, {'Nameservers': name_servers})
    print(response)


if __name__ == "__main__":
    """
            namecheap_api_script.py 'example.com' 'ns1.example.com,ns2.example.com'
    """
    domain = sys.argv[1]
    name_servers = sys.argv[2]
    update_name_server(domain, name_servers)
