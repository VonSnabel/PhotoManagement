import os
import userManager as um
import groupManager as gm



def main():
    users = um.loadUsersFromJson("/home/main/Documents/PhotoManagement/users.json")
    for user in users:
        print(user.name)

    return

if __name__ == "__main__":
    main()