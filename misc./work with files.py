""" Working with files """
import os
#Know where the file you want to work with is

os.getcwd()
os.chdir('\\insert path here')

"""Check if file exists """
if os.path.exists("nameoffile.txt"):
    print("file exists")
else:
    print("The file does not exist")

""" Save to a specific file """
path = "Insert path here"
file_name = "nameoffile.txt"
os.path.join(path, file_name)

""" Create new file """
file = open("nameOfFile.txt", "x") #x creates file

""" Overwrite/create file """
file = open("fileName.txt", "w")
file.write("information in file")

""" Open existing file """ #default
file = open("file_name.extension", 'r')

""" Append to file """
file = open("filename.txt", "a")

""" Read the file """
print(file.read())
print(file.read(n)) #print n characters

print(file.readline()) #prints one line
#keep printing readline to read each line

#loop through the file line by line
for x in file:
    print(x)
    
#close file
file.close()

#delete file
os.remove("filename.txt")
#delete whole folder
os.rmdir("folderName")
