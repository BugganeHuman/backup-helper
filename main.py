import logics


def main () :
    print("\nyou can write -readme")
    while True :
        main_menu_choice = input("\nwrite:\n"
                                 "0 - to exit\n\n"
                                 "1 - fast backup\n\n"
                                 "2 - create backup\n\n"
                                 "3 - permanent paths:  ")

        if main_menu_choice == "0" :
            break

        elif main_menu_choice == "1" :
            print ("\ncopying . . .\n")
            try :
                logics.fast_backup()
            except Exception :
                print(Exception)
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
            while True :
                meny_permanent_paths_choice = input("\npress:\n"
                            "0 - to main menu\n\n"
                            "1 - add paths in the text file with paths to"
                            " often copied directories or files\n\n"
                            "2 - add paths in a text file with paths backups\n\n"
                            "3 - show file with paths to copied directories or files\n\n"
                            "4 - show file with paths to backups\n\n"
                            "5 - overwrite file with paths to copied directories "
                            "or files for new paths\n\n"
                            "6 - overwrite file with paths to backups "
                            "for a new paths:       ")
                if meny_permanent_paths_choice == "0" :
                    break

                elif meny_permanent_paths_choice == "1" :
                    paths_copied_directories = input("\nwrite paths to copied"                                                    
                        " files separator by ', ' without \"\"\n"
                        ": ")
                    logics.add_paths_in_copied_files(paths_copied_directories)

                elif meny_permanent_paths_choice == "2" :
                    paths_buckup = input("write paths to backup separator"
                     "by ', ' without \"\" \n: ")
                    logics.add_path_in_backup_file(paths_buckup)

                elif meny_permanent_paths_choice == "3" :
                    logics.show_paths_of_copied_files()

                elif  meny_permanent_paths_choice == "4" :
                    logics.show_paths_of_backup()

                elif meny_permanent_paths_choice == "5" :
                    choice_in_overwrite_copied_files = input("\nare you sure?\n"
                                                        "write 0 - to back\n"
                                                        "write 1 - to go: ")
                    if choice_in_overwrite_copied_files == "0" :
                        break
                    elif choice_in_overwrite_copied_files == "1" :
                        logics.overwrite_file_copied_files()
                elif meny_permanent_paths_choice == "6" :
                    choice_in_overwrite_backup = input("\nare you sure?\n"
                                                        "write 0 - to back\n"
                                                        "write 1 - to go: ")
                    if choice_in_overwrite_backup == "0" :
                        break
                    elif choice_in_overwrite_backup == "1" :
                        logics.overwrite_file_backup()

        elif main_menu_choice == "-readme" :
            print ("\nThis is a backup-helper, he can:\n"
                   "1 - keep paths to files and backups to\n"
                   "    make a backup with just two clicks.\n"
                   "2 - make a backup of the files you wrote to it earlier.\n"
                   "3 - Make a manual backup, specifying the source and\n"
                   "    destination of the copy.\n"
                   "paths is stored in txt files, if you need something unusual\n"
                   "you can rewrite their by yourself\n"
                   "if you don't like something, you can rewrite code by yourself\n"
                   "link to repository -  https://github.com/BugganeHuman/backup-helper\n"
                   "my email - bugganehuman@gmail.com\n"
                   "                :)\n")


if __name__ == "__main__" :
    main()

