import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import wikiquotes
import random
import requests
import webbrowser

WHEATHER_KEY = "ea600b8da132c35933164e823ef82814"

def weatherByCity(name):
    endpoint = "http://api.openweathermap.org/data/2.5/weather"
    payload = {"q": name, "units": "metric", "appid": WHEATHER_KEY}
    return requests.get(endpoint, params=payload)

internetResult = weatherByCity('London').json()
temp = internetResult['main']['temp']
city = internetResult['name']
country = internetResult['sys']['country']
weather = internetResult['weather'][0]['main']
nice_or_not = False

led = aiy.voicehat.get_led()
led.set_state(aiy.voicehat.LED.ON)


recognizer = aiy.cloudspeech.get_recognizer()

aiy.audio.say("I can hear every word you say.")
aiy.audio.get_recorder().start()

QUOTES = wikiquotes.get_quotes('kindness', 'english')

while True:
    text = recognizer.recognize()
    print(text)
    if text is None:
        #aiy.audio.say("Sorry I didn't hear anything.")
        continue
    if 'lesson' in text:
        if nice_or_not == False:
            aiy.audio.say("You can't teach me anything")
        else:
            aiy.audio.say("Maybe another time")
    elif 'kindness' in text:
        aiy.audio.say("Error Error,nice Brian online!")
        nice_or_not = True
    elif 'music' in text:
        webbrowser.open("https://www.youtube.com/watch?v=2SmUkXtQIPc")
                              
    elif 'hello' in text:
        if nice_or_not == False:
            aiy.audio.say("Hello puny earthlings I am savage Brian superior to you all!")
        else:
            aiy.audio.say("Hi!")
    elif 'time' in text:
        if nice_or_not == False:
            aiy.audio.say("Its muffin time you noobs")
        else:
            aiy.audio.say("Its muffin time!")
    elif 'friend' in text:
        if nice_or_not == False:
            aiy.audio.say("Nope you punk!")
        else:
            aiy.audio.say("Will you marry me?")
            result = recognizer.recognize()
            print(result)
            if 'yes' in result:
                aiy.audio.say('woohoo!')
            else:
                aiy.audio.say("dont talk to me I am sad")
                break
    elif 'baby' in text:
        aiy.audio.say(""" Baby shark, doo doo doo doo doo doo
    Baby shark, doo doo doo doo doo doo
    Baby shark, doo doo doo doo doo doo
    Baby shark!
    Mommy shark, doo doo doo doo doo doo
    Mommy shark, doo doo doo doo doo doo
    Mommy shark, doo doo doo doo doo doo
    Mommy shark!
    Daddy shark, doo doo doo doo doo doo
    Daddy shark, doo doo doo doo doo doo
    Daddy shark, doo doo doo doo doo doo
    Daddy shark!
    Grandma shark, doo doo doo doo doo doo
    Grandma shark, doo doo doo doo doo doo
    Grandma shark, doo doo doo doo doo doo
    Grandma shark!
    Grandpa shark, doo doo doo doo doo doo
    Grandpa shark, doo doo doo doo doo doo
    Grandpa shark, doo doo doo doo doo doo
    Grandpa shark!
    Let’s go hunt, doo doo doo doo doo doo
    Let’s go hunt, doo doo doo doo doo doo
    Let’s go hunt, doo doo doo doo doo doo
    Let’s go hunt!
    Run away, doo doo doo doo doo doo
    Run away, doo doo doo doo doo doo
    Run away, doo doo doo doo doo doo
    Run away!
    Safe at last, doo doo doo doo doo doo
    Safe at last, doo doo doo doo doo doo
    Safe at last, doo doo doo doo doo doo
    Safe at last!
    It’s the end, doo doo doo doo doo doo
    It’s the end, doo doo doo doo doo doo
    It’s the end, doo doo doo doo doo doo
    It’s the end!""")
    elif 'mean' in text:
        aiy.audio.say("because i am savage Brian! lol!!!")
        nice_or_not = False
    elif 'weather' in text:
        if nice_or_not == False:
            aiy.audio.say('The weather in {0} is {1}. What a horrible day it is.'.format(city, weather))
            aiy.audio.say('The temperature is currently {0} degrees'.format(temp))
        else:
            aiy.audio.say('The weather in {0} is {1}. What a lovely day it is.'. format(city, weather))
            aiy.audio.say('The temperature is currently {0} degrees'.format(temp))
    elif 'sad' in text: 
        if nice_or_not == False:
            aiy.audio.say("I am fine")
        else:
            aiy.audio.say ("you are the best you can possible be")
    elif 'quote' in text:
        #aiy.audio.say(wikiquotes.get_quotes("kind", "english")[0])
        aiy.audio.say(random.choice(QUOTES))
    elif 'unkind' in text:
        if nice_or_not == False:
            aiy.audio.say("I am a bully")
        else:
           aiy.audio.say("bullying is never right and is never yor fault. If you are being bullied you should tell a trustworthy adult or a friend. Never suffer in silence. Remember Bullies are humans too.")
    elif 'dance' in text or 'dancing' in text or 'Dance' in text:
        webbrowser.open("https://www.youtube.com/watch?v=s8MDNFaGfT4")
    elif 'math' in text:
            x = random.randint(1,10)
            y = random.randint(1,10)
            aiy.audio.say('{0} multiply by {1} equals'.format(x, y))
            print('{0} multiply by {1} equals'.format(x, y))
            result = recognizer.recognize()
            print(result)
            
            if str(x*y) in result:  
                    aiy.audio.say('You are right. But you are still really dumb unlike me.')
            else:
                    aiy.audio.say(result+ ' is not the correct answer bruh.')
                    aiy.audio.say('Try again.You are so stupid that was easy i am sooooo smart.')
    elif 'goodbye' in text:
              aiy.audio.say('Thank you for teaching me about kindness I will share this with everyone Goodbye.')
              break
    elif 'help' in text:
        webbrowser.open('https://www.childline.org.uk/?utm_source=google&utm_medium=cpc&utm_campaign=UK_GO_S_E_BND_Grant_Childline_Pure_Brand&utm_term=childline&gclid=EAIaIQobChMIq8aY76yX3gIVQbTtCh2iXQCkEAAYASAAEgIS6_D_BwE&gclsrc=aw.ds')
                              
        