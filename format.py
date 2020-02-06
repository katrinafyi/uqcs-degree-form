import json 

def get_program_name(program):
    name = program['name']
    name = name.replace(' - St Lucia', '')
    name = name.replace(' - Gatton', '')
    type = program['type']
    type = type.replace(' (Dual Degree)', 's')
    type = type.replace(' Honours', '')
    type = type.replace(' (Extended)', '')

    if 'units)' in name:
        name = name.split(' (')[0]
    return f'{type} of {name}'

with open('ugpg.json') as f:
    ug = json.load(f)
with open('pgpg.json') as f:
    pg = json.load(f)

ug = [(get_program_name(x)) for x in ug]
ug = list(sorted(set(ug)))
pg = [(get_program_name(x)) for x in pg]
pg = list(sorted(set(pg)))

with open('programs.json', 'w') as f:
    json.dump({'ug': ug, 'pg': pg}, f)