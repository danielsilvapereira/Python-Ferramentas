import sys

from zabbix_api import ZabbixAPI
from github import Github

# Connect to Zabbix
zabbix_server = "http://zabbix.example.com"
zabbix_username = "user"
zabbix_password = "password"

zapi = ZabbixAPI(url=zabbix_server, user=zabbix_username, password=zabbix_password)

# Login to GitHub
github_username = "user"
github_password = "password"

g = Github(github_username, github_password)

# Get list of groups from Zabbix
groups = zapi.hostgroup.get({
    "output": "extend",
    "sortfield": "name"
})

# For each group, get the associated templates
for group in groups:
    templates = zapi.template.get({
        "output": "extend",
        "sortfield": "name",
        "groupids": group["groupid"]
    })

    # For each template, export the template and upload to GitHub
    for template in templates:
        # Export the template
        export_result = zapi.configuration.export({
            "format": "xml",
            "options": {
                "templates": [template["templateid"]]
            }
        })

        template_xml = export_result["result"]

        # Save the template to a file
        with open(f"{template['name']}.xml", "w") as f:
            f.write(template_xml)

        # Upload the file to GitHub
        repo = g.get_repo("user/repo")
        repo.create_file(f"{group['name']}/{template['name']}.xml", "Upload template", template_xml)

print("Templates exportados e enviados com sucesso para o GitHub!")
