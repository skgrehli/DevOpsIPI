import os

# Set NAMECHEAP Variable
NAMECHEAP_API_KEY = os.environ.get('NAMECHEAP_API_KEY', 'api_key')
NAMECHEAP_USERNAME = os.environ.get('NAMECHEAP_USERNAME', 'username')
NAMECHEAP_IP_ADDRESS = os.environ.get('NAMECHEAP_IP_ADDRESS', 'ip_address')
NAMECHEAP_SANDBOX = os.environ.get('NAMECHEAP_SANDBOX', True)


# Set DIGITALOCEAN Variable
DIGITALOCEAN_TOKEN = os.environ.get('DIGITALOCEAN_TOKEN', 'token')


# Set SERVERPILOT Variable
SERVERPILOT_CLIENTID = os.environ.get('SERVERPILOT_CLIENTID', 'clientid')
SERVERPILOT_APIKEY = os.environ.get('SERVERPILOT_APIKEY', 'apikey')