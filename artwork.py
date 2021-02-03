import eyed3
import os

for filename in os.listdir('All'):
    tag = filename[0:24]

    au = eyed3.load('All/' + tag +'.mp3')
    if (au.tag == None):
        au.initTag()

    au.tag.images.set(3, open('imgs/'+tag+'.png','rb').read(),'image/jpeg')
    au.tag.save(version=eyed3.id3.ID3_V2_3)