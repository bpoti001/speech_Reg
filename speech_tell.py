import speech_recognition as sr
import subprocess
from gtts import gTTS

a = True
while a:
# Record Audio
        r = sr.Recognizer()
        with sr.Microphone() as source:
                ext_text ="to quit say exit or to continue Say somthing!!"
                tts1 = gTTS(text=ext_text,lang='en')
                exit_aud = 'exit_audio.mp3'
                tts1.save(exit_aud)
                rt_c = subprocess.call(['afplay',exit_aud])
                audio = r.listen(source)
 
                # Speech recognition using Google Speech Recognition
        try:
                text_data = r.recognize_google(audio)
        except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
        if text_data:
                print("You said: " + text_data)
                audio_file ="hello.mp3"
                tts = gTTS(text=text_data,lang="en")
                tts.save(audio_file)
                return_code = subprocess.call(['afplay',audio_file])
                if text_data =='exit':
                    a=False
                if 'open' in text_data:
                    tt = text_data.split()
                    for i in range(1,len(tt)):
                        tt[i] = tt[i][0].upper()
                    app =''.join(tt[1:])
                    ds = subprocess.call(['open -a '+app])
        
        
                