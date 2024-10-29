import requests
from collections import Counter

ACCESS_TOKEN = '5lRvVDSnCTTXgdFWLuCN7HLAK2UWKjUbJwPCEiWJxirzVT3VfLsAeHnhflmt'
search_query = 'creators.affiliation:(+university +alabama +birmingham)'

response = requests.get('https://zenodo.org/api/records/',
                        params={'q': search_query,
                                'access_token': ACCESS_TOKEN,
                                'size': 128,
                                'type' : 'dataset'
                                })

records = response.json()

results = []
record_ids = []

for i in range(len(records['hits']['hits'])):
    c = []
    contributors = ''
    
    record_id = records['hits']['hits'][i]['id']
    record_ids.append(record_id)
    if 'resource_type' in records['hits']['hits'][i]['metadata']:
        resource_type = records['hits']['hits'][i]['metadata']['resource_type']['title']
    else:
        resource_type = "none"
    if 'title' in records['hits']['hits'][i]['metadata']:
        title = records['hits']['hits'][i]['metadata']['title']
    else:
        title = "none"
    if 'contributors' in records['hits']['hits'][i]['metadata']:
        for j in range(len(records['hits']['hits'][i]['metadata']['contributors'])):
            c.append(records['hits']['hits'][i]['metadata']['contributors'][j]['type']) 
        
        contributor_counts = Counter(c)
        
        count = 0
        for contrib in contributor_counts.keys():
            if (count > 0):
                contributors += ','
            contributors += contrib + "=" + str(contributor_counts[contrib])
            count += 1
    else:    
        contributors = 'none'
    
    results.append([record_id,title,resource_type,contributors])

print(record_ids)