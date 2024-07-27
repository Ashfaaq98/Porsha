
import time
import sys
import pyshark
import json
import requests

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

    api_key = ""

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
