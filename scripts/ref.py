import json

with open("references.json", "r") as fref:
    references = json.load(fref)

articles = []
proceedings = []

years = []
for ref in references:
    years.append(ref['year'])
set_years = sorted(set(years), reverse=True)
print(set_years)

final = {}
for year in set_years:
    final.update({year: []})

print(final)
for ref in references:
    if ref['category'] == "Article":
        #print(f"{ref['author']} ({ref['year']}). {ref['title']}. {ref['journal']}, {ref['volume']}, {ref['pages']}. {ref['doi']}\n")
        articles.append(f"""{ref['author']} ({ref['year']}). {ref['title']}. <em>{ref['journal']}</em>, {ref['volume']}, {ref['pages']}. <link href="https://doi.org/{ref['doi']}" rel="{ref['doi']}"/>""")
        final[ref['year']].append(f"""{ref['author']} ({ref['year']}). {ref['title']}. <em>{ref['journal']}</em>, {ref['volume']}, {ref['pages']}. <link href="https://doi.org/{ref['doi']}" rel="{ref['doi']}"/>""")
    elif ref['category'] == "InProceedings":
        #print(f"{ref['author']} ({ref['year']}). {ref['title']}. {ref['meeting']}.\n")
        proceedings.append(f"""{ref['author']} ({ref['year']}). {ref['title']}. <em>{ref['meeting']}</em>.""")
        final[ref['year']].append(f"""{ref['author']} ({ref['year']}). {ref['title']}. <em>{ref['meeting']}</em>.""")
print(final)