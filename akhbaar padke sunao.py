def speaker(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(str)

if __name__ =='__main__':
    speaker('You are best my friend')