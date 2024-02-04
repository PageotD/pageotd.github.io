import json
from jinja2 import Environment, FileSystemLoader

def  add_data(filename: str)->dict:
    with open(filename, "r") as fjson:
        content = json.load(fjson)
    return {filename.removesuffix(".json") : content}

data = {}
data.update(add_data("social.json"))
data.update(add_data("education.json"))
data.update(add_data("experience.json"))
data.update(add_data("references.json"))
data.update(add_data("interests.json"))
data.update(add_data("certifications.json"))
data.update(add_data("skills.json"))

# Set up Jinja environment
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('index.j2')

# Render the template with the data
output = template.render(data)

with open("../index.html", "w") as findex:
    findex.write(output)
