import os


path = os.getcwd()

main_dirs = input("Root directories? Separate with commas:")
main_list = main_dirs.split(", ")
for folder in main_list:
	main_path = os.path.join(path, folder)
	main_sub=input("Subdirectories for {}? Separate with commas:".format(folder))
	if main_sub != "none":

		sublist = main_sub.split(", ")
		for sub in sublist:
				sub_path = os.path.join(main_path, sub)
				newsub = input("Add subdirectories for "+sub+":")
				if newsub != "none":
					newlist = newsub.split(", ")
					for sub2 in newlist:
						path3 = os.path.join(sub_path, sub2)
						os.makedirs(path3)
				else:
					os.makedirs(sub_path)
	else:
		os.makedirs(main_path)


