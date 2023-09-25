#!/usr/bin/python

# This is a multi-purpose Forensics Tool
# Submitted to University of Westminster
# London, Uk
# 25/09/2023
# Module : 7COSC006W – Computer System Tools
# Assessment : Coursework 2


# Author : M.F.M. Ashfaaq
# Email : w1945035@my.westminster.ac.uk

# Import Statements for essential modules

import PIL
from PIL import Image,  ExifTags
import hashlib
import os,sys 
import pyshark
import time
import requests
import json
import subprocess


################################################################################

def mainmenu():

    # This is the main function that provides a main menu and interacts with the user
    # There are 6 options the user can select from. There are 5 functions and number 6 will quit the program


    print("===============================================================")
    print("===============================================================")
    print("AUTHOR       : M.F.M. Ashfaaq")
    print("Email        : w19450355@westminster.ac.uk")
    print("Student ID   : w19450355")
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
                hashfun()
                break
            elif selection==2:
                netfun()
                break
            elif selection==3:
                memfun()
                break
            elif selection==4:
                diskfun()
                break
            elif selection==5:
                metafun()
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

################################################################################

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

    mainmenu()


################################################################################

def metafun():
    # This function will take the user input of the image file and will extract the exif information
    
    imag = input("Enter the name of the image:")
    img=PIL.Image.open(imag)
    exifdata=img._getexif()
    print(type(exifdata))

    # If no exif data is found the function will print none and if any exif information is found 
    # the function will print it on the terminal

    if exifdata is None:
        print('Sorry, image has no exif data.')
    else:
        for key, val in exifdata.items():
            if key in ExifTags.TAGS:
                print(f'{ExifTags.TAGS[key]}:{val}')
    
    sys.stdout.write('### Returning back to main page ####')
    mainmenu()


####################################################################################

def netfun():
    # This function takes the input of a pcap file and performs network forenscis analysis
    # The pyshark module is used to filter the http traffic from the pcap file
    # and store the values in the list


    file_name = input("Enter the name of the pcap file: ")

    # this list will store URLS from http and https packets
    resource_list = []

    capture = pyshark.FileCapture(file_name, display_filter='http.request.method and tcp')

    for pkt in capture:
        
        if pkt.http.request_full_uri:
            
            resource_list.append(pkt.http.request_full_uri)

    # The api key below is used to for virustotal.com
    # this key will authorize our requests
    # Replace the value of the key with your own

    api_key = "0d2b080f79d3972231b47ee9711427449992cd1d74ca9c1a5aed4dbd940dff7a"

    # The below for loop will check for malicious content on each of the http request 
    # using the virustotal database and return the results in the form of json value

    for maliouc_resource in resource_list:
    
        url = 'https://www.virustotal.com/vtapi/v2/url/report'
        params = {'apikey': api_key, 'resource': maliouc_resource}
        response = requests.get(url, params=params)
        response_json = json.loads(response.content)

    # if the resource is malicious then it will list which antivirus vendor has marked it
    
        try:
            if response_json['positives'] > 0:
                antivir_list = []

                for antivir in response_json['scans']:
                    if response_json['scans'][antivir]['detected'] == True:
                        antivir_list.append(antivir)
                
                
                print(response_json['resource'])
                print("Resource above is found malicious by",antivir_list)
        except:
            pass

        # The API access level is limited. You can make 4 requests per minute. 
        time.sleep(16)  

        exit()

    # Closing the pcap file capture and returning back to the main menu

    capture.close()
    sys.stdout.write('### Returning back to main page ####')
    mainmenu()


####################################################################################


def diskfun():
    # This function will take the user input of a disk image
    # Runs TSK's fsstat utility on the disk image 
    # Outputs the partition information to the terminal

    disk = input("Enter the disk partition name:")
    part = os.popen("fsstat " + disk).read()
    sys.stdout.write(part)

    sys.stdout.write('### Returning back to main page ####')
    mainmenu()


#################################################################################

def hashfun():
    # This function takes the input of a file and calculates the md5 and sha1 hash.
    # Outputs the value back on to the terminal

    filename = input("Enter the file name:")

    with open(filename, "rb") as f:
        bytes = f.read()
        readable_hash =  hashlib.md5(bytes).hexdigest();
        readable_hash2 = hashlib.sha1(bytes).hexdigest();

        print("========================================")
        print("MD5 hash value  :" + readable_hash)
        print("SHA1 hash value :" + readable_hash2)
        print("========================================")

    sys.stdout.write('### Returning back to main page ####')
    mainmenu() 
    
##################################################################################

mainmenu()

