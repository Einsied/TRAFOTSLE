def connect(Topics, Concepts, Particles, Items, Notes):
	uncontainedItems = []
	for ItemId in sorted(Items.keys()):
		if (len(Items[ItemId]["Particles"]) == 0):
			uncontainedItems.append(ItemId)
	uncontainedNotes = []
	for NoteId in sorted(Notes.keys()):
		if (len(Notes[NoteId]["Particles"]) == 0):
			uncontainedNotes.append(NoteId)
	# Prepare particles
	for particleId in Particles.keys():
		Particles[particleId] = {
			"content": Particles[particleId],
			"Concepts": [],
			"Topics": []
		}
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
