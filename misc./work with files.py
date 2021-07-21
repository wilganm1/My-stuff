""" Working with files """
import os
#Know where the file you want to work with is

os.getcwd()
os.chdir('\\insert path here')

"""Check if file exists """
if os.path.exists(".\\nameoffile.txt"):
    print("file exists")
else:
    print("The file does not exist")

""" Create new file """
with open("nameOfFile.txt", "x") as file:
    #stuff here. 

""" Overwrite/create file """
with open("fileName.txt", "w") as file, open("fileName2","r") as file2:
file.write("information in file")

""" Open existing file """ #default
with open("file_name.extension", 'r') as file:

""" Append to file """
with open("filename.txt", "a") as file:

""" Read the file """
print(file.read())
print(file.read(n)) #print n characters

print(file.readline()) #prints one line
#keep printing readline to read each line

#loop through the file line by line
with open("nameoffile", 'r') as file:
    for x in file:
        print(x)
    
""" Read multiple files"""
import fileinput
import sys

files = fileinput.input()
for line in files:
    if fileinput.isfirstline():
        print(f'\n--- Reading {fileinput.filename()} ---')
    print(' -> ' + line, end='')
print()

""" Delete files"""

os.remove("filename.txt")
#delete whole folder
os.rmdir("folderName")

""" Rename files """
os.rename('name', 'new_name')

from pathlib import Path
data_file = Path('filename')
data_file.rename('newfilename')

""" Save to a specific directory """
path = "Insert path here"
file_name = "nameoffile.txt"
os.path.join(path, file_name)

""" Archiving ZIP and TAR """
#Read ZIP files
import zipfile

#get list of file in archive
with zipfile.ZipFile('data.zip','r') as zipobj:
    zipobj.namelist()
    
#Get information about file
    bar_info = zipobj.getinfo('sub_dir/bar.py')
    bar_info.file_size
    
#Extract zip archives
data_zip = zipfile.ZipFile('data.zip','r')

#Extract 1 file
data_zip.extract('file1.py')

#Extract all files to a different directory
data_zip.extractall(path='destination_dir')
data_zip.close()
    
""" Creating zip archives """
#Write a new zip archive
file_list = [file1.py, 'sub_dir/']
with zipfile.ZipFile('new.zip', 'w') as new_zip:
    for name in file_list:
        new_zip.write(name)
        
#Adding to existing arhive
with zipfile.ZipFile('new.zip', 'a') as new_zip:
    new_zip.write('data.txt')
    new_zip.write('latin.txt')

""" Searching for files """
#Search a directory for files
for f_name in os.listdir('some_directory'):
    if f_name.endswith('.txt'):
        print(f_name)

#use fnmatch
import fnmatch

for file_name in os.listdi('some_dir/'):
    if fnmatch.fnmatch(file_name, '*.txt'):
        print(file_name)
        
#use glob with wildcard * to find all matches
import glob

for name in glob.glob('*[0-9]*.txt'):
    
#search recursively through subdirectories
for file in glob.iglob('**/*.py', recursive = True):
    print(file)

#search for files of types that startwith something
from pathlib import Path
    p = Path('.')
    for name in p.glob('*.p*'):
        print(name)
        
""" Moving & Copying files """
import shutil
#copying a file
src = "source here"
dst = 'destination'
shutil.copy2(src, dst)

#copying a directory to another
shutil.copytree('source_dir', 'dest_dir')

#moving files
shutil.move(src, dst)

