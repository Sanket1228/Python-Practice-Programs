from win32com.client import Dispatch
import requests
import json

def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == "__main__":
    # speak("Sanket is my best friend")
    speak("News for today... Lets begin")
    url = ('https://newsapi.org/v2/everything?'
       'q=top-headlines&'
       'sortBy=the-times-of-india&'
       'apiKey=e0e9b7a279dd4ababe20bced391e1585')
    response = requests.get(url).text
    # print(response.json())
    news_dict = json.loads(response)
    arts = news_dict['articles']
    for article in arts:
        print(f"{article['title']} - {article['description']}")
        speak(article['title'])
        speak("Do you want to listen full news")
        ans = input("Do you want to listen full news ? : ")
        if ans == "y" or ans=="yes" or ans=="Yes":
            speak("In detail")
            speak(article['description'])
        speak("Moving on to the next news...")
    speak("Thanks for listening....")