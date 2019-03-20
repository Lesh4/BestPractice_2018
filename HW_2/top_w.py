""" This program check 5 .json files and find the top of words """
from zipfile import ZipFile
import string
import json
import os

FOLDER = "JsonFolder"
TOP = {}
WORDS_TOP = []
for file in os.listdir():
    if file.endswith(".zip"):
        file_zip = file
        if not os.path.exists(FOLDER):
            os.makedirs(FOLDER)
        file_json = ZipFile(file_zip)
        file_json.extractall(FOLDER)
        file_json.close()

for file in os.listdir(FOLDER):
    file_name = "/JsonFolder/" + file
    with open(file_name, "r") as data:
        for line in data:
            line = json.loads(line)
            letter = line["body"].translate(
                str.maketrans('', '', string.punctuation))
            if letter != "deleted":
                letter = letter.lower()
            words = letter.split()
            for word in words:
                if word not in TOP.keys():
                    TOP[word] = 1
                else:
                    TOP[word] += 1

for key, val in list(TOP.items()):
    if len(key) > 3:
        WORDS_TOP.append((val, key))

WORDS_TOP.sort(reverse=True)

with open("TOP.json", "w") as end_file:
    json.dump(WORDS_TOP[:20], end_file)
