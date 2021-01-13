import os
import json

def Read(NewItemFile, OldItemFile, ImageItemFile):
	Items = {}
	with open(OldItemFile, "r") as ItemFile:
		OldItems = json.load(ItemFile)
		for Item in OldItems["Items"]:
			Items[Item["Id"]] = {
				"Description": Item["Description"],
				"Keywords": Item["Keywords"],
				"Old": True,
				"Particles": []
			}
	with open(NewItemFile, "r") as ItemFile:
		NewItems = json.load(ItemFile)
		for Item in NewItems["Items"]:
			Items[Item["Id"]] = {
				"Description": Item["Description"],
				"Old": False,
				"Particles": Item["Particles"]
			}
	with open(ImageItemFile, "r") as ItemFile:
		NewItems = json.load(ItemFile)
		for Item in NewItems["Items"]:
			if Item["Id"] not in Items:
				print("{Id:} not found in items.".format(Id = Item["Id"]))
			else:
				Items[Item["Id"]]["Images"] = Item["Images"]
	return Items 
