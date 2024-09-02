import subprocess
import os
import time
from datetime import datetime
import sys
now = datetime.now()
t=now.strftime('%I:%M:%p')
print(t)

inp = subprocess.getoutput("termux-speech-to-text")
time.sleep(1)
print("\033[95m You said: ",str(inp))

def system():
     if inp == "":
         subprocess.call(["termux-tts-speak","please tell something sir"])

     elif "hello" in inp:
         subprocess.call(["termux-tts-speak","hallow sir "])
         
     elif "close" in inp:
         subprocess.call(["termux-tts-speak","ok sir wait a minute"])
         time.sleep(1)
         sys.exit()
     elif "how are you" in inp:
        subprocess.call(["termux-tts-speak","i am good sir "])
     elif "battery" in inp:
         subprocess.call(["termux-battery-status"])
         
     elif "sleep" in inp:
         subprocess.call(["termux-tts-speak","ok sir i am going to sleep for 5 second"])
         time.sleep(5)
         
     elif "call me" in inp:
         os.system("termux-telephony-call +91")
     elif "torch on" in inp:
         os.system("termux-torch on")
     elif "torch off" in inp:
         os.system("termux-torch off")
         
     elif "YouTube" in inp:
         os.system("termux-open https://m.youtube.com")
     elif "Google" in inp:
         os.system("termux-open https://www.google.co.in/")    
         
     elif "contact" in inp:
         os.system("termux-contact-list")
         
     elif "who are you" in inp:
         subprocess.call(["termux-tts-speak","I am your virtual assistanct Termux, sir"])
         
     elif "time" in inp:
         subprocess.call(["termux-tts-speak",t])
         
     elif "what are you doing" in inp:
        subprocess.call(["termux-tts-speak","i am busy with you "])
        
     elif "are you busy" in inp:
         subprocess.call(["termux-tts-speak","i am always free for you"])
     
     elif "name" in inp:
         subprocess.call(["termux-tts-speak","you can call me termux "])
         
     elif "who is sirtaj gamer" in inp: 
         subprocess.call(["termux-tts-speak","Sirtaj Gamer is an Indian gaming YouTuber hailing from Uttar Pradesh, he currently has over 1.50K followers on his channel."])
         
     elif "counting from one to one" in inp:
              subprocess.call(["termux-tts-speak","count from one to one sir 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 "])
     
     
     elif "muhammad sallallahu alaihi wasallam kon hai" in inp:
         subprocess.call(["termux-tts-speak","muhammad 570 ee - 8 joon 632 ee) islaam ke sansthaapak then. islaamik maanyata ke anusaar, vah ek paigambar aur eeshvar ke sandeshavaahak the, jinhen islaam ke paigambar bhee kahate hain, jo pahale aadam , ibraaheem , moosa eesa (yeshoo) aur any paigambar dvaara prachaarit ekeshvaravaadee shikshaon ko prastut karane aur pushti karane ke lie bheje gae the."])
     elif "video" in inp:
         os.system("termux-open https://www.google.com/search?q=video")
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     else:
       subprocess.call(["termux-tts-speak","I am not cooded for that"])

system()

os.system("python main.py")