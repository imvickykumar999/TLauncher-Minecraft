
import anvil
import pandas as pd

region = anvil.EmptyRegion(0, 0)
chunk = 1

tall = 120
radius = 16*chunk -1

df = pd.read_csv('minecraftDot.csv', 
                   header=None, 
                   index_col=False)

for x in range(1, len(df.columns)):
	for z in range(1, len(df.columns)):
		block = df.iloc[x, z]
		block = block.split(':')

		pixel = anvil.Block('minecraft', block[1])
		region.set_block(pixel, x-1, 100, z-1)
		print(x-1, z-1, block[1])

region.save('region/r.0.0.mca')
print('\nBuild Complete.')
