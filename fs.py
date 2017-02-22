

# Create account with foursquare
# Create app; use example.com as website; required

# Note client_id and client_secret


import requests

client_id = 'your id here'
client_secret = 'your secret here'

# Get nearests starbucks to a zip code ; MCTC's zip code

def search_by_zip(zip_code):


    # TODO error handling

    getparams = {'near': zip_code, 'query':'starbucks', 'client_id': client_id, 'client_secret': client_secret, 'v':'20170202'}
    fs_base_url = 'https://api.foursquare.com/v2/venues/search'
    response = requests.get(fs_base_url, params=getparams)
    
    return response.json()
