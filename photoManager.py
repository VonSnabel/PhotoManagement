import os
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime



def photoGetDate(filePath):
    """
    Extracts date of photo from EXIF metadata.
    If failed, returns file modification date.

    :param filePath: str - path to image. 
    :return imageDate: 
    """

    try:
        img = Image.open(filePath)
        exifData = img._getexif()
        if exifData is None:
            raise ValueError("No EXIF metadata")
        
        for tagID, value in exifData.items():
            tagName = TAGS.get(tagID, tagID)
            if tagName == "DateTimeOriginal":
                return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
        
    except Exception as e:
        print(f"Error reading EXIF data from {filePath}: {e}")


    try:
        return datetime.fromtimestamp(os.path.getmtime(filePath))
    except Exception as e:
        print(f"Error getting modification date for {filePath}: {e}")
        return None
