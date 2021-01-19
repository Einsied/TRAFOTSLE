import os
import json

def Read(TopicFolder):
	TopicFiles = os.listdir(TopicFolder)
	Topics= {}

	for TopicFile in TopicFiles:
		with open(TopicFolder + TopicFile, "r") as topicFile:
			topic = json.load(topicFile)
			Topics[topic["Id"]] = {
				"Name": topic["Name"],
				"Particles": topic["Particles"],
				"Concepts": topic["Concepts"]
			}
	return Topics
