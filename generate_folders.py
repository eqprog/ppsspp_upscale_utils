import os
import shutil

cwd = os.getcwd()
try:
	os.makedirs("textures")
except:
	print("Texture directory: OK!")
try:
	os.makedirs("masters")
except:
	print("Masters directory: OK!")

try:
	path = os.path.join(cwd, 'textures')
except:
	print("Something went wrong")
else:

	main_dirs = input("Root directories? Separate with commas: ")
	main_list = main_dirs.split(", ")
	for folder in main_list:
		main_path = os.path.join(path, folder)
		print("Subdirectories for {}? Enter 'none' if applicable".format(folder))
		main_sub=input("Separate with commas: ")
		if main_sub != "none":
	
			sublist = main_sub.split(", ")
			print(sublist)
			for sub in sublist:
					sub_path = os.path.join(main_path, sub)
					newsub = input("Add subdirectories for "+sub+": ")
					if newsub != "none":
						newlist = newsub.split(", ")
						print(newlist)
						for sub2 in newlist:
							path3 = os.path.join(sub_path, sub2)
							os.makedirs(path3)
					else:
						os.makedirs(sub_path)
		else:
			os.makedirs(main_path)
	master_path = os.path.join(cwd, 'masters')
	textures_path = os.path.join(cwd, 'textures')
	dirs = [f.name for f in os.scandir(textures_path) if f.is_dir()]
	for dir in dirs:
		source = os.path.join(textures_path, dir)
		destination = os.path.join(master_path, dir)
		try:
			shutil.copytree(source, destination)
		except:
			print(f"Could not copy {dir} to {master_path}")
		else:
			print(f"Successfully copied {dir} to {master_path}")

finally:
	print("Texture directory creation finished.")

print("Now let's create temporary directories for sorting!")
try:
	os.makedirs("sorting")
except:
	print("Sorting directory: OK!")

tempdirs = input("Sorting folder names, separate with commas: ")
tempdirs_list = tempdirs.split(", ")

for tempdir in tempdirs_list:
	try:
		os.makedirs(tempdir)
	except:
		print(f"Error when creating \'{tempdir}\'!")

print("Folder creation finished")
exit = input("Enter any key to exit!")
