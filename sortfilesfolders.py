import os
import shutil

# Change to the working directory

#os.chdir('/home/marceloramirez/Documents/prueba')

# Extract the name of the folders from file names, as file names contain creation year, month and day the day is replaced by 01 

fol = []
filesfolders = []
for f in os.listdir('/home/marceloramirez/Documents/20200601_Fotos'):
     f_name, f_ext = os.path.splitext(f)
     fo_name = f_name[4:10]+'01'
     fol.append(fo_name)
     filesfolders.append([fo_name,f])

# Remove duplicate names

folders = list(set(fol))

# Alternate way for removing duplicates
# folder = []
# for name in fol:
#      if name not in folder:
#           folder.append(name)

print(folders)
print(filesfolders)


# Create the folders with the year, month and first day 

for fo in folders:
     os.mkdir('/home/marceloramirez/Documents/20200601_Fotos/' + fo)

f_path = '/home/marceloramirez/Documents/20200601_Fotos/'

# Move a file from the directory d1 to d2

for fifo in filesfolders:
     d1 = f_path+fifo[1]
     d2 = f_path+fifo[0]+'/'+fifo[1]
     shutil.move(d1, d2)


# # Move a file from the directory d1 to d2
# shutil.move('/Users/billy/d1/xfile.txt', '/Users/billy/d2/xfile.txt')