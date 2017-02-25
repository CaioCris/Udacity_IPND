import os

def rename_files():
    file_list = os.listdir(r"/home/caio-cris/Projetos/Udacity/intro_programming_nanodegree//Stage3/prank")
    print(file_list)
    saved_path = os.getcwd() # to know where you are, in which dir
    os.chdir(r"/home/caio-cris/Projetos/Udacity/intro_programming_nanodegree//Stage3/prank")
    for file_name in file_list:
        new_name = file_name.translate(file_name.maketrans("","","0123456789"))
        print("Old name - "+file_name)
        print("New name - "+new_name)
        os.rename(file_name, new_name)
    os.chdir(saved_path)

rename_files()