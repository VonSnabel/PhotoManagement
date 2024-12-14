import os
import time
import json
import photoManager as pm
from datetime import datetime, timedelta



class Group:
    def __init__(self, name, memberNames):
        """
        Initialize a Group object.

        :param name: str - The name of the group
        :param memberNames: list - List of member names, user str
        :param members: list - The members of the group, user class
        :param relevantFolders: list - The folders associated with the group
        :param cache: list - Cache for speciality Photos. (e.g. New or anniversary)
        """
        self.name = name
        self.memberNames = memberNames
        self.members = []
        self.relevantFolders = []
        self.cache = []

    def addMember(self, User):
        """
        Add User Class to list of members.

        :param User: Class - User Class of member
        """
        self.members.append(User)
        self.relevantFolders.append(User.dumpFolder+"/"+self.name)
        if os.path.isdir(User.dumpFolder+"/All"):
                self.relevantFolders.append(User.dumpFolder+"/All")


    def getRelevantFolders(self):
        """
        Returns list of all relevant folders for the group

        :return relevantFolders: list - list of path to relevant folders.
        """
        return self.relevantFolders

    def updateCache(self):
        """
        Update cache
        Should be run each day. 
        """
        self.cache = []
        today = datetime.now()
        recentThreashold = today - timedelta(days=7) # Define recent as one week.

        for folder in self.relevantFolders:
            for filename in os.listdir(folder):
                filePath = os.path.join(folder, filename)

                if not os.path.isfile(filePath):
                    continue

                if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                    continue

                photoDate = self.getPhotoDate(filePath)
                if not photoDate:
                    continue

                # Check new photos
                if photoDate >= recentThreashold:
                    self.cache.append({
                        "type":"new",
                        "path": filePath,
                        "date": photoDate
                    })
                
                #Find Anniversary Photos
                if (photoDate.month == today.month & photoDate.day == today.day):
                    self.cache.append({
                        "type": "anniversary",
                        "path": filePath,
                        "date": photoDate
                    })

    def getPhotoDate(self, filePath):
        return pm.photoGetDate(filePath)

    def getCache(self):
        """
        :return cache: list - Cache with speciality photos
        """
        return self.cache



def loadGroupsFromJson(jsonPath):
    with open(jsonPath, 'r') as file:
        data=json.load(file)
    groups = []
    for groupData in data["groups"]:
        group = Group(
            name=groupData["name"],
            memberNames=groupData["members"]
        )
        groups.append(group)
    return groups