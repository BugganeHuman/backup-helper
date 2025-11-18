from pathlib import Path



def add_paths_in_copied_files(paths_for_add) :
    #give argument need with variable
    #can not with just a string
    with open ("copied_files.txt", 'a+') as file :
        paths_for_add_row = r""
        paths_for_add_row += paths_for_add
        paths = paths_for_add_row.split(sep=" ")
        if paths_for_add_row.strip() != "" :
            for path_string in paths:
                path = Path(path_string)
                if path.exists() :
                    file.write(path_string + "\n")
                else :
                    print (path_string + " didn't add because"
                    " it is not exists path")
            print("\ndone\n")
        else :
            print ("path is empty")

def add_path_in_backup_file(path_to_backup) :
    # give argument need with input
    # can not with just a string
    with open("backup.txt", 'a+') as file :
        path_to_backup_row = r""
        path_to_backup_row += path_to_backup
        path_to_backups_list = path_to_backup_row.split(sep=" ")
        if path_to_backup_row.strip() != "" :
            for path_backup_string in path_to_backups_list :
                file.write(path_backup_string + "\n")
            print ("\ndone\n")
        else :
            print("path is empty")

def show_paths_of_backup() :
    with open("backup.txt", 'r') as file :
        list_paths = file.readlines()
        for path in list_paths :
            print(path)

def show_paths_of_copied_files() :
    with open ("copied_files.txt", 'r') as file :
        list_paths = file.readlines()
        for path in list_paths :
            print (path)

def overwrite_file_backup() :
    with open ('backup.txt', 'w+') as file :
        paths = input("write paths to backup separator"
                     "by space without \"\"\n: ")
        add_path_in_backup_file(paths)

def overwrite_file_copied_files () :
    with open ("copied_files.txt", 'w+') as file :
        paths = input ("write paths to copied files separator"
                        "by space without \"\"\n"
                        ": ")
        add_paths_in_copied_files(paths)


#       TESTS DOWN
#___________________________________________________
#if __name__ == "__main__" :

 #   overwrite_file_copied_files()




#____________________________________________________
#       END TESTS



"""
нужны функции -

1) add_paths_in_copied_files(path) - сначала надо path разбить по пробелам
и записать в list, и элементы list записать в файл copied_files.txt

2) add_path_in_backup_file(path_to_backup) записывает только один путь или
несколько что бы копировалост в несколько мест 🐍

3) show_file_path_to_backup()

4) show_create_file_copied_files()

5) overwrite_file_path_to_backup() - удаляет все строки и вызывает
    add_path_to_backup_in_backup(path)

6)overwrite_file_copied_files() - удаляет все строки и вызывает
    add_paths_in_copied_files(path)

7) copy (copy, backup) деректория или деректории backup (через пробел можно -
разделить) копирутся в backup если есть изминения (это надо додумать)
"""


