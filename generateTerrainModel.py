import sys
from panda3d.core import GeoMipTerrain
from pandac.PandaModules import TextureStage, Texture
import direct.directbase.DirectStart

if True:

	heightfieldIndex = 2

	#zScale = sys.argv[1]
	zScale = 60

	#heightfieldFile = sys.argv[heightfieldIndex]
	heightfieldFile = "a.png"

	terrain = GeoMipTerrain("hey")
	
	terrain.setHeightfield("bin/terrain.png")
	terrain.setColorMap("bin/terrain_texure.png")  
	#terrain.setColorMap("colourmap.jpg")
	#terrain.setBlockSize(512)
	#terrain.setBruteforce(True)

	
	terrain.generate()

	root = terrain.getRoot()
	root.setSz(5) 

	print root.getBounds()

	for i in range(0, 128):

		print terrain.getElevation(128, i+1)
	

	#textures1 = ["default_c.png", "maps/default_d.png", "maps/default_l.png", 
	#			"textures/bigRockFace.png", "textures/hardDirt.png", "textures/grayRock.png", "textures/shortGrass.png"]

	textures = ["hardDirt.png"]

	#for i in range(heightfieldIndex + 1, len(sys.argv)-1):
	i = 0
	for texture in textures:

		#texture = loader.loadTexture(sys.argv[i])

		print texture
		texture = loader.loadTexture(texture)
		texture.setMinfilter(Texture.FTLinearMipmapLinear)


		terrain.getRoot().setTexture(TextureStage('tex' + str(i)), texture)

		i+=1

	terrain.getRoot().setShader(loader.loadShader('terraintexture.sha'))

	#outputFile = sys.argv[-1]
	outputFile = "test.bam"

	root.writeBamFile(outputFile)
		
#except Exception:

#	print "Error generating .egg model"
#	print Exception