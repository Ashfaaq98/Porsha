import sys
import os

def memfun():
    # This function will perform forenscis analysis on a memory image
    # Takes the filename as the input and runs the basics volatility scripts on the memory image.

    filenamemem = input("Enter the name of the memory dump:")

    # Runs the Volatility script to gather information.
    # Using the grep utility to filter System and Os information and cut the value using awk tool
    # Variables memm1 and memm2 will store the System Time and OS information of the image


    sys.stdout.write("\n#### Retrieving information from memory image......#### \n")
    sys.stdout.flush()
    memm1 = os.popen("vol.py -f memory.img info.Info 2>/dev/null | grep NtProductType | awk '{print $2}'").read()
    memm2 = os.popen("vol.py -f memory.img info.Info 2>/dev/null | grep SystemTime| awk '{print $2,$3}'").read()

    # Variable memm3 will store the process tree information of the image dump
    # The volatility script to extract windows process list from the dump and 
    # pipe it avoid reading the first 3 lines using tail 

    sys.stdout.write("\n#### Retrieving process list information from memory image......#### \n")
    sys.stdout.flush()
    memm3 = os.popen("vol.py -f memory.img windows.pslist.PsList 2>/dev/null | tail -n +3").read()

    # Variable memm4 will store the windows registry list form the memory dump

    sys.stdout.write("\n#### Retrieving Registry information from memory image......#### \n")
    sys.stdout.flush()
    memm4 = os.popen("vol.py -f memory.img windows.registry.hivelist.HiveList 2>/dev/null | tail -n +2").read()

    # Variable memm5 will store the malicious processes from the memory dump

    sys.stdout.write("\n#### Searching for suspicous malware information  information from memory image......#### \n")
    sys.stdout.flush()
    memm5 = os.popen("vol.py -f memory.img windows.malfind.Malfind 2>/dev/null | tail -n +2").read()

    print("################################################")
    print("Saving the retrieved information to file\n")


    # Finally the function will save the stored information in the variables to a text file.
    # After successfully storing the information the function will return back to the main menu.

    with open("memory.txt","w") as text:
        text.write("Product Type:" + memm1)
        text.write("System Type: " + memm2)
        text.write("=====================================================\n")
        text.write("List of processes running on Memory\n" + memm3)
        text.write("=====================================================\n")
        text.write("Information of the Registry Hive \n" + memm4)
        text.write("======================================================\n")
        text.write("Malicious Findings \n" + memm5)

    sys.stdout.write("#### Successfully Saved ####\n")
    sys.stdout.write('### Returning back to main page ####')
    sys.stdout.flush()