import os
import json


class User:
    def __init__(self, name, dumpFolder, displayFolder, interestMap, groups=None):
        self.name = name
        self.dumpFolder = dumpFolder
        self.displayFolder = displayFolder
        self.priorityInterest = interestMap
        self.groups = groups


    def addGroup(self, group):
        if group not in self.groups:
            self.groups.append(group)

    def movePhotos(self):
        for group in self.groups


class  Group:
    def __init__(self, name, members):
        self.name = name
        self.members = members


    def addMemeber:
        #To be Implemented



def movePhotosBasedOnMembership(user):
    for group in user.groups:
        