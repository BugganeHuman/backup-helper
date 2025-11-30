import logics


def main () :
    logics.start()
    print("\nyou can write -readme")
    while True :
        main_menu_choice = input("\nwrite:\n"
                                 "0 - to exit\n\n"
                                 "1 - fast backup\n\n"
                                 "2 - manual backup\n\n"
                                 "3 - permanent paths:  ")

        if main_menu_choice == "0" :
            break
        elif main_menu_choice == "1" :
            print ("\ncopying . . .\n")
            try :
                logics.fast_backup()
            except Exception as e:
                print(e, "error in main(logics.fast_backup())")

        elif main_menu_choice == "2" :
            paths_copied_files = input("\nwrite paths to copied files"     
                                        " separator by ', ' without \"\" \n"
                                        ": ")
            list_of_paths_copied_files = paths_copied_files.split(sep=", ")
            paths_backup = input ("\nwrite paths to backup separator"
                                "by ', ' without \"\"\n: ")
            print ("\ncopying . . .\n")
            list_of_paths_backup = paths_backup.split(sep=", ")

            logics.manual_backup(list_of_paths_copied_files, list_of_paths_backup)

        elif main_menu_choice == "3" :
            dict_acts_add = {
                "1": logics.add_paths,
                "2": logics.add_paths,
                "3": logics.add_paths,
                "4": "copied_files.txt",
                "5": "backup.txt",
                "6": "exceptions.txt",
            }
            dict_acts_show = {
                "1": logics.show_paths,
                "2": logics.show_paths,
                "3": logics.show_paths,
                "4": "copied_files.txt",
                "5": "backup.txt",
                "6": "exceptions.txt",
            }
            dict_acts_overwrite = {
                "1": logics.overwrite_file,
                "2": logics.overwrite_file,
                "3": logics.overwrite_file,
                "4": "copied_files.txt",
                "5": "backup.txt",
                "6": "exceptions.txt",
            }
            while True :
                meny_permanent_paths_choice = input("\n press:\n"
                            "0 - to main menu\n\n"
                            "1 - add paths \n\n"
                            "2 - show file\n\n"
                            "3 - overwrite file\n"
                            ":  ")
                if meny_permanent_paths_choice == "0" :
                    break
                elif meny_permanent_paths_choice == "1" :
                    while True:
                        choice_to_add_paths = input("\nwrite number for add paths of:\n"
                                                "0 - return\n\n"
                                                "1 - copied_files\n\n"
                                                "2 - backup\n\n"
                                                "3 - exceptions\n"
                                                ":  ")
                        if choice_to_add_paths == "0":
                            break
                        else:
                            if choice_to_add_paths in dict_acts_add:
                                var = str(int(choice_to_add_paths) + 3)
                                try:
                                    dict_acts_add[choice_to_add_paths](dict_acts_add[var])
                                except Exception as e:
                                    print(e)

                elif meny_permanent_paths_choice == "2" :
                    while True:
                        choice_to_show = input("\nwrite number for show paths of:\n"
                                                    "0 - return\n\n"
                                                    "1 - copied_files\n\n"
                                                    "2 - backup\n\n"
                                                    "3 - exceptions: ")
                        if choice_to_show == "0":
                            break
                        else:
                            if choice_to_show in dict_acts_show:
                                var = str(int(choice_to_show) + 3)
                                try:
                                    print()
                                    dict_acts_show[choice_to_show](dict_acts_show[var])
                                except Exception as e:
                                    print(e)
                elif meny_permanent_paths_choice == "3":
                    while True:
                        choice_to_overwrite = input("\nwrite number to overwrite paths of:\n"
                                                    "0 - return\n\n"
                                                    "1 - copied_files\n\n"
                                                    "2 - backup\n\n"
                                                    "3 - exceptions: ")
                        if choice_to_overwrite == "0":
                            break
                        else:
                            if choice_to_overwrite in dict_acts_overwrite:
                                var = str(int(choice_to_overwrite) + 3)
                                try:
                                    dict_acts_overwrite[choice_to_overwrite](dict_acts_overwrite[var])
                                    break
                                except Exception as e:
                                    print(e)
        elif main_menu_choice == "-readme" :
            print ("\nThis is a backup-helper, he can:\n"
                   "1 - keep paths to files and backups to\n"
                   "    make a backup with just two clicks.\n"
                   "2 - make a backup of the files you wrote to it earlier.\n"
                   "3 - Make a manual backup, specifying the source and\n"
                   "    destination of the copy.\n"
                   "IMPORTANT:\n"
                   "    If you plan to back up something frequently and of large size,\n"
                   "    I strongly recommend using fast backup because it copies only those files\n"
                   "    that have been changed, while manual backup simply overwrites files.\n"
                   "paths is stored in txt files, if you need something unusual\n"
                   "you can rewrite their by yourself\n"
                   "if you don't like something, you can rewrite code by yourself\n"
                   "link to repository -  https://github.com/BugganeHuman/backup-helper\n"
                   "my email - bugganehuman@gmail.com\n"
                   "                :)\n")


if __name__ == "__main__" :
    main()
    
