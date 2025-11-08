from os import getenv

import requests, os
from requests.auth import HTTPBasicAuth

jenkins_url = "https://jenkins.procopan.md/job/python/build"
auth = HTTPBasicAuth("admin", os.getenv("jenkins-token"))

res = requests.post(jenkins_url, auth=auth)
print("Triggered:", res.status_code)
