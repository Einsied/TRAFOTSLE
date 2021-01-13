import os
from python import CreateImageIndex
from python import ReadParticles
from python import ReadAnalogItems
from python import CreateHtmlNotes

jsonFileName = CreateImageIndex.CreateIndex("./analog_notes/")
Particles = ReadParticles.Read("./particles/")
Items = ReadAnalogItems.Read("./analog_notes/NewIndex.json", "./analog_notes/OldIndex.json", jsonFileName)
CreateHtmlNotes.CreateNotes("./htmlNotes/", Items, Particles)
