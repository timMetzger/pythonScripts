# *******************
# By: Timothy Metzger
# *******************

import os


def main():
    """Asks user for a base folder name and number of folders they
        wish to create in a user specified directory
        ie Base Folder Name: Homework , Number of Folders: 10  --> Homework 1, Homework 2,..., Homework n """

    base_name = input("Base folder name: ")
    number_folders = int(input("Number of folders you wish to create: "))
    directory = input("Directory: ")

    directory = directory.replace("\\", "/")
    print(directory)

    if not os.path.exists(directory + "/" + base_name + "s"):
        os.mkdir(directory + "/" + base_name + "s")

    for i in range(1, number_folders + 1):
        try:
            os.mkdir(directory + "/" + base_name + "s/" + f'{base_name} {i}')
        except Exception:
            print(Exception)


if __name__ == '__main__':
    main()
