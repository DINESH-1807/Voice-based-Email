import speech_recognition as sr
import easyimap as e
import pyttsx3
import smtplib

unm = "vthtteam16@gmail.com"   # Your Gmail ID
pwd = "cccr luee gukm lcuq"    # Your Gmail app password

r = sr.Recognizer()

engine = pyttsx3.init()        # Defining an engine for text to speech
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


def speak(message):            # Function for text to speech
    print(message)
    engine.say(message)
    engine.runAndWait()


def listen():                  # Function for speech to text
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        speak("Speak Now:")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text.lower()   # Convert everything to lowercase
        except:
            speak("Sorry could not recognize what you said")
            return None


def sendmail():
    speak("Please speak the recipient's email address")
    rec_email = listen()

    if rec_email:
        # Clean up email address
        rec_email = rec_email.replace(" ", "").lower()
        rec_email = rec_email.replace("dot", ".").replace("at", "@")

        speak("Recipient's email address is: " + rec_email)
        rec = rec_email
    else:
        speak("No recipient recognized. Cancelling.")
        return

    speak("Please speak the body of your email")
    body = listen()

    if not body:
        speak("No body recognized. Cancelling.")
        return

    speak("Your body of the email is")
    speak(body)

    # Send the email
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(unm, pwd)
    server.sendmail(unm, rec, body)
    server.quit()

    speak("The email has been Sent")


def readmail():
    server = e.connect("imap.gmail.com", unm, pwd)
    email_ids = server.listids()

    speak("Please say the serial number of the email you want to read starting from the latest")

    user_input = listen()

    if user_input:
        if user_input == "one":
            user_input = "1"

        try:
            email_index = int(user_input) - 1

            if 0 <= email_index < len(email_ids):
                email = server.mail(email_ids[email_index])

                speak("The email is from:")
                speak(email.from_addr)
                speak("The subject of the email is:")
                speak(email.title)
                speak("The body of the email is:")
                speak(email.body)
            else:
                speak("Invalid email number. Please provide a valid serial number.")
        except ValueError:
            speak("Could not recognize the number you said. Please provide a valid number.")
    else:
        speak("No input was recognized. Please try again.")


# Main program loop
speak("Welcome to voice controlled email service")

while True:
    speak("Speak SEND to Send email    Speak READ to Read Inbox   Speak EXIT to Exit")
    ch = listen()

    if ch == 'send':
        speak("You have chosen to send an email")
        sendmail()

    elif ch == 'read':
        speak("You have chosen to read email")
        readmail()

    elif ch == 'exit':
        speak("You have chosen to exit, bye bye")
        exit(1)

    else:
        if ch:
            speak("Invalid choice, you said:")
            speak(ch)
        else:
            speak("I did not catch that. Please try again.")
