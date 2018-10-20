import aiy.audio
import aiy.cloudspeech
import aiy.voicehat

led = aiy.voicehat.get_led()
led.set_state(aiy.voicehat.LED.ON)


recognizer = aiy.cloudspeech.get_recognizer()

aiy.audio.say("yo i can hear you")
aiy.audio.get_recorder().start()

while True:
    text = recognizer.recognize()
    if text and "blink" in text:
        led.set_state(aiy.voicehat.LED.BLINK)
         elif 'math' in text:
            x = random.randint(1,10)
            y = random.randint(1,10)
            aiy.audio.say('{0} multiply by {1} equals'.format(x, y))
            result = recognizer.recognize()
            print(result)
            if str(x*y) in result:
                aiy.audio.say('You are right. But you are still really dumb.')
            else:
                aiy.audio.say(result+ ' is not the correct answer.')
                aiy.audio.say('Try again. I am so more clever than you.')
                              
    elif "yo" in text:
        aiy.audio.say("Yo")
    elif "john cena" in text:
        aiy.audio.say("Doo doo doo")