import os

ItemFolder = "./html/Items"
ParticleFolder = "./html/Items"

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

def CreateItems(Items):
	def CreateItemPage(Id, Item):
		# Indentation inherited from html file
		htmlIndentation = 2
		htmlStr = indentedNewLine("<main>", htmlIndentation)
		htmlIndentation += 1
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
		htmlStr += "\n" + indentedNewLine("<p>", htmlIndentation)
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
				"<a href=\"../particles/{particle:}\">".format(particle = particle), 
				htmlIndentation
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
		htmlIndentation += 1
		htmlStr += "\n" + indentedNewLine(
			"<h1 class=\"ItemTitle\">{Title:}</h1>".format(Title = Id),
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
		htmlStr += "\n" + indentedNewLine(Particle, htmlIndentation)
		htmlIndentation -= 1
		htmlStr += "\n" + indentedNewLine("<p>", htmlIndentation)
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
		htmlStr += "\n" + indentedNewLine("<table>", htmlIndentation)
		htmlIndentation += 1
		htmlStr += "\n" + indentedNewLine("<tr>", htmlIndentation)
		htmlIndentation += 1
		htmlStr += "\n" + indentedNewLine("<th> ID </th>", htmlIndentation)
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

def CreateNotes(HtmlFolder, Items, Particles, Notes):
	GenerateFolder(HtmlFolder)
	global ItemFolder, ParticleFolder
	ItemFolder = HtmlFolder + "/Items"
	ParticleFolder = HtmlFolder +"/Particles"
	CreateItems(Items)
	CreateParticles(Particles)
