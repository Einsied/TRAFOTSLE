import os
from python import CreateImageIndex
from python import ReadParticles
from python import ReadConcepts
from python import ReadTopics
from python import ReadAnalogItems
from python import ReadDigitalNotes
from python import Connect
from python import CreateHtmlNotes

jsonFileName = CreateImageIndex.CreateIndex("./analog_notes/")
Items = ReadAnalogItems.Read("./analog_notes/NewIndex.json", "./analog_notes/OldIndex.json", jsonFileName)
Notes = ReadDigitalNotes.Read("./digital_notes/Index.json")
Particles = ReadParticles.Read("./particles/")
Concepts = ReadConcepts.Read("./concepts/")
Topics = ReadTopics.Read("./topics/")
Uncontained = Connect.connect(Topics, Concepts, Particles, Items, Notes)
CreateHtmlNotes.HtmlNotes("./html").CreateNotes(
	Items, Notes, Particles, Concepts, Topics, Uncontained
)
