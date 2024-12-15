import photoManager as pm
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS


filePath = 'path'
newDate = datetime(2002, 12, 22, 18, 42) # Replace with the desired date
pm.editImageDate(filePath, newDate)


print(pm.photoGetDate(filePath))
