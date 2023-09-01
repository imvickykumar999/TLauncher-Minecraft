
# https://pypi.org/project/anvil-parser/
import anvil

region = anvil.EmptyRegion(0, 0)
side = 15
tall = 100

wall = anvil.Block('minecraft', 'diamond_block')
floor = anvil.Block('minecraft', 'gold_block')

# use black_stained_glass as floor to avoid mob spawn
# floor = anvil.Block('minecraft', 'black_stained_glass')

for x in range(side): # walls
    for y in range(-63, tall-2):
        for z in range(side):
            if(x == 0 or x == side - 1 or z == 0 or z == side - 1):
                region.set_block(wall, x, y, z)

for x in range(side): # floor
    for y in range(-63, tall, 5):
        for z in range(side):
            if y == -63 or not (x == 1 and z == 1):
                region.set_block(floor, x, y, z)
                
region.save('region/r.0.0.mca')
print('Build Complete.')
