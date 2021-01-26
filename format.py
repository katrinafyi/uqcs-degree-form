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

def format_data(data):
    out = {}
    for prog in sorted(data, key=lambda x: x['name']):
        name = get_program_name(prog)
        out[name] = prog['majors']
    return out

with open('ugpg.json') as f:
    ug = json.load(f)
with open('pgpg.json') as f:
    pg = json.load(f)

ug2 = format_data(ug)
pg2 = format_data(pg)

ug = [(get_program_name(x)) for x in ug]
ug = list(sorted(set(ug)))
pg = [(get_program_name(x)) for x in pg]
pg = list(sorted(set(pg)))

with open('programs.json', 'w') as f:
    json.dump({'undergrad': ug, 'postgrad': pg}, f, indent=2)

with open('programs_with_majors.json', 'w') as f:
    json.dump({'undergrad': ug2, 'postgrad': pg2}, f, indent=2)
