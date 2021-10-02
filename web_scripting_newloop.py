


import requests
import time

from bs4 import BeautifulSoup
import smtplib
import email.mime
import datetime



import requests
import pyttsx3
import bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen

text_speech = pyttsx3.init()
import time    

for i in range(60):
 headers = {
    'User-Agent':"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Mobile Safari/537.36 Edg/94.0.992.31'"
 }
    
 url = "https://www.bbc.com/weather/your-city-id" #Enter the weather link of the city that needs to be checked   
 t = time.localtime()
 current_hr = time.strftime("%H:%M", t)
 text_speech.say(current_hr)
 text_speech.runAndWait()
 cnt5=''
 cnt6=''
 cnt1 =''
 r = requests.get(url,{'headers':headers})
 soup = bs4.BeautifulSoup(r.text,"html.parser")
 tag = soup.find('h1', attrs={"id": "wr-location-name-id"})
 cnt1+=tag.text
 tag = soup.find('span', attrs={"class": "wr-value--temperature--c"})
 cnt5+=tag.text
 tag = soup.find('div', attrs={"class": "wr-day__weather-type-description wr-js-day-content-weather-type-description wr-day__content__weather-type-description--opaque"})
 cnt6+=tag.text
 final = "The   temperature is "+ cnt5 + "  now"
 text_speech.say(cnt1)
 text_speech.runAndWait()
 text_speech.say(final)
 text_speech.runAndWait()
 text_speech.say(cnt6)
 text_speech.runAndWait()
 print(current_hr)
 time.sleep(600)  #no of minutes 
    
