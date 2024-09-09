import requests
from requests.auth import HTTPBasicAuth

def main():

    url = 'https://georgetowntx.atlassian.net/wiki/rest/api/template/page'
    username = 'chase.kluge@georgetown.org'
    with open('C:/Projects/confluence-automation/temp/atlassian-secret.secret', 'r') as file:
        secret = file.read()
    space_key = 'UA'

    response = requests.get(
        url,
        params={'spaceKey': space_key},
        auth=HTTPBasicAuth(username, secret)
    )

    if response.status_code == 200:
        templates = response.json()
    #     for template in templates['results']:
    #         print(f"Template Name: {template['name']}, Template Key: {template['templateId']}")
    # else:
    #     print(f"Failed to retrieve templates: {response.status_code} - {response.text}")

    for t in templates['results']:
        if t['name'] == 'Utility Support Sync-up Template':
            return(t['templateId'])


if __name__ == '__main__':
    main()