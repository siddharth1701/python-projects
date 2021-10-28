############ Method : 1 ############

# import os
# print(os.path.abspath(os.getcwd()))

# def folder_create(name):
#     directory = os.path.abspath(os.getcwd())
#     os.chdir(directory)
#     fileli = os.listdir()
#     if name in fileli:
#         print(f'Folder "{name}" exist!')
#     else:
#         os.mkdir(name)
#         print(f'Folder "{name}" succesfully created!')
#         return


# folder_create('test folder')



############ Method: 2 ############
# import os

# # Gets current working directory
# path = os.getcwd()

# # Joins the folder that we wanted to create
# folder_name = 'output'
# path = os.path.join(path, folder_name)

# # Creates the folder, and checks if it is created or not.
# os.makedirs(path, exist_ok=True)


############ Method : 3 ############
# import os

# folderName = "test folder"
# if not os.path.exists(os.getcwd() + '/' + folderName):
#     os.makedirs(os.getcwd() + '/' + folderName, exist_ok=True) 


############ Method : 4 ############
# import os
# import os.path

# folder = "abc"
# os.chdir(".")
# print("current dir is: %s" % (os.getcwd()))

# if os.path.isdir(folder):
#     print("Exists")
# else:
#     print("Doesn't exists")
#     os.mkdir(folder)
#     print(f'Folder "{folder}" succesfully created!')


############ Method : 5 ############
# import os, errno
# try:
#     os.makedirs('my_folder')
#     print("Folder created successfully!")
# except OSError as e:
#     # If error is not already exists, then raise the error else continue
#     if e.errno != errno.EEXIST:
#         raise
# # Now do what you want with my_folder

############ Method : 6 ############
import os
if not os.path.exists('my_folder'):
    os.makedirs('my_folder')
    print("Folder created successfully!")