#Import Temp File Module 
import tempfile

#Create a Temp File
tempFile=tempfile.TemporaryFile()


#Write a Temp File
#Note - you have to change the string into a bytes object, hence the lower case b before the string
tempFile.write(b"Save this special number for me and the rest of the planet: 42")
#Resetting the seek pointer
tempFile.seek(0)

#Read a Temp File
print(tempFile.read())

#Close a Temp File
tempFile.close()
