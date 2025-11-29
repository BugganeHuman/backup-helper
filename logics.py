from pathlib import Path
import shutil
from shlex import split


def add_paths (path_to_file):
    paths_for_add = input(f"n\nwrite paths to {path_to_file} "                                                    
                        "separator by ', ' without \"\"\n"
                        ": ")
    with open (path_to_file, 'a+') as file :
        paths_for_add_row = r""
        paths_for_add_row += paths_for_add
        paths = paths_for_add_row.split(sep=", ")
        if paths_for_add_row.strip() != "" :
            for path_string in paths:
                path = Path(path_string)
                if path.exists() :
                    file.write(path_string + "\n" )
                else :
                    print (path_string + " didn't add because"
                    " it is not exists path")
            print("\ndone\n")
        else :
            print ("path is empty")

def show_paths(path_to_file):
    with open(path_to_file, 'r') as file :
        list_paths = file.readlines()
        for path in list_paths :
            print(path)

def overwrite_file(path_to_file) :
    with open (path_to_file, 'w+') as file :
        paths = input(f"write paths to {path_to_file}separator"
                     "by ', ' without \"\"\n: ")
        choice_in_exceptions = input("\nare you sure?\n"
                                     "write 0 - to back\n"
                                     "write 1 - to go: ")
        if choice_in_exceptions == "0":
            return
        elif choice_in_exceptions == "1":
            add_paths(path_to_file)

def fast_backup () :

    copied_files = open("copied_files.txt", 'r+')
    backup_file = open("backup.txt", 'r+')
    exceptions_file = open("exceptions.txt", 'r+')
    # надо читать так если надо откинуть последний \n для переноса строки
    # а то вознекает ошибка, ибо ищется путь вместе с \n на конце
    backup_file_list = backup_file.read().splitlines()
    copied_files_list = copied_files.read().splitlines()
    exceptions_file_list = exceptions_file.read().splitlines()
    for path_to_backup_string in backup_file_list :
        if path_to_backup_string == "":
            continue
        path_to_backup = Path(path_to_backup_string)
        if path_to_backup.is_dir()  :
            for path_to_copied_file_string in copied_files_list :
                if path_to_copied_file_string in exceptions_file_list:
                    print(f"skipped {path_to_copied_file_string}")
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
                        print(item)
                        if item in exceptions_file_list: # баг 
                            print(f"skipped {item}")
                            continue
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
