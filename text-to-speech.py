from gtts import gTTS

speech = "Hello Friends lets learn python with me"
x = gTTS(text=speech, lang='mr')
x.save('AI.mp3')


import os

os.system('AI.mp3')
