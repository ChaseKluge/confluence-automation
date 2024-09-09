from atlassian import Confluence
import get_monday
import get_template

def main():
    with open('C:/Projects/confluence-automation/temp/atlassian-secret.secret', 'r') as file:
        secret = file.read()

    confluence = Confluence(
        url='https://georgetowntx.atlassian.net',
        username='chase.kluge@georgetown.org',
        password=secret
    )

    date = str(get_monday.main())

    space_key = 'UA'
    parent_page_id = '2146074631'
    title = f"{date} Utility Support Weekly Sync"
    template_key = get_template.main()

    template_content = confluence.get_content_template(template_key)['body']['storage']['value']

    result = confluence.create_page(
        space=space_key,
        title=title,
        parent_id=parent_page_id,
        body=template_content
    )

    print(f"Page created successfully: {result}")

if __name__ == '__main__':
    main()