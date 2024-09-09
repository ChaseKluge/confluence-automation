# Confluence Automation for Water Utility Support
Automatically create new confluence pages using templates.
2024; Georgetown Water Analytics

## Overview
This little python program uses the Atlassian Python library to collect template data and create a new confluence page with a dynamic name. Currently, designed to be run every Monday to create a new weekly sync-up agenda.


## Use
Adds a new weekly sync agenda with a dynamically generated date in the title (the next Monday from runtime). Uses the template that is defined in the `get_template.py` script.
### Setup
1. Download the program
2. Register for a key from Atlassian using your user account.
3. Add an `atlassian-secret.secret` file to the `temp` directory
### Basic Use
Intended for use with Microsoft Task Scheduler. Comes with an included PowerShell wrapper in the `scripts` directory for this purpose.
### Testing
No formal testing tools included, just run it and see what happens in Confluence!!!
