import requests
import os
import shutil


API_URL = "https://api-inference.huggingface.co/models/umm-maybe/AI-image-detector"
headers = {"Authorization": "Bearer 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"}

def getallfiles(sourcedir):
    """retruns Lists of all files in the specified directory."""
    my_list =[]
    for filename in os.listdir(sourcedir):
        filepath = os.path.join(sourcedir, filename)
        if filepath.startswith('.'):
            continue
        my_list.append(filepath)

    return my_list


def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()


sourcefolder='/Users/parthgaba/Desktop/Twitter/twitter_data/images 2/'

destinationfolder='/Users/parthgaba/Desktop/Twitter/twitter_data/AI-Generated-Images/'


sourceimage_list=getallfiles(sourcefolder)

all_artificial= []

for sourceimage in sourceimage_list:
    
    output = query(sourceimage)

    print(output)

    #if isinstance(output, list):
    for item in output:
        if isinstance(item, dict):  # Ensure item is a dictionary
            print(item["label"], item["score"])
            if item["label"] == 'artificial':
                print(item["label"], item["score"])
                if float(item["score"]) > 0.85:  # Use float instead of int for score comparison
                    print(item["label"], item["score"])
                    all_artificial.append(sourceimage)
                    shutil.copy(sourceimage, destinationfolder)


print("......................................................")    
print(len(all_artificial))
print("......................................................")
print(all_artificial)
print("......................................................")

