
"""
Class of all group caches belonging to a user. 
"""

class GroupCaches:
    def __init__(self):
        """
        Cache for speciality image for groups.

        :param groupCache: dict - Dictionary for group caches
        """
        self.groupCache={}

    
    
    def getGroupCaches(self, group):
        """
        Get cache info of specific group

        :param group: class - The group we want the cache of. 
        """

        if group.name in self.groupCache:
            groupData, timestamp = self.groupCache[group.name]

            print()


    def setGroupCache(self, groups):

