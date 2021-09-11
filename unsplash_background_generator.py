import os
import random
import sys
import urllib
import numpy as np
import requests
import shutil # to save it locally
import ctypes
import os
import time

query_term = 'mountains'

# Unsplash API configuration
client_id = '' ## you will need an unsplash client ID
collections_url = 'https://api.unsplash.com/search/collections'
photos_url = 'https://api.unsplash.com/photos/random'


# Retrieving unsplash image url and stylizing
collections_response = requests.get(collections_url, params={'client_id': client_id, 'query': query_term, 'per_page':'100'}).json()


collection_list_response = 0
collections_ids = []
for each in collections_response['results']:
    collections_ids.append(collections_response['results'][collection_list_response]['id'])
    collection_list_response +=1

collections_ids = ','.join([str(i) for i in collections_ids if i])

photos_response = requests.get(photos_url, params={'client_id': client_id, 'collections': collections_ids , 'orientation': 'landscape'}).json()



## Set up the image URL and filename
image_url = photos_response['links']['download']
print(photos_response)
filename = image_url.split("/")[-1]+'.jpg'

# Open the url image, set stream to True, this will return the stream content.
r = requests.get(image_url, stream = True)

# Check if the image was retrieved successfully
if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r.raw.decode_content = True
    
    # Open a local file with wb ( write binary ) permission.
    with open(filename,'wb') as f:
        shutil.copyfileobj(r.raw, f)
        
    print('Image sucessfully Downloaded: ',filename)
else:
    print('Image Couldn\'t be retreived')

absolute_filepath = os.path.abspath(filename)


SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, absolute_filepath , 0)
