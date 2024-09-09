import requests
from requests.auth import HTTPBasicAuth
from pathlib import Path

def main():
    program_root = Path(__file__).parents[1]

    secret = Path(program_root / 'temp' / 'atlassian-secret.secret').read_text()

    url = 'https://georgetowntx.atlassian.net/wiki/rest/api/template/page'
    
    username = 'chase.kluge@georgetown.org'
    
    space_key = 'UA'

    response = requests.get(
        url,
        params={'spaceKey': space_key},
        auth=HTTPBasicAuth(username, secret)
    )

    if response.status_code == 200:
        templates = response.json()
    
        for t in templates['results']:
            if t['name'] == 'Utility Support Sync-up Template':
                return(t['templateId'])

    else:
        print(f'Failed to retrieve template data: {response.status_code} - {response.text}')


if __name__ == '__main__':
    main()