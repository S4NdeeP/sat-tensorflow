from HTMLParser import HTMLParser
# create a subclass and override the handler methods
from sklearn import model_selection as ms

startFlag = False
imageFileNameList = []
imageFileName = ''
imageCaption = []
outputFileLines = []
count = 0

imagesCount = 0
imagesCaptionSetCount = 0
class MyHTMLParser(HTMLParser):
	
	def handle_starttag(self, tag, attrs):
		global startFlag
		global imageCaption
		global imageFileName
		global count
		global outputFileLines
		global imagesCaptionSetCount
		global imageFileNameList

		if tag == 'table':
			startFlag = True

		if tag == 'img':
			# To handle the case for images 2008_003858.jpg 2008_008748.jpg 2008_006210.jpg which
			# have only 4 captions
			if(count == 4):
				imagesCaptionSetCount += 1
				for line in imageCaption:
					outputFileLines.append(line)

			imageCaption = []
			count = 0
			

			global imagesCount
			imagesCount +=1
			for attr in attrs:
				if attr[0] == 'src':
					pathParts = attr[1].split('/')
					imageFileName = pathParts[2]
					imageFileName = 'PASCAL_' + imageFileName
					imageFileNameList.append(imageFileName)

	def handle_endtag(self, tag):
		pass
		#print "Encountered an end tag :", tag

	def handle_data(self, data):
		global startFlag
		global imageCaption
		global imageFileName
		global count
		global outputFileLines
		global imagesCaptionSetCount

		if(startFlag):
			line = imageFileName + '#' + str(count) + '\t' + data.strip() + '\n'
			imageCaption.append(line)

			if(count == 4):
				imagesCaptionSetCount += 1
				for line in imageCaption:
					outputFileLines.append(line)

			count += 1

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
#with open('dummy.html', 'r') as file:
with open('vision.cs.uiuc.edu.html', 'r') as file:
	html = file.read()
html = html.replace('\n','')
parser.feed(html)

with open('PASCALVOC.token.txt', 'w') as file:
	for line in outputFileLines:
		file.write(line)

with open('PASCALVOC.images.txt', 'w') as file:
	for imageFileName in imageFileNameList:
		file.write(imageFileName + '\n')

images_train, images_test = ms.train_test_split(imageFileNameList, test_size=0.3, random_state=42)
images_val, images_test = ms.train_test_split(images_test, test_size=0.5, random_state=42)

with open('PASCALVOC.train.images.txt', 'w') as file:
	for imageFileName in images_train:
		file.write(imageFileName + '\n')

with open('PASCALVOC.val.images.txt', 'w') as file:
	for imageFileName in images_val:
		file.write(imageFileName + '\n')

with open('PASCALVOC.test.images.txt', 'w') as file:
	for imageFileName in images_test:
		file.write(imageFileName + '\n')

print "No of Images = " + str(imagesCount)
print "No of Caption Set = " + str(imagesCaptionSetCount)