import json
    
# read file
with open('../Downloads/stories_encoded.json', 'r') as f:
    data=f.read()

# parse file
data = json.loads(data)

profile_urls = []
for e in data:
    profile_urls.append(e['linkOfAuthorProfile'])