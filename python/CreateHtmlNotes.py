import os

def GenerateFolder(Folder):
	if not os.path.exists(Folder):
		os.mkdir(Folder)
	return

def indentedNewLine(content, indentationDepth = 0):
	return "\t" * indentationDepth + content

class HtmlNotes:
	def __init__(self, HtmlFolder):
		self.HtmlFolder     = HtmlFolder
		self.ItemFolder     = self.HtmlFolder + "/Items"
		self.ParticleFolder = self.HtmlFolder + "/Particles"
		self.NotesFolder    = self.HtmlFolder + "/Notes"
		self.ConceptFolder  = self.HtmlFolder + "/Concepts"
		self.TopicFolder    = self.HtmlFolder + "/Topics"

	def CreateCssFile(self):
		def addCssAttribute(name, value):
			return "\n\t{name:}:{value:};".format(name = name, value = value)
		def addCssClass(name, attributeList):
			classString = ".{name:}{{".format(name = name)
			for attribute in attributeList:
				classString += addCssAttribute(
					attribute["Name"], attribute["Value"]
				)
			classString += "\n}"
			return classString
		# Particle
		cssString = addCssClass("ParticleTitle", [])
		cssString += addCssClass("ParticleContent", [])
		cssString += addCssClass("ParticleMeta", [])
		# Item 
		cssString += addCssClass("ItemTitle", [])
		cssString += addCssClass("ItemDescription", [])
		cssString += addCssClass("ItemMeta", [])
		cssString += addCssClass("ItemScan", [
			{"Name": "max-width", "Value":"45%"}
		])
		# Note
		cssString += addCssClass("NoteTitle", [])
		cssString += addCssClass("NoteDescription", [])
		cssString += addCssClass("NoteMeta", [])
		# Concept
		cssString += addCssClass("ConceptTitle", [])
		cssString += addCssClass("ConceptDescription", [])
		cssString += addCssClass("ConceptParticles", [])
		# Topic
		cssString += addCssClass("TopicTitle", [])
		cssString += addCssClass("TopicParticles", [])
		CssFileName = self.HtmlFolder + "/docu.css"
		with open (CssFileName, "w") as CssFile:
			CssFile.write(cssString)

	def CreateNavbar(self, Root, htmlIndentation):
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
		def addNavEntryUncontained(PathToIndex, htmlIndentation):
			htmlStr = indentedNewLine("<li>", htmlIndentation)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine(
				"<a href=\"{IndexPath:}\">".format(
					IndexPath = Root + PathToIndex + "/Uncontained.html"
				), htmlIndentation
			)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine("Uncontained Objects", htmlIndentation)
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
			addNavEntry("Items", self.ItemFolder, htmlIndentation), htmlIndentation
		)
		htmlStr += "\n" + indentedNewLine(
			addNavEntry("Particles", self.ParticleFolder, htmlIndentation), htmlIndentation
		)
		htmlStr += "\n" + indentedNewLine(
			addNavEntry("Notes", self.NotesFolder, htmlIndentation), htmlIndentation
		)
		htmlStr += "\n" + indentedNewLine(
			addNavEntry("Concepts", self.ConceptFolder, htmlIndentation), htmlIndentation
		)
		htmlStr += "\n" + indentedNewLine(
			addNavEntry("Topics", self.TopicFolder, htmlIndentation), htmlIndentation
		)
		htmlStr += "\n" + indentedNewLine(
			addNavEntryUncontained(self.HtmlFolder, htmlIndentation)
		)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</ul>", htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("</nav>", htmlIndentation)
		return htmlStr

	def htmlFile(self, title, content, Root):
		htmlIndentation = 0
		htmlStr = indentedNewLine("<!DOCTYPE html>", htmlIndentation)
		htmlStr += "\n" + indentedNewLine("<html>", htmlIndentation)
		htmlIndentation += 1
		# Header
		htmlStr += "\n" + indentedNewLine("<head>", htmlIndentation)
		htmlIndentation += 1
		htmlStr += "\n" + indentedNewLine(
			"<link rel=\"stylesheet\" href=\"{Root:}/docu.css\" />".format(
				Root = Root + self.HtmlFolder 
			),htmlIndentation
		)
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

	def CreateItems(self, Items):
		def CreateItemPage(Id, Item):
			# Indentation inherited from html file
			htmlIndentation = 2
			htmlStr = indentedNewLine("<main>", htmlIndentation)
			htmlIndentation += 1
			htmlStr += indentedNewLine(self.CreateNavbar("../../", htmlIndentation), htmlIndentation)
			htmlStr += "\n" + indentedNewLine(
				"<h1 class=\"ItemTitle\">{Title:}</h1>".format(Title = Id),
				htmlIndentation
			)
			htmlStr += "\n" + indentedNewLine("<section class=\"ItemDescription\">",
				htmlIndentation
			)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine("<h2>Content:</h2>".format(Title = Id),
				htmlIndentation
			)
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
			htmlIndentation += 1
			if(len(Item["Particles"]) > 0):
				htmlStr += "\n" + indentedNewLine("<h2>Spawned Particles:</h2>", htmlIndentation)
				htmlStr += "\n" + indentedNewLine("<ul>", htmlIndentation)
				htmlIndentation += 1
				for particle in sorted(Item["Particles"]):
					htmlStr += "\n" + indentedNewLine("<li>", htmlIndentation)
					htmlIndentation += 1
					htmlStr += "\n" + indentedNewLine(
						"<a href=\"../../{particlePath:}\">".format(
							particlePath = self.ParticleFolder + "/" + particle + ".html"
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
			for Image in sorted(Item["Images"]):
				htmlStr += "\n" + indentedNewLine(
					"<img class=\"ItemScan\" "
					+ "src=\"../../analog_notes/{ImagePath:}\"".format(
						ImagePath = Id + "/" + Image
					)
					+ " alt=\"Scan of {Id:}\" />".format(Id=Id),
					htmlIndentation
				)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</section>", htmlIndentation)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</main>", htmlIndentation)
			return htmlStr
		def CreateIndex(Items):
			# Indentation inherited from html file
			htmlIndentation = 2
			htmlStr = indentedNewLine("<main>", htmlIndentation)
			htmlIndentation += 1
			htmlStr += indentedNewLine(self.CreateNavbar("../../", htmlIndentation), htmlIndentation)
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
				for particle in sorted(Items[Id]["Particles"]):
					htmlStr += "\n" + indentedNewLine(
						"<a href=\"../../{particle:}.html\">".format(
							particle = self.ParticleFolder + "/" + particle
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
		GenerateFolder(self.ItemFolder)
		for Id in sorted(Items.keys()):
			FileName = self.ItemFolder + "/" + Id + ".html"
			with open (FileName, "w") as ItemFile:
				ItemFile.write(self.htmlFile(Id, CreateItemPage(Id, Items[Id]), 
					"../../")
				)
		IndexFileName = self.ItemFolder + "/Index.html"
		with open (IndexFileName, "w") as IndexFile:
			IndexFile.write(self.htmlFile("Index", CreateIndex(Items), "../../"))

	def CreateParticles(self, Particles):
		GenerateFolder(self.ParticleFolder)
		def CreateParticlePage(Id, Particle):
			# Indentation inherited from html file
			htmlIndentation = 2
			htmlStr = indentedNewLine("<main>", htmlIndentation)
			htmlIndentation += 1
			htmlStr += indentedNewLine(self.CreateNavbar("../../", htmlIndentation), htmlIndentation)
			htmlStr += "\n" + indentedNewLine(
				"<h1 class=\"ParticleTitle\">{Title:}</h1>".format(Title = Id),
				htmlIndentation
			)
			htmlStr += "\n" + indentedNewLine("<section class=\"ParticleContent\">",
				htmlIndentation
			)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine("<h2>Content:</h2>".format(Title = Id),
				htmlIndentation
			)
			htmlStr += "\n" + indentedNewLine("<p>", htmlIndentation)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine(Particle["Content"], htmlIndentation)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("<p>", htmlIndentation)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</section>", htmlIndentation)
			htmlStr += "\n" + indentedNewLine("<section class=\"ParticleMeta\">",
				htmlIndentation
			)
			htmlIndentation += 1
			if (Particle["SourceId"] != None):
				htmlStr += "\n" + indentedNewLine("<h2>Spawned by:</h2>".format(Title = Id),
					htmlIndentation
				)
				Folder = ""
				if Particle["SourceId"][0] == "I":
					Folder = self.ItemFolder
				if Particle["SourceId"][0] == "N":
					Folder = NotesFolder
				htmlStr += "\n" + indentedNewLine(
					"<a href=\"../../{Path:}\">".format(
						Path = Folder + "/" + Particle["SourceId"] + ".html"
					), htmlIndentation
				)
				htmlIndentation += 1
				htmlStr += "\n" + indentedNewLine(Particle["SourceId"], htmlIndentation)
				htmlIndentation -= 1
				htmlStr += "\n" + indentedNewLine("</a>", htmlIndentation)
			if(len(Particle["Concepts"]) > 0 or len(Particle["Topics"])):
				htmlStr += "\n" + indentedNewLine("<h2>Contained in:</h2>".format(
					Title = Id), htmlIndentation
				)
				htmlStr += "\n" + indentedNewLine("<ul>", htmlIndentation)
				htmlIndentation += 1
				if(len(Particle["Concepts"]) > 0):
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
								conceptPath = self.ConceptFolder + "/" + conceptId + ".html"
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
				if(len(Particle["Topics"]) > 0):
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
								topicPath = self.TopicFolder + "/" + TopicId + ".html"
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
			htmlIndentation += 1
			htmlStr += indentedNewLine(self.CreateNavbar("../../", htmlIndentation), htmlIndentation)
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
				for TopicId in sorted(Particles[Id]["Topics"]):
					htmlStr += "\n" + indentedNewLine(
						"<a href=\"{TopicPath:}\">".format(
							TopicPath =(
								"../../" + self.TopicFolder + "/" + TopicId + ".html"
							)
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
				for ConceptId in sorted(Particles[Id]["Concepts"]):
					htmlStr += "\n" + indentedNewLine(
						"<a href=\"{ConceptPath:}\">".format(
							ConceptPath = self.ConceptFolder + "/" + ConceptId + ".html"),
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
			FileName = self.ParticleFolder + "/" + Id + ".html"
			with open (FileName, "w") as ItemFile:
				ItemFile.write(self.htmlFile(Id, CreateParticlePage(Id, Particles[Id]),
					"../../"
				))
		IndexFileName = self.ParticleFolder + "/Index.html"
		with open (IndexFileName, "w") as IndexFile:
			IndexFile.write(self.htmlFile("Index", CreateIndex(Particles), "../../"))

	def CreateDigitalNotes(self, Notes):
		def CreateNotePage(Id, Note):
			# Indentation inherited from html filea
			htmlIndentation = 2
			htmlStr = indentedNewLine("<main>", htmlIndentation)
			htmlIndentation += 1
			htmlStr += indentedNewLine(self.CreateNavbar("../../", htmlIndentation), htmlIndentation)
			htmlStr += "\n" + indentedNewLine(
				"<h1 class=\"NoteTitle\">{Title:}</h1>".format(Title = Id),
				htmlIndentation
			)
			htmlStr += "\n" + indentedNewLine("<section class=\"NoteDescription\">",
				htmlIndentation
			)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine("<h2>Content:</h2>".format(Title = Id),
				htmlIndentation
			)
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
			htmlIndentation += 1
			if(len(Note["Particles"]) > 0):
				htmlStr += "\n" + indentedNewLine("<h2>Spawned Particles:</h2>", htmlIndentation)
				htmlStr += "\n" + indentedNewLine("<ul>", htmlIndentation)
				htmlIndentation += 1
				for particle in sorted(Note["Particles"]):
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
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</main>", htmlIndentation)
			return htmlStr
		def CreateIndex(Notes):
			# Indentation inherited from html file
			htmlIndentation = 2
			htmlStr = indentedNewLine("<main>", htmlIndentation)
			htmlIndentation += 1
			htmlStr += indentedNewLine(self.CreateNavbar("../../", htmlIndentation), htmlIndentation)
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
				for particle in sorted(Notes[Id]["Particles"]):
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
		GenerateFolder(self.NotesFolder)
		for Id in sorted(Notes.keys()):
			FileName = self.NotesFolder + "/" + Id + ".html"
			with open (FileName, "w") as ItemFile:
				ItemFile.write(self.htmlFile(Id, CreateNotePage(Id, Notes[Id]),
					"../../"
				))
		IndexFileName = self.NotesFolder + "/Index.html"
		with open (IndexFileName, "w") as IndexFile:
			IndexFile.write(self.htmlFile("Index", CreateIndex(Notes),
				"../../"
			))

	def CreateConcepts(self, Concepts, Particles):
		def CreateConceptPage(Id, Concept):
			# Indentation inherited from html filea
			htmlIndentation = 2
			htmlStr = indentedNewLine("<main>", htmlIndentation)
			htmlIndentation += 1
			htmlStr += indentedNewLine(self.CreateNavbar("../../", htmlIndentation), htmlIndentation)
			htmlStr += "\n" + indentedNewLine(
				"<h1 class=\"ConceptTitle\">{Title:}</h1>".format(
					Title = Concept["Name"] + " ({Id:})".format(Id = Id)
				), htmlIndentation
			)
			htmlStr += "\n" + indentedNewLine("<section class=\"ConceptDescription\">",
				htmlIndentation
			)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine("<h2>Description:</h2>",
				htmlIndentation
			)
			for paragraph in Concept["Description"]:
				htmlStr += "\n" + indentedNewLine("<p>", htmlIndentation)
				htmlIndentation += 1
				htmlStr += "\n" + indentedNewLine(paragraph,
					htmlIndentation
				)
				htmlIndentation -= 1
				htmlStr += "\n" + indentedNewLine("</p>", htmlIndentation)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</section>", htmlIndentation)
			if(len(Concept["Particles"]) > 0):
				htmlStr += "\n" + indentedNewLine("<section class=\"ConceptParticles\">",
					htmlIndentation
				)
				htmlStr += "\n" + indentedNewLine("<h2>Particles:</h2>",
					htmlIndentation
				)
				htmlIndentation += 1
				for particle in Concept["Particles"]:
					FileName = "../../" + self.ParticleFolder + "/" + particle + ".html"
					htmlStr += "\n" + indentedNewLine("<h3>", htmlIndentation)
					htmlIndentation += 1
					htmlStr += "\n" + indentedNewLine(
						"<a href=\"{FileName:}\">".format(FileName = FileName), 
						htmlIndentation
					)
					htmlIndentation += 1
					htmlStr += "\n" + indentedNewLine(particle, htmlIndentation)
					htmlIndentation -= 1
					htmlStr += "\n" + indentedNewLine("</a>", htmlIndentation)
					htmlIndentation -= 1
					htmlStr += "\n" + indentedNewLine("</h3>", htmlIndentation)
					htmlStr += "\n" + indentedNewLine("<p>", htmlIndentation)
					htmlIndentation += 1
					htmlStr += "\n" + indentedNewLine(Particles[particle]["Content"],
						htmlIndentation
					)
					htmlIndentation -= 1
					htmlStr += "\n" + indentedNewLine("</p>", htmlIndentation)
				htmlIndentation -= 1
				htmlStr += "\n" + indentedNewLine("</section>", htmlIndentation)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</main>", htmlIndentation)
			return htmlStr
		def CreateIndex(Concepts):
			# Indentation inherited from html file
			htmlIndentation = 2
			htmlStr = indentedNewLine("<main>", htmlIndentation)
			htmlIndentation += 1
			htmlStr += indentedNewLine(self.CreateNavbar("../../", htmlIndentation), htmlIndentation)
			htmlStr += "\n" + indentedNewLine("<table>", htmlIndentation)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine("<tr>", htmlIndentation)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine("<th> ID </th>", htmlIndentation)
			htmlStr += "\n" + indentedNewLine("<th> Name </th>", htmlIndentation)
			htmlStr += "\n" + indentedNewLine("<th> Contained Particles </th>", htmlIndentation)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</tr>", htmlIndentation)
			for Id in sorted(Concepts.keys()):
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
				htmlStr += "\n" + indentedNewLine("{Name:}".format(
					Name = Concepts[Id]["Name"]
				), htmlIndentation)
				htmlIndentation -= 1
				htmlStr += "\n" + indentedNewLine("</td>", htmlIndentation)
				htmlStr += "\n" + indentedNewLine("<td>", htmlIndentation)
				htmlIndentation += 1
				for particle in sorted(Concepts[Id]["Particles"]):
					FileName = "../../" + self.ParticleFolder + "/" + particle + ".html"
					htmlStr += "\n" + indentedNewLine(
						"<a href=\"{FileName:}\">".format(FileName = FileName), 
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
		GenerateFolder(self.ConceptFolder)
		for Id in sorted(Concepts.keys()):
			FileName = self.ConceptFolder + "/" + Id + ".html"
			with open (FileName, "w") as ConceptFile:
				ConceptFile.write(self.htmlFile(Id, CreateConceptPage(Id, Concepts[Id]),
					"../../"
				))
		IndexFileName = self.ConceptFolder + "/Index.html"
		with open (IndexFileName, "w") as IndexFile:
			IndexFile.write(self.htmlFile("Index", CreateIndex(Concepts),
				"../../"
			))

	def CreateTopics(self, Topics, Particles):
		def CreateTopicPage(Id, Topic):
			# Indentation inherited from html filea
			htmlIndentation = 2
			htmlStr = indentedNewLine("<main>", htmlIndentation)
			htmlIndentation += 1
			htmlStr += indentedNewLine(self.CreateNavbar("../../", htmlIndentation), htmlIndentation)
			htmlStr += "\n" + indentedNewLine(
				"<h1 class=\"TopicTitle\">{Title:}</h1>".format(
				Title = Topic["Name"] + " ({Id:})".format(Id = Id)
				), htmlIndentation
			)
			htmlStr += "\n" + indentedNewLine("<section class=\"TopicParticles\">",
				htmlIndentation
			)
			htmlStr += "\n" + indentedNewLine("<h2>Particles:</h2>",
				htmlIndentation
			)
			htmlIndentation += 1
			for particle in sorted(Topic["Particles"]):
				FileName = "../../" + self.ParticleFolder + "/" + particle + ".html"
				htmlStr += "\n" + indentedNewLine("<h3>", htmlIndentation)
				htmlIndentation += 1
				htmlStr += "\n" + indentedNewLine(
					"<a href=\"{FileName:}\">".format(FileName = FileName), 
					htmlIndentation
				)
				htmlIndentation += 1
				htmlStr += "\n" + indentedNewLine(particle, htmlIndentation)
				htmlIndentation -= 1
				htmlStr += "\n" + indentedNewLine("</a>", htmlIndentation)
				htmlIndentation -= 1
				htmlStr += "\n" + indentedNewLine("</h3>", htmlIndentation)
				htmlStr += "\n" + indentedNewLine("<p>", htmlIndentation)
				htmlIndentation += 1
				htmlStr += "\n" + indentedNewLine(Particles[particle]["Content"],
					htmlIndentation
				)
				htmlIndentation -= 1
				htmlStr += "\n" + indentedNewLine("</p>", htmlIndentation)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</section>", htmlIndentation)
			if(len(Topic["Concepts"]) > 0):
				htmlStr += "\n" + indentedNewLine("<section class=\"TopicConcepts\">",
					htmlIndentation
				)
				htmlStr += "\n" + indentedNewLine("<h2>Concepts:</h2>",
					htmlIndentation
				)
				htmlStr += "\n" + indentedNewLine("<ul>", htmlIndentation)
				htmlIndentation += 1
				for concept in sorted(Topic["Concepts"],
					key = lambda concept: concept["Id"]
				):
					FileName = "../../" + self.ConceptFolder + "/" + concept["Id"] + ".html"
					htmlStr += "\n" + indentedNewLine("<li>", htmlIndentation)
					htmlIndentation += 1
					htmlStr += "\n" + indentedNewLine(
						"<a href=\"{FileName:}\">".format(FileName = FileName), 
						htmlIndentation
					)
					htmlIndentation += 1
					htmlStr += "\n" + indentedNewLine("{Id:}({Name:})".format(
						Id = concept["Id"],
						Name = concept["Name"]
					), htmlIndentation)
					htmlIndentation -= 1
					htmlStr += "\n" + indentedNewLine("</a>", htmlIndentation)
					htmlIndentation -= 1
					htmlStr += "\n" + indentedNewLine("</li>", htmlIndentation)
				htmlIndentation -= 1
				htmlStr += "\n" + indentedNewLine("</ul>", htmlIndentation)
				htmlIndentation -= 1
				htmlStr += "\n" + indentedNewLine("</section>", htmlIndentation)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</main>", htmlIndentation)
			return htmlStr
		def CreateIndex(Topics):
			# Indentation inherited from html file
			htmlIndentation = 2
			htmlStr = indentedNewLine("<main>", htmlIndentation)
			htmlIndentation += 1
			htmlStr += indentedNewLine(self.CreateNavbar("../../", htmlIndentation), htmlIndentation)
			htmlStr += "\n" + indentedNewLine("<table>", htmlIndentation)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine("<tr>", htmlIndentation)
			htmlIndentation += 1
			htmlStr += "\n" + indentedNewLine("<th> ID </th>", htmlIndentation)
			htmlStr += "\n" + indentedNewLine("<th> Name </th>", htmlIndentation)
			htmlStr += "\n" + indentedNewLine("<th> Contained Particles </th>", htmlIndentation)
			htmlStr += "\n" + indentedNewLine("<th> Contained Concepts </th>", htmlIndentation)
			htmlIndentation -= 1
			htmlStr += "\n" + indentedNewLine("</tr>", htmlIndentation)
			for Id in sorted(Topics.keys()):
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
				htmlStr += "\n" + indentedNewLine("{Name:}".format(
					Name = Topics[Id]["Name"]
				), htmlIndentation)
				htmlIndentation -= 1
				htmlStr += "\n" + indentedNewLine("</td>", htmlIndentation)
				htmlStr += "\n" + indentedNewLine("<td>", htmlIndentation)
				htmlIndentation += 1
				for particle in sorted(Topics[Id]["Particles"]):
					FileName = "../../" + self.ParticleFolder + "/" + particle + ".html"
					htmlStr += "\n" + indentedNewLine(
						"<a href=\"{FileName:}\">".format(FileName = FileName), 
						htmlIndentation
					)
					htmlIndentation += 1
					htmlStr += "\n" + indentedNewLine(particle, htmlIndentation)
					htmlIndentation -= 1
					htmlStr += "\n" + indentedNewLine("</a>", htmlIndentation)
				htmlIndentation -= 1
				htmlStr += "\n" + indentedNewLine("</td>", htmlIndentation)
				htmlStr += "\n" + indentedNewLine("<td>", htmlIndentation)
				htmlIndentation += 1
				for concept in sorted(Topics[Id]["Concepts"],
					key = lambda concept: concept["Id"]
				):
					FileName = "../../" + self.ConceptFolder + "/"
					FileName += concept["Id"] + ".html"
					htmlStr += "\n" + indentedNewLine(
						"<a href=\"{FileName:}\">".format(FileName = FileName), 
						htmlIndentation
					)
					htmlIndentation += 1
					htmlStr += "\n" + indentedNewLine(concept["Id"], htmlIndentation)
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
		GenerateFolder(self.TopicFolder)
		for Id in sorted(Topics.keys()):
			FileName = self.TopicFolder + "/" + Id + ".html"
			with open (FileName, "w") as TopicFile:
				TopicFile.write(self.htmlFile(Id, CreateTopicPage(Id, Topics[Id]),
					"../../"
				))
		IndexFileName = self.TopicFolder + "/Index.html"
		with open (IndexFileName, "w") as IndexFile:
			IndexFile.write(self.htmlFile("Index", CreateIndex(Topics), "../../"))

	def CreateUncontained(self, Uncontained):
		def CreateUncontainedPage():
			# Indentation inherited from html file
			htmlIndentation = 2
			htmlStr = indentedNewLine("<main>", htmlIndentation)
			htmlIndentation += 1
			htmlStr += indentedNewLine(self.CreateNavbar("../", htmlIndentation), htmlIndentation)
			if (len(Uncontained["uncontainedItems"]) > 0):
				htmlStr += indentedNewLine("<h2>Items</h2>", htmlIndentation)
				htmlStr += indentedNewLine("<ul>", htmlIndentation)
				htmlIndentation += 1
				for Item in sorted(Uncontained["uncontainedItems"]):
					FileName = "../" + self.ItemFolder + "/" + Item + ".html"
					htmlStr += indentedNewLine("<li>", htmlIndentation)
					htmlIndentation += 1
					htmlStr += "\n" + indentedNewLine(
						"<a href=\"{FileName:}\">".format(FileName = FileName), 
						htmlIndentation
					)
					htmlIndentation += 1
					htmlStr += "\n" + indentedNewLine(Item, htmlIndentation)
					htmlIndentation -= 1
					htmlStr += "\n" + indentedNewLine("</a>", htmlIndentation)
					htmlIndentation -= 1
					htmlStr += indentedNewLine("</li>", htmlIndentation)
				htmlIndentation -= 1
				htmlStr += indentedNewLine("</ul>", htmlIndentation)
			if (len(Uncontained["uncontainedNotes"]) > 0):
				htmlStr += indentedNewLine("<h2>Notes</h2>", htmlIndentation)
				htmlStr += indentedNewLine("<ul>", htmlIndentation)
				htmlIndentation += 1
				for Note in sorted(Uncontained["uncontainedNotes"]):
					FileName = "../" + self.NotesFolder + "/" + Note + ".html"
					htmlStr += indentedNewLine("<li>", htmlIndentation)
					htmlIndentation += 1
					htmlStr += "\n" + indentedNewLine(
						"<a href=\"{FileName:}\">".format(FileName = FileName), 
						htmlIndentation
					)
					htmlIndentation += 1
					htmlStr += "\n" + indentedNewLine(Note, htmlIndentation)
					htmlIndentation -= 1
					htmlStr += "\n" + indentedNewLine("</a>", htmlIndentation)
					htmlIndentation -= 1
					htmlStr += indentedNewLine("</li>", htmlIndentation)
				htmlIndentation -= 1
				htmlStr += indentedNewLine("</ul>", htmlIndentation)
			if (len(Uncontained["uncontainedParticles"]) > 0):
				htmlStr += indentedNewLine("<h2>Particles</h2>", htmlIndentation)
				htmlStr += indentedNewLine("<ul>", htmlIndentation)
				htmlIndentation += 1
				for Particle in sorted(Uncontained["uncontainedParticles"]):
					FileName = "../" + self.ParticleFolder + "/" + Particle + ".html"
					htmlStr += indentedNewLine("<li>", htmlIndentation)
					htmlIndentation += 1
					htmlStr += "\n" + indentedNewLine(
						"<a href=\"{FileName:}\">".format(FileName = FileName), 
						htmlIndentation
					)
					htmlIndentation += 1
					htmlStr += "\n" + indentedNewLine(Particle, htmlIndentation)
					htmlIndentation -= 1
					htmlStr += "\n" + indentedNewLine("</a>", htmlIndentation)
					htmlIndentation -= 1
					htmlStr += indentedNewLine("</li>", htmlIndentation)
				htmlIndentation -= 1
				htmlStr += indentedNewLine("</ul>", htmlIndentation)
			if (len(Uncontained["uncontainedConcepts"]) > 0):
				htmlStr += indentedNewLine("<h2>Concepts</h2>", htmlIndentation)
				htmlStr += indentedNewLine("<ul>", htmlIndentation)
				htmlIndentation += 1
				for Concept in sorted(Uncontained["uncontainedConcepts"]):
					FileName = "../" + self.ConceptFolder + "/" + Concept + ".html"
					htmlStr += indentedNewLine("<li>", htmlIndentation)
					htmlIndentation += 1
					htmlStr += "\n" + indentedNewLine(
						"<a href=\"{FileName:}\">".format(FileName = FileName), 
						htmlIndentation
					)
					htmlIndentation += 1
					htmlStr += "\n" + indentedNewLine(Concept, htmlIndentation)
					htmlIndentation -= 1
					htmlStr += "\n" + indentedNewLine("</a>", htmlIndentation)
					htmlIndentation -= 1
					htmlStr += indentedNewLine("</li>", htmlIndentation)
				htmlIndentation -= 1
				htmlStr += indentedNewLine("</ul>", htmlIndentation)
			htmlIndentation -= 1
			htmlStr += indentedNewLine("</main>", htmlIndentation)
			return htmlStr
		IndexFileName = self.HtmlFolder + "/Uncontained.html"
		with open (IndexFileName, "w") as IndexFile:
			IndexFile.write(self.htmlFile("Uncontained Objects", CreateUncontainedPage(), "../"))

	def CreateNotes(self,
		Items, Notes, Particles, Concepts, Topics, Uncontained
	):
		GenerateFolder(self.HtmlFolder)
		self.CreateCssFile()
		self.CreateItems(Items)
		self.CreateDigitalNotes(Notes)
		self.CreateParticles(Particles)
		self.CreateConcepts(Concepts, Particles)
		self.CreateTopics(Topics, Particles)
		self.CreateUncontained(Uncontained)
