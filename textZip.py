#Zipfile Module
import zipfile
#Open and List
zip = zipfile.ZipFile("wishlist.zip", "r")
print(zip.namelist)

#MetaData
for meta in zip.infolist():
    print(meta)

info = zip.getinfo("purchased.txt")
print(info)

#Accessing files in the zip folder
print(zip.read("wishlist.txt"))
with zip.open("wishlist.txt") as f:
    print(f.read())


#Extracting files in the zip folder
zip.extract("wishlist.txt")
#Closing files in the zip folder
zip.close()
