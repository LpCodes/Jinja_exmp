import datetime
import os
import sys
import platform
import sysconfig

import requests
from jinja2 import Environment, FileSystemLoader

# environment setup
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('2.html')  # place the file in template folder

dt = datetime.datetime.now().strftime("%H:%M:%S")

response = requests.get("https://dog.ceo/api/breeds/image/random")  # gets random dog image
pinop = response.json()
print(pinop, type(pinop))
print(pinop["message"])

print("os.name                     ", os.name)
print("sys.platform                ", sys.platform)
print("platform.system()           ", platform.system())
print("sysconfig.get_platform()    ", sysconfig.get_platform())
print("platform.machine()          ", platform.machine())
print("platform.architecture()     ", platform.architecture())

osinfo = [os.name, sys.platform, platform.architecture(), platform.machine(), platform.system()]

output = template.render(name_for_html=dt, pinop=pinop, osinfo=osinfo)
# print(output)

url = 'output.html'
with open('output.html', 'w') as fp:
    fp.write(output)

os.startfile(url)
