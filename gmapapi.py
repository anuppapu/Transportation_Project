# -*- coding: utf-8 -*-
###############################################################################
"""
Created on Wed Aug 15 21:55:36 2018

@author: Anup
Date :   15/08/2018
Purpose: Retrieve Location informations using Google APIs
Description : This program will take geographical location as an input and 
              Provide detailed information about the location like geometry code
              (lattitude, longitude), location type, place id, type, etc ...
"""
###############################################################################
# import the libraries to capture url web details
import urllib.request, urllib.parse, urllib.error
import json

#Google Maps APIs URL
gurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
while True:
    address=input("Please Enter address:  ")
    if len(address) <1:
        break
#format the URL for the request
    url = gurl + '&address='+ address.replace(" ","+")
    print("Check URL :  " , url)

#Sends the request and reads the response.
    response = urllib.request.urlopen(url)
# Read the whole document in UTF-8
    data = response.read().decode()

# Returns object from a string. Load Internal String
    try:
        js=json.loads(data)
         
        if not js or 'status' not in js or js['status'] != 'OK':
            print('==== Failure To Retrieve ====')
            print(data)
            continue
    
        # Call json dump and print it with an indent of four
        print(json.dumps(js))
        print("**************************************************************")
        #Print Dist/state/country
        for i in range(0, len(js["results"][0]["address_components"])):      
            print("Address:  ", js["results"][0]["address_components"][i]["long_name"])
    
        #print Complete Address
        print("Complete Address:  ", js['results'][0]['formatted_address'])
        print("**************************************************************")
        #print place id
        print("place id:  ", js['results'][0]['place_id'])
        print("**************************************************************")
        #print Longitude and Lattitude
        print("Longitude: " , js["results"][0]["geometry"]["location"]["lng"])
        print("Lattitude: " , js["results"][0]["geometry"]["location"]["lat"])
    
    except:
        js=None 
        
    #End Notes
    print("******************************************************************")
    print("To Exit Press 'Enter' OR To continue 'Enter new Address' ")
    
##################################End of Program###############################   
