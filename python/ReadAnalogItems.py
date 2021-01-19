import os
import json

def reformParagraph(lineList):
	paragraph = ""
	for line in lineList:
		paragraph += " " + line.strip()
	return paragraph.strip()

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
			Items[Item["Id"]]["Description"] = reformParagraph(
				Item["Description"]
			)
			Items[Item["Id"]]["Old"] = False
	with open(ImageItemFile, "r") as ItemFile:
		NewItems = json.load(ItemFile)
		for Item in NewItems["Items"]:
			if Item["Id"] not in Items:
				print("{Id:} not found in items.".format(Id = Item["Id"]))
			else:
				Items[Item["Id"]]["Images"] = Item["Images"]
	return Items 
