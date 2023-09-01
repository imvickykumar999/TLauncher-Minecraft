
# https://pypi.org/project/anvil-parser/
import anvil

region = anvil.EmptyRegion(0, 0)
chunk = 1

side = 16*chunk -1
tall = 120

wall = anvil.Block('minecraft', 'blue_stained_glass')
# wall = anvil.Block('minecraft', 'diamond_block')

floor = anvil.Block('minecraft', 'glowstone')
# floor = anvil.Block('minecraft', 'gold_block')

for x in range(side): # walls
    for y in range(-63, tall-1):
        for z in range(side):
            if(x == 0 or x == side - 1 or z == 0 or z == side - 1):
                region.set_block(wall, x, y, z)

for x in range(side): # floor
    for y in range(-63, tall, 5):
        for z in range(side):
            if y == -63 or not (x == 1 and z == 1):
                region.set_block(floor, x, y, z)
                
region.save('region/r.0.0.mca')
print('\nBuild Complete.')
