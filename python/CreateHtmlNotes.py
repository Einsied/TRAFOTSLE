import os

ItemFolder = "./html/Items"
ParticleFolder = "./html/Particles"
NotesFolder = "./html/Notes"
ConceptFolder = "./html/concepts"
TopicFolder = "./html/topics"

def GenerateFolder(Folder):
	if not os.path.exists(Folder):
		os.mkdir(Folder)
	return

def indentedNewLine(content, indentationDepth = 0):
	return "\t" * indentationDepth + content

def htmlFile(title, content):
	htmlIndentation = 0
	htmlStr = indentedNewLine("<!DOCTYPE html>", htmlIndentation)
	htmlStr += "\n" + indentedNewLine("<html>", htmlIndentation)
	htmlIndentation += 1
	# Header
	htmlStr += "\n" + indentedNewLine("<head>", htmlIndentation)
	htmlIndentation += 1
	htmlStr += "\n" + indentedNewLine("<meta charset=\"utf-8\" />", 
		htmlIndentation
	)
	htmlStr += "\n" + indentedNewLine(
		"<meta name=\"viewport\" content=\"decivce-width, initial-scale=1.0\"/>", 
		htmlIndentation
	)
	htmlStr += "\n" + indentedNewLine(
		"<title>{title}</title>".format(title = title), htmlIndentation
	)
	htmlIndentation -= 1
	htmlStr += "\n" + indentedNewLine("</head>", htmlIndentation)
	# Body
	htmlStr += "\n" + indentedNewLine("<body>", htmlIndentation)
	htmlIndentation += 1
	htmlStr += "\n" + indentedNewLine(content)
	htmlIndentation -= 1
	htmlStr += "\n" + indentedNewLine("</body>", htmlIndentation)
	htmlIndentation -= 1
	htmlStr += "\n" + indentedNewLine("</html>", htmlIndentation)
	return htmlStr

def CreateNavbar(Root, htmlIndentation):
	def addNavEntry(Name, PathToIndex, htmlIndentation):
		htmlStr = indentedNewLine("<li>", 0)
		htmlIndentation += 1
		htmlStr += "\n" + indentedNewLine(
			"<a href=\"{IndexPath:}\">".format(
				IndexPath = Root + PathToIndex + "/Index.html"
			), htmlIndentation
		)
		htmlIndentation += 1
		htmlStr += "\n" + indentedNewLine(Name, htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</a>", htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</li>", htmlIndentation)
		return htmlStr
	htmlStr = "\n" + indentedNewLine("<nav>", htmlIndentation)
	htmlIndentation += 1
	htmlStr += "\n" + indentedNewLine("<h2>Navigation</h2>", htmlIndentation)
	htmlStr += "\n" + indentedNewLine("<ul>", htmlIndentation)
	htmlIndentation += 1
	htmlStr += "\n" + indentedNewLine(
		addNavEntry("Items", ItemFolder, htmlIndentation), htmlIndentation
	)
	htmlStr += "\n" + indentedNewLine(
		addNavEntry("Particles", ParticleFolder, htmlIndentation), htmlIndentation
	)
	htmlStr += "\n" + indentedNewLine(
		addNavEntry("Notes", NotesFolder, htmlIndentation), htmlIndentation
	)
	htmlIndentation -= 1
	htmlStr += "\n" + indentedNewLine("</ul>", htmlIndentation)
	htmlIndentation -= 1
	htmlStr += "\n" + indentedNewLine("</nav>", htmlIndentation)
	return htmlStr

def CreateItems(Items):
	def CreateItemPage(Id, Item):
		# Indentation inherited from html file
		htmlIndentation = 2
		htmlStr = indentedNewLine("<main>", htmlIndentation)
		htmlIndentation += 1
		htmlStr = indentedNewLine(CreateNavbar("../../", htmlIndentation), htmlIndentation)
		htmlStr += "\n" + indentedNewLine(
			"<h1 class=\"ItemTitle\">{Title:}</h1>".format(Title = Id),
			htmlIndentation
		)
		htmlStr += "\n" + indentedNewLine("<h2>Content:</h2>".format(Title = Id),
			htmlIndentation
		)
		htmlStr += "\n" + indentedNewLine("<section class=\"ItemDescription\">",
			htmlIndentation
		)
		htmlIndentation += 1
		htmlStr += "\n" + indentedNewLine("<p>", htmlIndentation)
		htmlIndentation += 1
		htmlStr += "\n" + indentedNewLine(Item["Description"], htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</p>", htmlIndentation)
		htmlStr += "\n" + indentedNewLine("<h2>Keywords:</h2>".format(Title = Id),
			htmlIndentation
		)
		htmlStr += "\n" + indentedNewLine("<ul>", htmlIndentation)
		htmlIndentation += 1
		for keyword in Item["Keywords"]:
			htmlStr += "\n" + indentedNewLine("<li>", htmlIndentation)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine(keyword, htmlIndentation)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</li>", htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</ul>", htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</section>", htmlIndentation)
		htmlStr += "\n" + indentedNewLine("<section class=\"ItemMeta\">",
			htmlIndentation
		)
		htmlStr += "\n" + indentedNewLine("<h2>Spawned Particles:</h2>", htmlIndentation)
		htmlStr += "\n" + indentedNewLine("<ul>", htmlIndentation)
		htmlIndentation += 1
		for particle in Item["Particles"]:
			htmlStr += "\n" + indentedNewLine("<li>", htmlIndentation)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine(
				"<a href=\"../../{particlePath:}\">".format(
					particlePath = ParticleFolder + "/" + particle + ".html"
				), htmlIndentation
			)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine(particle, htmlIndentation)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</a>", htmlIndentation)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</li>", htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</ul>", htmlIndentation)
		htmlStr += "\n" + indentedNewLine("<h2>Original Item</h2>", htmlIndentation)
		for Image in Item["Images"]:
			htmlStr += "\n" + indentedNewLine(
				"<img class=\"ItemScan\" "
				+ "src=\"../../analog_notes/{ImagePath:}\"".format(
					ImagePath = Id + "/" + Image
				)
				+ "alt=\"Scan of {Id:}\"".format(Id=Id),
				htmlIndentation
			)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</section>", htmlIndentation)
		htmlIndentation += 1
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</main>", htmlIndentation)
		return htmlStr
	def CreateIndex(Items):
		# Indentation inherited from html file
		htmlIndentation = 2
		htmlStr = indentedNewLine("<main>", htmlIndentation)
		htmlIndentation += 1
		htmlStr = indentedNewLine(CreateNavbar("../../", htmlIndentation), htmlIndentation)
		htmlStr += "\n" + indentedNewLine("<table>", htmlIndentation)
		htmlIndentation += 1
		htmlStr += "\n" + indentedNewLine("<tr>", htmlIndentation)
		htmlIndentation += 1
		htmlStr += "\n" + indentedNewLine("<th> ID </th>", htmlIndentation)
		htmlStr += "\n" + indentedNewLine("<th> Particles </th>", htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</tr>", htmlIndentation)
		for Id in sorted(Items.keys()):
			FileName = "./" + Id + ".html"
			htmlStr += "\n" + indentedNewLine("<tr>", htmlIndentation)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine("<td>", htmlIndentation)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine(
				"<a href=\"{FileName:}\">".format(FileName = FileName), 
				htmlIndentation
			)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine(Id, htmlIndentation)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</a>", htmlIndentation)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</td>", htmlIndentation)
			htmlStr += "\n" + indentedNewLine("<td>", htmlIndentation)
			htmlIndentation += 1
			for particle in Items[Id]["Particles"]:
				htmlStr += "\n" + indentedNewLine(
					"<a href=\"../../{particle:}.html\">".format(
						particle = ParticleFolder + "/" + particle
					), 
					htmlIndentation
				)
				htmlIndentation += 1
				htmlStr += "\n" + indentedNewLine(particle, htmlIndentation)
				htmlIndentation -= 1
				htmlStr += "\n" + indentedNewLine("</a>", htmlIndentation)
				htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</td>", htmlIndentation)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</tr>", htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</table>", htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</main>", htmlIndentation)
		return htmlStr
	GenerateFolder(ItemFolder)
	for Id in sorted(Items.keys()):
		FileName = ItemFolder + "/" + Id + ".html"
		with open (FileName, "w") as ItemFile:
			ItemFile.write(htmlFile(Id, CreateItemPage(Id, Items[Id])))
	IndexFileName = ItemFolder + "/Index.html"
	with open (IndexFileName, "w") as IndexFile:
		IndexFile.write(htmlFile("Index", CreateIndex(Items)))

def CreateParticles(Particles):
	GenerateFolder(ParticleFolder)
	def CreateParticlePage(Id, Particle):
		# Indentation inherited from html file
		htmlIndentation = 2
		htmlStr = indentedNewLine("<main>", htmlIndentation)
		htmlStr = indentedNewLine(CreateNavbar("../../", htmlIndentation), htmlIndentation)
		htmlIndentation += 1
		htmlStr += "\n" + indentedNewLine(
			"<h1 class=\"ParticleTitle\">{Title:}</h1>".format(Title = Id),
			htmlIndentation
		)
		htmlStr += "\n" + indentedNewLine("<h2>Content:</h2>".format(Title = Id),
			htmlIndentation
		)
		htmlStr += "\n" + indentedNewLine("<section class=\"ParticleContent\">",
			htmlIndentation
		)
		htmlIndentation += 1
		htmlStr += "\n" + indentedNewLine("<p>", htmlIndentation)
		htmlIndentation += 1
		print(Particle)
		htmlStr += "\n" + indentedNewLine(Particle["Content"], htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("<p>", htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</section>", htmlIndentation)
		htmlStr += "\n" + indentedNewLine("<section class=\"ParticleMeta\">",
			htmlIndentation
		)
		htmlIndentation += 1
		htmlStr += "\n" + indentedNewLine("<h2>Contained in:</h2>".format(Title = Id),
			htmlIndentation
		)
		htmlStr += "\n" + indentedNewLine("<ul>", htmlIndentation)
		htmlIndentation += 1
		htmlStr += "\n" + indentedNewLine("<li>", htmlIndentation)
		htmlIndentation += 1
		htmlStr += "\n" + indentedNewLine("Concepts:", htmlIndentation)
		htmlStr += "\n" + indentedNewLine("<ul>", htmlIndentation)
		htmlIndentation += 1
		for conceptId in Particle["Concepts"]:
			htmlStr += "\n" + indentedNewLine("<li>", htmlIndentation)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine(
				"<a href=\"../../{conceptPath:}\">".format(
					conceptPath = ConceptFolder + "/" + conceptId + ".html"
				), htmlIndentation
			)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine(conceptId, htmlIndentation)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</a>", htmlIndentation)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</li>", htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</ul>", htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</li>", htmlIndentation)
		htmlStr += "\n" + indentedNewLine("<li>", htmlIndentation)
		htmlIndentation += 1
		htmlStr += "\n" + indentedNewLine("Topics:", htmlIndentation)
		htmlStr += "\n" + indentedNewLine("<ul>", htmlIndentation)
		htmlIndentation += 1
		for TopicId in Particle["Topics"]:
			htmlStr += "\n" + indentedNewLine("<li>", htmlIndentation)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine(
				"<a href=\"../../{topicPath:}\">".format(
					topicPath = TopicFolder + "/" + TopicId + ".html"
				), htmlIndentation
			)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine(TopicId, htmlIndentation)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</a>", htmlIndentation)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</li>", htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</ul>", htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</li>", htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</ul>", htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</section>", htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</main>", htmlIndentation)
		return htmlStr
	def CreateIndex(Particles):
		# Indentation inherited from html file
		htmlIndentation = 2
		htmlStr = indentedNewLine("<main>", htmlIndentation)
		htmlStr = indentedNewLine(CreateNavbar("../../", htmlIndentation), htmlIndentation)
		htmlIndentation += 1
		htmlStr += "\n" + indentedNewLine("<table>", htmlIndentation)
		htmlIndentation += 1
		htmlStr += "\n" + indentedNewLine("<tr>", htmlIndentation)
		htmlIndentation += 1
		htmlStr += "\n" + indentedNewLine("<th> ID </th>", htmlIndentation)
		htmlStr += "\n" + indentedNewLine("<th> Contained in Topics </th>", htmlIndentation)
		htmlStr += "\n" + indentedNewLine("<th> Contained in Concepts </th>", htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</tr>", htmlIndentation)
		for Id in sorted(Particles.keys()):
			FileName = "./" + Id + ".html"
			htmlStr += "\n" + indentedNewLine("<tr>", htmlIndentation)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine("<td>", htmlIndentation)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine(
				"<a href=\"{FileName:}\">".format(FileName = FileName), 
				htmlIndentation
			)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine(Id, htmlIndentation)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</a>", htmlIndentation)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</td>", htmlIndentation)
			htmlStr += "\n" + indentedNewLine("<td>", htmlIndentation)
			htmlIndentation += 1
			for TopicId in Particles[Id]["Topics"]:
				htmlStr += "\n" + indentedNewLine(
					"<a href=\"{TopicPath:}\">".format(
						TopicPath= TopicFolder + "/" + TopicId + ".html"
					), htmlIndentation
				)
				htmlIndentation += 1
				htmlStr += "\n" + indentedNewLine(TopicId + " ", htmlIndentation)
				htmlIndentation -= 1
				htmlStr += "\n" + indentedNewLine("</a>", htmlIndentation)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</td>", htmlIndentation)
			htmlStr += "\n" + indentedNewLine("<td>", htmlIndentation)
			htmlIndentation += 1
			for ConceptId in Particles[Id]["Concepts"]:
				htmlStr += "\n" + indentedNewLine(
					"<a href=\"{ConceptPath:}\">".format(
						ConceptPath = ConceptFolder + "/" + ConceptId + ".html"),
					htmlIndentation
				)
				htmlIndentation += 1
				htmlStr += "\n" + indentedNewLine(ConceptId + " ", htmlIndentation)
				htmlIndentation -= 1
				htmlStr += "\n" + indentedNewLine("</a>", htmlIndentation)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</td>", htmlIndentation)

			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</tr>", htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</table>", htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</main>", htmlIndentation)
		return htmlStr
	for Id in sorted(Particles.keys()):
		FileName = ParticleFolder + "/" + Id + ".html"
		with open (FileName, "w") as ItemFile:
			ItemFile.write(htmlFile(Id, CreateParticlePage(Id, Particles[Id])))
	IndexFileName = ParticleFolder + "/Index.html"
	with open (IndexFileName, "w") as IndexFile:
		IndexFile.write(htmlFile("Index", CreateIndex(Particles)))

def CreateDigitalNotes(Notes):
	def CreateNotePage(Id, Note):
		# Indentation inherited from html filea
		htmlIndentation = 2
		htmlStr = indentedNewLine("<main>", htmlIndentation)
		htmlStr = indentedNewLine(CreateNavbar("../../", htmlIndentation), htmlIndentation)
		htmlIndentation += 1
		htmlStr += "\n" + indentedNewLine(
			"<h1 class=\"NoteTitle\">{Title:}</h1>".format(Title = Id),
			htmlIndentation
		)
		htmlStr += "\n" + indentedNewLine("<h2>Content:</h2>".format(Title = Id),
			htmlIndentation
		)
		htmlStr += "\n" + indentedNewLine("<section class=\"NoteDescription\">",
			htmlIndentation
		)
		htmlIndentation += 1
		htmlStr += "\n" + indentedNewLine("<p>", htmlIndentation)
		htmlIndentation += 1
		htmlStr += "\n" + indentedNewLine(Note["Description"], htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("<p>", htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</section>", htmlIndentation)
		htmlStr += "\n" + indentedNewLine("<section class=\"NoteMeta\">",
			htmlIndentation
		)
		htmlStr += "\n" + indentedNewLine("<h2>Spawned Particles:</h2>", htmlIndentation)
		htmlStr += "\n" + indentedNewLine("<ul>", htmlIndentation)
		htmlIndentation += 1
		for particle in Note["Particles"]:
			htmlStr += "\n" + indentedNewLine("<li>", htmlIndentation)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine(
				"<a href=\"../../{particleFile:}\">".format(
					particleFile = ParticleFolder + "/" + particle + ".html"
				), htmlIndentation
			)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine(particle, htmlIndentation)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</a>", htmlIndentation)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</li>", htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</ul>", htmlIndentation)
		htmlStr += "\n" + indentedNewLine("<h2>Original File</h2>", htmlIndentation)
		htmlStr += "\n" + indentedNewLine(
			"<a href=\"../../digital_notes/{File:}\">".format(File = Note["File"]), 
			htmlIndentation
		)
		htmlIndentation += 1
		htmlStr += "\n" + indentedNewLine(Note["File"], htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</a>", htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</section>", htmlIndentation)
		htmlIndentation += 1
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</main>", htmlIndentation)
		return htmlStr
	def CreateIndex(Notes):
		# Indentation inherited from html file
		htmlIndentation = 2
		htmlStr = indentedNewLine("<main>", htmlIndentation)
		htmlStr = indentedNewLine(CreateNavbar("../../", htmlIndentation), htmlIndentation)
		htmlIndentation += 1
		htmlStr += "\n" + indentedNewLine("<table>", htmlIndentation)
		htmlIndentation += 1
		htmlStr += "\n" + indentedNewLine("<tr>", htmlIndentation)
		htmlIndentation += 1
		htmlStr += "\n" + indentedNewLine("<th> ID </th>", htmlIndentation)
		htmlStr += "\n" + indentedNewLine("<th> Particles </th>", htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</tr>", htmlIndentation)
		for Id in sorted(Notes.keys()):
			FileName = "./" + Id + ".html"
			htmlStr += "\n" + indentedNewLine("<tr>", htmlIndentation)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine("<td>", htmlIndentation)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine(
				"<a href=\"{FileName:}\">".format(FileName = FileName), 
				htmlIndentation
			)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine(Id, htmlIndentation)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</a>", htmlIndentation)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</td>", htmlIndentation)
			htmlStr += "\n" + indentedNewLine("<td>", htmlIndentation)
			htmlIndentation += 1
			for particle in Notes[Id]["Particles"]:
				htmlStr += "\n" + indentedNewLine(
					"<a href=\"../../{particle:}.html\">".format(
						particle = ParticleFolder + "/" + particle
					), 
					htmlIndentation
				)
				htmlIndentation += 1
				htmlStr += "\n" + indentedNewLine(particle, htmlIndentation)
				htmlIndentation -= 1
				htmlStr += "\n" + indentedNewLine("</a>", htmlIndentation)
				htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</td>", htmlIndentation)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</tr>", htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</table>", htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</main>", htmlIndentation)
		return htmlStr
	GenerateFolder(NotesFolder)
	for Id in sorted(Notes.keys()):
		FileName = NotesFolder + "/" + Id + ".html"
		with open (FileName, "w") as ItemFile:
			ItemFile.write(htmlFile(Id, CreateNotePage(Id, Notes[Id])))
	IndexFileName = NotesFolder + "/Index.html"
	with open (IndexFileName, "w") as IndexFile:
		IndexFile.write(htmlFile("Index", CreateIndex(Notes)))

def CreateConcepts(Concepts, Particles):
	print("TODO: Concepts")
	print(Concepts)
	print()

def CreateTopics(Topics, Particles):
	print("TODO: Topics")
	print(Topics)
	print()

def CreateUncontained(Uncontained):
	print("TODO: Uncontained")
	print(Uncontained)
	print()

def CreateNotes(
	HtmlFolder, Items, Notes, Particles, Concepts, Topics, Uncontained
):
	GenerateFolder(HtmlFolder)
	global ItemFolder, ParticleFolder, NotesFolder 
	ItemFolder = HtmlFolder + "/Items"
	ParticleFolder = HtmlFolder + "/Particles"
	NotesFolder = HtmlFolder + "/Notes"
	CreateItems(Items)
	CreateDigitalNotes(Notes)
	CreateParticles(Particles)
	CreateConcepts(Concepts, Particles)
	CreateTopics(Topics, Particles)
	CreateUncontained(Uncontained)
	print("TODO: CreateCSV")
