# Python3 code to demonstrate working of 
# Append items at beginning of dictionary 
# Using update()

# initializing dictionary
test_dict = {
	"verified": 'false',
    "distance": 0.9028533205506547,
    "threshold": 0.68, 
    "model": "VGG-Face",
    "detector_backend": "opencv",
    "similarity_metric": "cosine",
    "facial_areas": '{"img1": {"x": 404, "y": 109, "w": 449, "h": 449, "left_eye": [696, 308], "right_eye": [563, 266]}, "img2": {"x": 164, "y": 361, "w": 840, "h": 840, "left_eye": [714, 676], "right_eye": [419, 678]}}',
    "time": 3.77}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing update dictionary
updict = {"files" : "resultados/atual.jpg-mulher2.jpg.json"}

# update() on new dictionary to get desired order
updict.update(test_dict)

# printing result 
print("The required dictionary : " + str(updict)) 
