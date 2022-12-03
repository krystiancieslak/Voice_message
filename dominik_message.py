import pyttsx3

def message_for_dominik():
    synthesizer = pyttsx3.init()
    synthesizer.say("Dominic, go to a fucking gym") 
    synthesizer.runAndWait() 
    synthesizer.stop()
    return

message_for_dominik()