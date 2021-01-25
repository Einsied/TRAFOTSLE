import os
import json

def Read(TopicFolder):
	TopicFiles = os.listdir(TopicFolder)
	Topics= {}

	for TopicFile in TopicFiles:
		with open(TopicFolder + TopicFile, "r") as topicFile:
			try:
				topic = json.load(topicFile)
			except ValueError:
				print("Error while reading {TopicFile:}".format(
					TopicFile = TopicFile
				))
				raise
			Topics[topic["Id"]] = {
				"Name": topic["Name"],
				"Particles": topic["Particles"],
				"Concepts": topic["Concepts"]
			}
	return Topics
