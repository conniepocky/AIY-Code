

import aiy.audio
import aiy.cloudspeech
import aiy.voice

def main():
    my_motion_detector = MotionDetector()
    recognizer = aiy.cloudspeech.get_recognizer()
    aiy.audio.get_recorder().start()
    
    while true:
        my_motion_detector = WaitForMotion()
        text = recognizer.recognize()
        aiy.audio.say("Hello puny humans, Brian is here. You said ", text)
        