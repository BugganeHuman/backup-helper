from pathlib import Path
import shutil


def add_paths_in_copied_files(paths_for_add) :
    #give argument need with variable
    #can not with just a string
    with open ("copied_files.txt", 'a+') as file :
        paths_for_add_row = r""
        paths_for_add_row += paths_for_add
        paths = paths_for_add_row.split(sep=", ")
        if paths_for_add_row.strip() != "" :
            for path_string in paths:
                path = Path(path_string)
                if path.exists() :
                    file.write(path_string+"\n" )
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
        path_to_backups_list = path_to_backup_row.split(sep=", ")
        if path_to_backup_row.strip() != "" :
            for path_backup_string in path_to_backups_list :
                file.write("\n" + path_backup_string)
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
                     "by ', ' without \"\"\n: ")
        add_path_in_backup_file(paths)

def overwrite_file_copied_files () :
    with open ("copied_files.txt", 'w+') as file :
        paths = input ("write paths to copied files separator"
                        "by ', ' without \"\"\n"
                        ": ")
        add_paths_in_copied_files(paths)

def fast_backup () :

    copied_files = open("copied_files.txt", 'r+')
    backup_file = open("backup.txt", 'r+')
    # надо читать так если надо откинуть последний \n для переноса строки
    # а то вознекает ошибка, ибо ищется путь вместе с \n на конце
    backup_file_list = backup_file.read().splitlines()
    copied_files_list = copied_files.read().splitlines()
    for path_to_backup_string in backup_file_list :
        if path_to_backup_string == "":
            continue
        path_to_backup = Path(path_to_backup_string)
        if path_to_backup.is_dir()  :
            for path_to_copied_file_string in copied_files_list :
                if path_to_backup_string == "":
                    continue
                path_to_copied_file = Path(path_to_copied_file_string)
                final_path = path_to_backup / path_to_copied_file.name
                if not final_path.exists():
                    print("creating - ", path_to_copied_file)
                    shutil.copytree(path_to_copied_file,
                                    path_to_backup/path_to_copied_file.name,
                                    dirs_exist_ok=True)
                    print(path_to_copied_file, "added")
                elif final_path.exists():

                    for item in path_to_copied_file.rglob('*'):
                        if item.is_dir():
                            relative_path = item.relative_to(path_to_copied_file)
                            path_to_dir = final_path/relative_path
                            try:
                                path_to_dir.mkdir(parents=True, exist_ok=True)
                            except IOError:
                                print(IOError, "error in create dir")
                        else:
                            item_in_final_relative = item.relative_to(path_to_copied_file)
                            item_in_final = final_path/item_in_final_relative

                            if (not item_in_final.exists() or item.stat().st_mtime >
                                    item_in_final.stat().st_mtime):
                                try :
                                    if item.is_file():
                                        shutil.copy2(item, item_in_final)
                                        # ошибка в том что он проходит по всем строкас backup.txt и даже пустым
                                        print(item, "added")
                                except IOError:
                                    print(IOError,"error in fast_backup to try add", item)
                            else:
                                continue
        else:
            print (path_to_backup, " did not find")
            continue
    print ("\nready\n")
    copied_files.close()
    backup_file.close()

def manual_backup (list_of_paths_copied_files, list_of_paths_backup) :
    for path_to_backup_string in list_of_paths_backup:
        path_to_backup = Path(path_to_backup_string)
        if path_to_backup.is_dir() :
            for path_to_copied_file_string in list_of_paths_copied_files :
                path_to_copied_file = Path(path_to_copied_file_string)

                if path_to_copied_file.is_dir() :
                    try:

                        shutil.copytree(path_to_copied_file,
                                        path_to_backup/path_to_copied_file.name,
                                        dirs_exist_ok=True)
                    except IOError :
                        print (IOError)
                elif path_to_copied_file.is_file() :
                    try:
                        path_to_backup.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(path_to_copied_file, path_to_backup)
                    except IOError :
                        print(IOError)
                else:
                    print (path_to_copied_file, " did not find")
                    continue
        else :
            print (path_to_backup, " did not find")
            continue
    print("\ndone\n")
