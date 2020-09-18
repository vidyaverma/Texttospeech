# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 12:47:53 2020

@author: HP
"""


from gtts import gTTS 
  

import os 

fh = open("test.txt", "r")
myText = fh.read().replace("\n", " ")

language = 'en'

output = gTTS(text=myText, lang=language, slow=False)

output.save("output.mp3")
fh.close()

# Play the converted file 
os.system("start output.mp3")