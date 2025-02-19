import json


def JsonSerialize(data, sFile):
    with open(sFile, "w") as write_file:
        json.dump(data, write_file,indent=(len(data)+1))

def JsonDeserialize(sFile):
    with open(sFile, "r") as read_file:
        return json.load(read_file)