import json
import sys

facelogin = '{"verified": false, "distance": 0.9028533205506547, "threshold": 0.68, "model": "VGG-Face", "detector_backend": "opencv", "similarity_metric": "cosine", "facial_areas": {"img1": {"x": 404, "y": 109, "w": 449, "h": 449, "left_eye": [696, 308], "right_eye": [563, 266]}, "img2": {"x": 164, "y": 361, "w": 840, "h": 840, "left_eye": [714, 676], "right_eye": [419, 678]} }, "time": 3.98}'

person = '{"name": "Bob", "languages": ["English", "French"]}'

def readJsonDict(string):
    json_dict = json.loads(string)
    print(json_dict['verified'])
    
print(type(facelogin))
person_dict = json.loads(facelogin)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
dictkey = sys.argv[1]
try:
    dictkey2 = sys.argv[2]
except:
    dictkey2 = ''

if dictkey2 == "":
    print(person_dict[dictkey])
else:
    print(person_dict[dictkey][dictkey2])

#print(person_dict['facial_areas']['img1'])

# Output: ['English', 'French']
#print(person_dict['languages'])