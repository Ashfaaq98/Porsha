#!/usr/bin/python

# This is a multi-purpose Forensics Tool
# Author : M.F.M. Ashfaaq
3
# Import Statements for essential modules

from Modules import disk, memory, hash, metadata, network


################################################################################

def mainmenu():

    # This is the main function that provides a main menu and interacts with the user
    # There are 6 options the user can select from. There are 5 functions and number 6 will quit the program


    print("===============================================================")
    print("===============================================================")
    print("AUTHOR       : M.F.M. Ashfaaq")
    print("---------------------------------------------------------------")
    print("******************** Welcome to Porsha  ***********************")
    print("---------------------------------------------------------------")
    print("Please select the activity you wish to Perform")
    print("---------------------------------------------------------------")
    print("---------------------------------------------------------------")
    print("1. Create Hashes for the files.")
    print("2. Perform network Forensics on pcap files")
    print("3. Perform Memory Forensics on memory dumps")
    print("4. Perform disk forensics")
    print("5. Extract metadata from images")
    print("6. Quit the Program")
    print("---------------------------------------------------------------")
    print("---------------------------------------------------------------")
    print("================================================================")

    # The while loop checks the user input and executes the forensics function.
    while True:
        try:
            selection=int(input("Enter the number of your choice: "))
            if selection==1:
                hash.hashfun()
                break
            elif selection==2:
                network.netfun()
                break
            elif selection==3:
                memory.memfun()
                break
            elif selection==4:
                disk.diskfun()
                break
            elif selection==5:
                metadata.metafun()
                break
            elif selection==6:
                print("--------------------------------------")
                print("+++++++++++++++ EXIT +++++++++++++++++")
                exit()
            else:
                print("Invalid choice. Choose from 1 to 6")
                mainmenu()

        except ValueError:
                print("Something went wrong. Choose from 1 to 6")
    exit


mainmenu()

