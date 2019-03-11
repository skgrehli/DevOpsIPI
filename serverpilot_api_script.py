import requests
from config import (SERVERPILOT_CLIENTID, SERVERPILOT_APIKEY)


def load_wordpress(domains, wordpress_data):
    # {"name": "wordpress", "sysuserid": "RvnwAIfuENyjUVnl", "runtime": "php7.0", "domains": ["example.com", "www.example.com"], "wordpress": {"site_title": "My WordPress Site", "admin_user": "admin", "admin_password": "mypassword", "admin_email": "example@example.com"}
    request_data = {
        "name": "wordpress",
        "sysuserid": "RvnwAIfuENyjUVnl",
        "runtime": "php7.0",
        "domains": domains,
        "wordpress": wordpress_data
    }
    response = requests.post(url='', data=request_data)
    print(response.json)


if __name__ == "__main__":
    """
            serverpilot_api_script.py 'example.com' {"site_title": "My WordPress Site", "admin_user": "admin", "admin_password": "mypassword", "admin_email": "example@example.com"}
    """
    domain = sys.argv[1]
    wordpress_data = sys.argv[2]
    load_wordpress(domain, wordpress_data)
