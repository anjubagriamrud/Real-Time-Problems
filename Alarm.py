import win10toast
import pyttsx3
import os
import pygame
from tkinter import *
import time
import datetime

ma = pyttsx3.init(
    "sapi5")  # todo sapi5=speech recognition API by microsoft SAPI[speech application programming interface]
voices = ma.getProperty("voices")
ma.setProperty("voice", voices[1].id)  # todo two deafault voices [zira,david]


def speak(audio):
    ma.say(audio)
    ma.runAndWait()


print('''THIS IS A ALARM CLOCK -BY ANJU BAGRI''')
value = input("ENTER [a] FOR ALARM AND [t] FOR TIME::-")
if value == "a":
    print(''' 			
				THIS SECTION IS FOR ALARM 

	  ''')

    hour = int(input("ENTER THE HOUR::-"))
    minute = int(input("ENTER THE MINUTE::-"))
    ampm = input("ENTER AM OR PM::-")
    note = input("DO YOU WANT TO ATTACH ANY NOTE TO YOUR ALARM ....ENTER [y] FOR YES AND [n] FOR NO::-")
    if note == "y":
        real = input("ENTER THE NOTE::")
    else:
        real = ""
    speak(f"your ALARM is set for {hour} hour {minute} minute ")
    print(f"          YOUR ALARM IS SET FOR  {hour}:{minute}:{ampm}")
    if ampm == "pm":
        if hour < 12:
            hour = hour + 12
    elif ampm == "am":
        hour = hour
    while (1 == 1):
        if datetime.datetime.now().hour == hour and datetime.datetime.now().minute == minute:
            music_dir = "C:\\Users\\Dell\\PycharmProjects\\realtimeproblems\\Alarm.mp3"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs))
            print("		ALARM RINGING................")
            toaster = win10toast.ToastNotifier()
            toaster.show_toast("ALARM", f"ANJU YOUR ALARM TIME HAS BEEN ATTAINED"
                                        f"{real}", duration=20)
            break
elif value == "t":
    def times():
        h = datetime.datetime.now().hour
        if h >= 12 and h < 24:
            k = "PM"
        elif h > 0 and h < 12:
            k = "AM"
        else:
            pass
        current_time = time.strftime("%H:%M:%S")
        clock.config(text=f"{current_time} {k}")
        clock.after(200, times)


    pygame.mixer.init()
    pygame.mixer.music.load("Fast Ticking Clock with Sound _ Animation(MP3_128K).mp3")
    pygame.mixer.music.play()

    root = Tk()
    root.title("DIGITAL CLOCK")
    root.geometry("580x400+550+50")
    root.config(bg="lightblue")
    root.maxsize(580, 400)
    clock = Label(root, font="lucida 55 bold", fg="red")
    clock.grid(row=2, column=2, pady=25, padx=100)
    times()
    digi = Label(root, text="DIGITAL CLOCK", font="Algerian 35 bold", fg="green", relief=SUNKEN, borderwidth=20)
    digi.grid(row=0, column=2)
    notations = Label(root, text="hours   minutes    seconds", font="Algerian 24 bold")
    notations.grid(row=3, column=2)
    dateis = Label(root, text=datetime.datetime.now().date(), font="Algerian 40 bold")
    dateis.grid(row=4, column=2, pady=50)
    root.mainloop()
else:
    speak("						PLEASE RE-START THE PROGRAMME        ")
    print("							PLEASE RE-START THE PROGRAMME        ")