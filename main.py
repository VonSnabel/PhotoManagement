import os
import userManager as um
import groupManager as gm
import fileManager as fm
from logger import logger


def main():
    logger.info("Program Started")
    users = um.loadUsersFromJson("/home/main/Documents/PhotoManagement/users.json")
    userDict = {}
    for i in users:
        userDict[i.name] = i
    groups = gm.loadGroupsFromJson("/home/main/Documents/PhotoManagement/groups.json")
    groupDict = {}
    for i in groups:
        groupDict[i.name] = i

    for user in users:
        for group in user.groupNames:
            user.addGroup(groupDict[group])
    
    for group in groups:
        for member in group.memberNames:
            group.addMember(userDict[member])
        group.getRelevantFolders()

    print("Starting Grouping")
    groupDict["Vernersson"].updateCache()
    groupDict["Mattsson"].updateCache()
    print("Grouping Done")

    
    for i in users:
        print("Cleaning User: ", i.name)
        fm.cleanUserDisplayFolder(userDict[i.name])
        print("Populating User: ", i.name)
        fm.populateUserDisplayFolder(userDict[i.name], 5)

    logger.info("Program Finished")
    return



if __name__ == "__main__":
    main()