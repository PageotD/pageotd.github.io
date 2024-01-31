import json
from jinja2 import Environment, FileSystemLoader

# # Load data from a JSON file
# data = {
#     "title": "About me",
#     "paragraphs": [
#         "With a master degree in Planetary Geosciences and a PhD in Geophysics, I had the opportunity to work on several topics and at different scales: lithosphere imaging, sea wall monitoring, concrete monitoring, seismic modeling at reduced scale.",
#         "After several years spent in research laboratories, I started a reconversion in the IT world by following a DevOps training. This allowed me to join Capgemini and to touch many technologies and methods: Jenkins, Docker, Kubernetes, BIG-IP F5, LDAP as Code..."
#     ]
# }

data = {}

with open("education.json", "r") as feduc:
    education = json.load(feduc)
    data.update({"education": education})

with open("experience.json", "r") as fexpe:
    experience = json.load(fexpe)
    data.update({"experience": experience})

# Set up Jinja environment
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('index.j2')

# Render the template with the data
#output = template.render(data)
output = template.render(data)

with open("../index.html", "w") as findex:
    findex.write(output)
# Print or save the rendered HTML
#print(output)
