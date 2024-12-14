import os
import random
import shutil

def populateUserDisplayFolder(User, minPhotos=300):
    """
    Adds photos to Display Folder for given User. 
    Takes photos from associated groups.
    Will prioritieze newly taken photos and anniversary photos.

    :param User: object - User Class Object
    :param minPhotos: int - number of photos it'll try to add, assuming there is enough. 
    """
    displayFolder = User.displayFolder
    os.makedirs(displayFolder, exist_ok=True)

    currentPhotos = set(os.listdir(displayFolder))
    for group in User.groups:
        for photo in group.cache:
            if photo["path"] not in currentPhotos:
                shutil.copy(photo["path"], displayFolder)
                currentPhotos.add(photo["path"])
                print(f"Photo added from priority")


    photoBank = []
    for group in User.groups:
        for folder in group.getRelevantFolders():
            folderPhotos = os.listdir(folder)
            photoBank.extend(os.path.join(folder, photo) for photo in folderPhotos)
    
    random.shuffle(photoBank)

    for photoPath in photoBank:
        if len(currentPhotos)>=minPhotos:
            break
        shutil.copy(photoPath, displayFolder)
        currentPhotos.add(photoPath)

    print(f"Populated display folder for {User.name} with {len(currentPhotos)} photos.")



def cleanUserDisplayFolder(User):
    """
    Deletes all files in the given users displayfolder

    :param User: Object - User Class Object
    """
    #ONLY WIP
    deleted = 0
    nbrToBeDeleted = len(os.listdir(User.displayFolder))

    if not os.path.exists(User.displayFolder):
        print(f"Display folder of user {User.name}: {User.displayFolder} does not exist. Nothing to clean.")
        return
    
    for fileName in os.listdir(User.displayFolder):
        filePath = os.path.join(User.displayFolder, fileName)
        try:
            if os.path.isfile(filePath):
                os.remove(filePath)
                deleted+=1
        except Exception as e:
            print(f"Error deleting {filePath}: {e}")

    print(f"Clean up has deleted {deleted} out of {nbrToBeDeleted} photos for user {User.name}")



