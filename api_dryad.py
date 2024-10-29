#!/usr/bin/env python3

import urllib.request
import json


# Search Dryad using the Dryad API

ENDPOINT = 'https://datadryad.org/api/v2'

# Search for datasets which have authors affiliated with UAB

params = {
    "affiliation": "https://ror.org/008s83205",
    "per_page": 100,
}

search_url = ENDPOINT + '/search?' + urllib.parse.urlencode(params)
print(search_url)
count = 1
# Get search results as parsed JSON
with urllib.request.urlopen(search_url) as request:
    response = json.loads(request.read())
    print(response.keys())
    print(response['_embedded']['stash:datasets'][39])
    # Iterate over the returned items
    # for item in response['_embedded']['stash:datasets']:
    #     link = item['identifier'].replace('doi:', 'https://doi.org/')
    #     title = item['title']
    #     count += 1
    #     print('----')
    #     print(f'Title: {title}')
    #     print(f'Link:  {link}')

print(count)