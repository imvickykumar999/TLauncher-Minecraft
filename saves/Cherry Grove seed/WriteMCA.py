
import anvil
import math

region = anvil.EmptyRegion(0, 0)
chunk = 1

tall = 120
radius = 16*chunk -1

def printPattern(radius=4, y=0):
	xyz = []

	for x in range((2 * radius)+1):
		for z in range((2 * radius)+1):
			
			dist = math.sqrt((x - radius) * (x - radius) +
				(z - radius) * (z - radius))

			if (dist > radius - 0.5 and dist < radius + 0.5):
				# print("*",end=" ")
				xyz.append((x-radius, y ,z-radius))
			else:
				# print(" ",end=" ")	
				pass
	
		# print()
	return xyz

# wall = anvil.Block('minecraft', 'gold_block')
wall = anvil.Block('minecraft', 'glowstone')

floor = anvil.Block('minecraft', 'diamond_block')
# floor = anvil.Block('minecraft', 'blue_stained_glass')

for x in range(2*radius): # floor
    for y in range(-63, tall, 5):
        for z in range(2*radius):
            if y == -63 or not (x == 1 and z == 1):
                region.set_block(floor, x, y, z)
                
for i in range(-63, tall-1): # wall
	for x,y,z in printPattern(radius, i):
		region.set_block(wall, x+radius, y, z+radius)

region.save('region/r.0.0.mca')
print('\nBuild Complete.')
