import os
import userManager as um
import groupManager as gm
import fileManager as fm



def main():
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


    fm.cleanUserDisplayFolder(userDict["Daniel"])
    fm.populateUserDisplayFolder(userDict["Daniel"], 40)


    return



if __name__ == "__main__":
    main()