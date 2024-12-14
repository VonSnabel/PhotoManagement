import json

#Logic order
#Check new photos (last 7 days)
#Check anneversaries
#Fill with random from priority list.

class User:
    def __init__(self, name, dumpFolder, displayFolder, groups=None):
        """
        Initialize a User object.

        :param name: str - The name of the user
        :param group: list - The groups this user belongs to.
        :param displayFolder: str - The display folder for the user.
        :param dumpFolders: list - The image dump locations.
        :param priorityInterest: map - The weight for other users.
        """
        self.name = name
        self.groups = groups
        self.displayFolder = displayFolder
        self.dumpFolder = dumpFolder
        #self.priorityInterest = interestMap

    def _generateGroupFolders(self):
        """
        Note: Quite sure I need to redo this a bit since each user has their own folder. 

        Generates folder paths for each group the user belongs to.

        :return: dict - Dictionary mapping group names to folder paths. 

        """
        return {group: f"{self.base_folder}/{group}" for group in self.groups}


    def get_group_folder(self, group_name):
        """
        Get the folder path for a specific group.

        :param group_name: str - The name of the group.
        :return: str or None - Folder path if the group exists, otherwise None.
        """
        return self.group_folders.get(group_name)

    def belongs_to_group(self, group_name):
        """
        Check if the user belongs to a specific group.

        :param group_name: str - The name of the group to check.
        :return: bool - True if the user is in the group, False otherwise.
        """
        return group_name in self.groups


def loadUsersFromJson(jsonPath):
    with open(jsonPath, 'r') as file:
        data=json.load(file)
    users = []
    for userData in data["users"]:
        user = User(
            name=userData["name"],
            groups=userData["groups"],
            displayFolder=userData["displayFolder"],
            dumpFolder=userData["dumpFolder"]
        )
        users.append(user)
    return users