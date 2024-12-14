import os
import json

#Logic order
#Check new photos (last 7 days)
#Check anneversaries
#Fill with random from priority list.

class User:
    def __init__(self, name, dumpFolder, displayFolder, interestMap, groups=None):
        self.name = name
        self.dumpFolder = dumpFolder
        self.displayFolder = displayFolder
        self.priorityInterest = interestMap
        self.groups = groups
        self.nbrGroups = len(groups)


    def addGroup(self, group):
        if group not in self.groups:
            self.groups.append(group)

    def movePhotos(self):
        for group in self.groups:
            print()

    def moveNewImages(self):
        #For each map of members check new photos. 
        #Take count and then check 

    def movePhotosBasedOnMembership(self):
        for group in self.user.groups:
            if group in self.user.priorityInterest:
                print()
            else:
                print()




class  Group:
    def __init__(self, name, members):
        self.name = name
        self.members = members
    








        