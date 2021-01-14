import os
from python import CreateImageIndex
from python import ReadParticles
from python import ReadAnalogItems
from python import ReadDigitalNotes
from python import CreateHtmlNotes

jsonFileName = CreateImageIndex.CreateIndex("./analog_notes/")
Particles = ReadParticles.Read("./particles/")
Items = ReadAnalogItems.Read("./analog_notes/NewIndex.json", "./analog_notes/OldIndex.json", jsonFileName)
Notes = ReadDigitalNotes.Read("./digital_notes/Index.json")
CreateHtmlNotes.CreateNotes("./html", Items, Particles, Notes)
