cat Flickr_30k.trainImages.txt >> COCO.train.images.txt
cat Flickr_30k.devImages.txt >> COCO.val.images.txt
cat Flickr_30k.testImages.txt >> COCO.test.images.txt

cat PASCALVOC.train.images.txt >> COCO.train.images.txt
cat PASCALVOC.val.images.txt >> COCO.val.images.txt
cat PASCALVOC.test.images.txt >> COCO.test.images.txt

cat token.txt >> COCO_all.token.txt
cat PASCALVOC.token.txt >> COCO_all.token.txt

mv COCO.train.images.txt Combined.trainImages.txt
mv COCO.val.images.txt Combined.devImages.txt
mv COCO.test.images.txt Combined.testImages.txt
mv COCO_all.token.txt Combined.token.txt
