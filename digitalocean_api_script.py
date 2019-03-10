from digitalocean_domain import Domain
from config import DIGITALOCEAN_TOKEN


def update_cname_aname(domain, param):
    domain_obj = Domain(token=DIGITALOCEAN_TOKEN, domain=domain)
    response = domain_obj.update_domain_record(param)
    print(response)


if __name__ == "__main__":
    """
        digitalocean_api_script.py 'example.com' 'A' 'www' '192.0.0.0'
            Args:
                type: The record type (A, MX, CNAME, etc).
                name: The host name, alias, or service being defined by the record
                data: Variable data depending on record type.
    """
    domain = sys.argv[1]
    name_servers =
    param = {
        'type': sys.argv[2],
        'name': sys.argv[3],
        'data': sys.argv[4],
    }
    update_cname_aname(domain, param)
