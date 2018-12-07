import json
from country_codes import get_country_code
from pygal.maps.world import World
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

#filename = r'matplot-demo\worldmap\population_data.json'
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# 创建一个包含人口数量的字典
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country)
        if code:
            cc_populations[code] = population

# 根据人口数量将所有的国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop > 1000000000:
        cc_pops_1[cc] = pop
    elif pop > 10000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

#wm_style = RotateStyle('#336699')
#wm = World(style=wm_style)

wm_style = RS('#336699', base_style=LCS)
wm = World()
wm.title = 'World Population in 2010, by Country'
wm.add('>1bn', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('0-10m', cc_pops_3)
wm.render_to_file('world_population.svg')