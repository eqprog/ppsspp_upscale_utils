import posixpath as unixPath
import glob
from pathlib import Path
import shutil
import os
import sys
import time

############Drag and drop folders to generate texture.ini file and prep for upscaling###########
"""Guide (PPSSPP): 

* Use generate_folders.py to create directory tree for your game first.
*  * It is HIGHLY RECOMMENDED that you organize your files based on in-game locations.

* This script is intended to be run in the following directory: '[PSP GAME ID]/new/'
	Be sure there are two sub-directories in the /new/ directory: 'masters' and 'textures'
		Then create a symlink to these directories in your [PSP GAME ID] directory. 
		(Admin) Command Line in Windows: mklink /J Link Target
				Example mklink "[full path to [PSP GAME ID]/textures" "[full path to [PSP GAME ID]/new/textures" ]
	Do the same thing making an '/ignore/' directory to make the emulator ignore files you don't want to upscale.
	
*Create textures.ini file with desired header for game and save in /new/
	Create symlink to this file in ['PSP GAME ID'] *** Do not use mklink /J
		mklink "[full path to PSP GAME ID]/textures.ini" [full path to PSP GAME ID]/new/textures.ini 

* Create directories  in /new/ for sorting specific stuff that may be more generalized. 
	See #CUSTOM FOLDERS# section and modify code as necessary
	To make sorting easier, it is recommended to create a 'sorting' directory containing symbolic links to your custom
	directories. Then you can keep three file explorer windows open and semi-automate sorting:
		One containing this file
		One with your desired directory tree
		Sorting Folder
	* First drag specific things into more specified folders before running script
	* After, drag desired target directory onto this file and it will automatically run
	* All PNG files in /new/ will be copied into target directories within /textures/ and /masters/
	* All PNG files in custom folders will be copied in to appropriate directories
	* Script will add lines into textures.ini
* When you're done going through the game you can upscale the /textures/ directory as you see fit and you will have
  a backup copy in /masters/ :)
"""
try:
	droppedDir = sys.argv[1]
	print(droppedDir)
	droppedDir = str(droppedDir)
	print(droppedDir)
	droppedDir = droppedDir.split("\\ULUS10336\\textures\\")
	print(droppedDir)
	droppedDir = droppedDir[-1]
	print(droppedDir)
	area = droppedDir.replace(os.path.sep, '/')
	print(area)

except:
	print("Something went wrong somewhere :(")
	area = input('Input game area:')


wildcard = "00000000"
uFiles = glob.glob('*png')

path = unixPath.join("textures", area)
####################CUSTOMER FOLDERS##########################
folders = ('npc', 'objects', 'art', 'dmw', 'manual')
epath = unixPath.join(path, "enemy")
print(epath)
mpath = unixPath.join("masters", area)
empath = unixPath.join(mpath, "enemy")
try:
	os.makedirs(path)

except:
	print("texture path ok!")
try:
	os.makedirs(mpath)
except:
	print("master path ok!")

exceptions = []
os.chdir('enemy/')
eFiles = glob.glob("*png")

os.chdir('../ignore/')
iFiles = glob.glob("*png")

os.chdir('..')

with open("textures.ini", "a") as ini:
	if len(uFiles) > 0:
		ini.write("\n\n")
		try:
			ini.write("#"+droppedDir+"\n")
		except:
			ini.write("#"+area+"\n")
		for uFile in uFiles:
			newpath = unixPath.join(path, uFile)
			print(newpath)
			newmpath = unixPath.join(mpath, uFile)
			ini.write(str(unixPath.splitext(uFile)[0]+" = /"+newpath+"\n"))
			shutil.copy2(uFile, newpath)
			shutil.copy2(uFile, "masters/"+area+"/"+uFile)
			os.remove(uFile)
	else:
		print ("No textures in /new/ directory!")
	

	if len(eFiles) > 0:
		try:
			os.makedirs(epath)
			os.makedirs(empath)
		except:
			print("Enemy directory ok!")
		ini.write("##{}##ENEMY##\n".format(droppedDir))
		for eFile in eFiles:
			newpath = unixPath.join(epath, eFile)
			print(newpath)
			newmpath = unixPath.join(empath, eFile)
			ini.write(str(unixPath.splitext(eFile)[0]+" = /"+newpath+"\n"))
			shutil.copy2('enemy/'+eFile, newpath)
			shutil.copy2('enemy/'+eFile, "masters/"+area+"/enemy/"+eFile)
			
			os.remove('enemy/'+eFile)
	else:
		print("Enemy directory not needed, no enemy textures in folder!")



	if len(iFiles) > 0:


		ini.write("###IGNORE THESE \n")
		for iFile in iFiles:
			ini.write(str(unixPath.splitext(iFile)[0]+" = \n"))
			os.remove('ignore/'+iFile)
	else:
		print("Ignore list not needed, no ignored textures in folder!")
	for folder in folders:
		os.chdir(folder)
		files = glob.glob("*.png")
		os.chdir('..')

		if len(files) > 0:
			ini.write("###{}{}".format(folder, "\n"))
			try:
				os.mkdirs(os.path.join(textures, folder))
				os.mkdirs(os.path.join(masters, folder))
			except:
				print("{} master & texture ok!".format(folder))
			for file in files:
				fpath = unixPath.join(folder, file)
				newpath = unixPath.join(path, fpath)
				newmpath = unixPath.join(mpath, fpath)
				print('textures/'+fpath)
				ini.write(str("{} = textures/{}\n".format(unixPath.splitext(file)[0], fpath)))
				shutil.copy2(fpath, unixPath.join('textures', folder))
				shutil.copy2(fpath, unixPath.join('masters', folder))
				os.remove(fpath)
		else:
			print("{}: nothing in folder, nothing done!".format(folder))
print("Finished! Exiting in 15 seconds...")
time.sleep(15)
