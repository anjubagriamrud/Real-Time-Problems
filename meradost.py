import pyttsx3
Dost=pyttsx3.init()
voices =Dost.getProperty('voices')
Dost.setProperty('voice',voices[1].id)      #0 for men voice, and 1 for women
Dost.say("Hello papa")

# Dost.say("Anju and Meenu are best friend")
Dost.runAndWait()