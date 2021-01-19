def connect(Topics, Concepts, Particles, Items, Notes):
	# Prepare Items and Notes
	for ItemId in sorted(Items.keys()):
		Items[ItemId]["Particles"] = []
	for NoteId in sorted(Notes.keys()):
		Notes[NoteId]["Particles"] = []
	# Process particles
	uncontainedItems = set(Items.keys())
	uncontainedNotes = set(Notes.keys())
	for particleId in Particles.keys():
		Particles[particleId]["Concepts"] = []
		Particles[particleId]["Topics"] = []
		SourceId = Particles[particleId]["SourceId"]
		if(SourceId in Items.keys()):
			Items[SourceId]["Particles"].append(SourceId)
			uncontainedItems -= set(SourceId)
		elif(SourceId in Notes.keys()):
			Notes[SourceId]["Particles"].append(SourceId)
			uncontainedNotes -= set(SourceId)
		elif(SourceId != "None"):
			print("SourceId: {SourceId:} unknown".format(
				SourceId = SourceId
			))
	# Prepare Concepts
	for conceptId in Concepts.keys():
		Concepts[conceptId]["Topics"] = []
	# First mark all
	uncontainedParticles = set(Particles.keys())
	uncontainedConcepts = set(Concepts.keys())
	# Start to eliminate the found ones
	foundConcepts = []
	foundParticles = []
	for ConceptId in Concepts.keys():
		foundParticles += Concepts[ConceptId]["Particles"]
		for ParticleId in Concepts[ConceptId]["Particles"]:
			if ConceptId not in Particles[ParticleId]["Concepts"]:
				Particles[ParticlId]["Concepts"].append(ConceptId)
	for TopicId in Topics.keys():
		Topic = Topics[TopicId]
		foundConcepts += Topic ["Concepts"]
		for ConceptId in Topic["Concepts"]:
			if TopicId not in Concepts[ConceptId]["Topics"]:
				Concepts[ConceptId]["Topics"].append(TopicID)
		foundParticles += Topic["Particles"]
		for ParticleId in Topic["Particles"]:
			if TopicId not in Particles[ParticleId]["Topics"]:
				Particles[ParticleId]["Topics"].append(TopicId)
	uncontainedParticles -= set(foundParticles)
	uncontainedConcepts -= set(foundConcepts)
	return {
		"uncontainedItems": uncontainedItems,
		"uncontainedNotes": uncontainedNotes,
		"uncontainedParticles": sorted(list(uncontainedParticles)),
		"uncontainedConcepts": sorted(list(uncontainedConcepts))
	}
