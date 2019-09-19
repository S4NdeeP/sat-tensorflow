import json
import pandas as pd

caption_file = 'captions_train2014.json'
with open(caption_file) as f:
	caption_data = json.load(f)

# id_to_filename is a dictionary such as {image_id: filename]} 
id_to_filename = {image['id']: image['file_name'] for image in caption_data['images']}

# data is a list of dictionary which contains 'captions', 'file_name' and 'image_id' as key.
data = []
for annotation in caption_data['annotations']:
	image_id = annotation['image_id']
	annotation['file_name'] = id_to_filename[image_id]
	data += [annotation]

# convert to pandas dataframe (for later visualization or debugging)
caption_data = pd.DataFrame.from_dict(data)
del caption_data['id']
caption_data.sort_values(by='image_id', inplace=True)
caption_data = caption_data.reset_index(drop=True)

imagesList = []
file_token = open('COCO_train.token.txt', 'w')
file_image = open('COCO.train.images.txt', 'w')
current_image_id = -1
no_of_images = 0
no_of_captions = 0
for i in range(len(caption_data)):
	image_id = int(caption_data['image_id'][i])
	if(current_image_id != image_id):
		count=0
		no_of_images += 1
		current_image_id = image_id
		imagesList.append(caption_data['file_name'][i])
		file_image.write(caption_data['file_name'][i] + '\n')
	
	caption = caption_data['caption'][i].strip().replace('\n',' ')
	line = caption_data['file_name'][i] + '#' + str(count) + '\t' + caption + '\n'
	file_token.write(line)
	no_of_captions += 1
	count+=1
file_token.close()
file_image.close()

print "No of Images = " + str(no_of_images)
print "No of Caption Set = " + str(no_of_captions)
