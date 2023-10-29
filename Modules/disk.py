import sys
import os
import pytsk3


def diskfun():
    # This function will take the user input of a disk image
    # Runs TSK's fsstat utility on the disk image 
    # Outputs the partition information to the terminal

    disk = input("Enter the disk partition name:")
    part = os.popen("fsstat " + disk).read()
    sys.stdout.write(part)

    sys.stdout.write('### Returning back to main page ####')
    