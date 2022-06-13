import os

from jinja2 import Environment, FileSystemLoader

# environment setup
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('1.html')  # place the file in template folder

persons = [
    {'name': 'Andrej', 'age': 34},
    {'name': 'Mark', 'age': 17},
    {'name': 'Thomas', 'age': 44},
    {'name': 'Lucy', 'age': 14},
    {'name': 'Robert', 'age': 23},
    {'name': 'Dragomir', 'age': 54}
]

output = template.render(persons=persons)
print(output)
url = 'output.html'
with open('output.html', 'w') as fp:
    fp.write(output)

os.startfile(url)
