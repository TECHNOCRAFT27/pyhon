
import datetime
import os
import webbrowser
from urllib.request import HTTPDefaultErrorHandler

import cv2 as cv
import googletrans
import gtts
import playsound
import pyttsx3
import pywhatkit
import random2
import speech_recognition as sr
import wikipedia
from googletrans import Translator
from pyttsx3 import engine
from wikipedia.wikipedia import languages

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


talk(" welcome back techno I am Caroline,  Please tell me how may I help you ?")


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Caroline' in command:
                command = command.replace('Caroline', '')
                print(command)
    except:
        pass
    return command
# # # database
# phono number
contact_list = {
    'lalit': ' +91 76201 85906',
    'sudarshan':'+91 74992 01573',
    'shadab':'+91 89838 45593',
    'Aditya s1':'91 72193 35147',
    'Parth s1':'91 98228 01222',
    'Rushikesh S1':'91 90960 99785'
   }
# phono number
# languages
# ful to short
bhasha1 = {
     'afrikaans':'af',
     'albanian':'sq',
     'amharic':'am',
     'arabic':'ar',
     'armenian':'hy',
     'azerbaijani':'az',
     'basque':'eu',
     'belarusian':'be',
     'bengali':'bn',
     'bosnian':'bs',
     'bulgarian':'bg',
     'catalan':'ca',
     'cebuano':'ceb',
     'chichewa':'ny',
     'chinese1 (simplified)':'zh-cn',
     'chinese2 (traditional)':'zh-tw',
     'corsican':'co',
     'croatian':'hr',
     'czech':'cs',
     'danish':'da',
     'dutch':'nl',
     'english':'en',
     'esperanto':'eo',
     'estonian':'et',
     'filipino':'tl',
     'finnish':'fi',
     'french':'fr',
     'frisian':'fy',
     'galician':'gl',
     'georgian':'ka',
     'german':'de',
     'greek':'el',
     'gujarati':'gu' ,
     'haitian creole':'ht',
     'hausa':'ha',
     'hawaiian':'haw',
     'hebrew':'iw',
     'hebrew':'he',
     'hindi':'hi',
     'hmong':'hmn',
     'hungarian':'hu',
     'icelandic':'is',
     'igbo':'ig',
     'indonesian': 'id',
     'irish':'ga',
     'italian':'it',
     'japanese':'ja',
     'javanese':'jw',
     'kannada':'kn',
     'kazakh':'kk' ,
     'khmer':'km',
     'korean':'ko',
     'kurdish (kurmanji)':'ku',
     'kyrgyz':'ky',
     'lao':'lo',
     'latin':'la',
     'latvian':'lv',
     'lithuanian':'lt',
     'luxembourgish':'lb',
     'macedonian':'mk',
     'malagasy':'mg' ,
     'malay':'ms',
     'malayalam':'ml',
     'maltese':'mt',
     'maori':'mi',
     'marathi':'mr',
     'mongolian':'mn',
     'myanmar (burmese)':'my',
     'nepali':'ne',
     'norwegian':'no',
     'odia':'or',
     'pashto':'ps',
     'persian':'fa',
     'polish':'pl',
     'portuguese':'pt',
     'punjabi':'pa' ,
     'romanian':'ro', 
     'russian':'ru' ,
     'samoan':'sm' ,
    'scots gaelic':'gd',
    'serbian':'sr',
    'sesotho':'st',
    'shona':'sn' ,
    'sindhi':'sd' ,
    'sinhala':'si' ,
    'slovak':'sk' ,
    'slovenian':'sl' ,
    'somali':'so' ,
    'spanish': 'es',
    'sundanese':'su' ,
    'swahili':'sw' ,
    'swedish':'sv' ,
    'tajik':'tg' ,
    'tamil':'ta' ,
    'telugu':'te' ,
    'thai':'th' ,
    'turkish':'tr' ,
    'ukrainian': 'uk',
    'urdu':'ur',
    'uyghur':'ug' ,
    'uzbek':'uz', 
    'vietnamese':'vi' ,
    'welsh':'cy' ,
    'xhosa':'xh' ,
    'yiddish':'yi' ,
    'yoruba': 'yo',
    'zulu':'zu'
    }
# ful to short
# # short to ful
bhasha2 ={
    'af': 'afrikaans',
    'sq': 'albanian', 
    'am': 'amharic', 
    'ar': 'arabic', 
    'hy': 'armenian', 
    'az': 'azerbaijani', 
    'eu': 'basque', 
    'be': 'belarusian', 
    'bn': 'bengali', 
    'bs': 'bosnian', 
    'bg': 'bulgarian', 
    'ca': 'catalan', 
    'ceb': 'cebuano', 
    'ny': 'chichewa', 
    'zh-cn': 'chinese (simplified)', 
    'zh-tw': 'chinese (traditional)', 
    'co': 'corsican', 'hr': 'croatian', 
    'cs': 'czech', 
    'da': 'danish', 
    'nl': 'dutch', 
    'en': 'english', 
    'eo': 'esperanto', 
    'et': 'estonian', 
    'tl': 'filipino', 
    'fi': 'finnish', 
    'fr': 'french', 
    'fy': 'frisian', 
    'gl': 'galician', 
    'ka': 'georgian', 
    'de': 'german', 
    'el': 'greek', 
    'gu': 'gujarati', 
    'ht': 'haitian creole', 
    'ha': 'hausa', 
    'haw': 'hawaiian', 
    'iw': 'hebrew', 
    'he': 'hebrew', 
    'hi': 'hindi', 
    'hmn': 'hmong', 
    'hu': 'hungarian', 
    'is': 'icelandic', 
    'ig': 'igbo', 
    'id': 'indonesian', 
    'ga': 'irish', 
    'it': 'italian', 
    'ja': 'japanese', 
    'jw': 'javanese', 
    'kn': 'kannada', 
    'kk': 'kazakh', 
    'km': 'khmer', 
    'ko': 'korean', 
    'ku': 'kurdish (kurmanji)', 
    'ky': 'kyrgyz', 
    'lo': 'lao', 
    'la': 'latin', 
    'lv': 'latvian', 
    'lt': 'lithuanian', 
    'lb': 'luxembourgish', 
    'mk': 'macedonian', 
    'mg': 'malagasy', 
    'ms': 'malay', 
    'ml': 'malayalam', 
    'mt': 'maltese', 
    'mi': 'maori', 
    'mr': 'marathi', 
    'mn': 'mongolian', 
    'my': 'myanmar (burmese)', 
    'ne': 'nepali', 
    'no': 'norwegian', 
    'or': 'odia', 
    'ps': 'pashto', 
    'fa': 'persian', 
    'pl': 'polish', 
    'pt': 'portuguese', 
    'pa': 'punjabi', 
    'ro': 'romanian', 
    'ru': 'russian', 
    'sm': 'samoan', 
    'gd': 'scots gaelic', 
    'sr': 'serbian', 
    'st': 'sesotho', 
    'sn': 'shona', 
    'sd': 'sindhi', 
    'si': 'sinhala', 
    'sk': 'slovak', 
    'sl': 'slovenian', 
    'so': 'somali', 
    'es': 'spanish', 
    'su': 'sundanese', 
    'sw': 'swahili', 
    'sv': 'swedish', 
    'tg': 'tajik', 
    'ta': 'tamil', 
    'te': 'telugu', 
    'th': 'thai', 
    'tr': 'turkish', 
    'uk': 'ukrainian', 
    'ur': 'urdu', 
    'ug': 'uyghur', 
    'uz': 'uzbek', 
    'vi': 'vietnamese', 
    'cy': 'welsh', 
    'xh': 'xhosa', 
    'yi': 'yiddish', 
    'yo': 'yoruba', 
    'zu': 'zulu'
}
# short to ful
# languages
#Task 

task ={
       '1',
       '2',
       '3',
       '4',
       '5',
       '6',
       '7',
       '8',
       '9',
       '10',
    }

#Task 
# database
# main part

def run_Caroline():
    command = take_command()
    print(command)

    # function
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif'schedule' in command:
        talk('here we go') 
        codePath = "C:\\Users\\pramila khopade\\Desktop\\my life\\2.workplace\\7.student\\basis\\Timetable.png"
        os.startfile(codePath)   
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'send message' in command:
        talk('To Whom you want to send message')
        name = take_command()
        receiver = contact_list[name]
        print(name)
        talk('What is the subject of your message?')
        subject = take_command()
        hour = datetime.datetime.now().hour
        min = datetime.datetime.now().minute
        pywhatkit.sendwhatmsg(receiver, subject, hour, min+1)
        talk('your message has been send ')            
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 5)
        print(info)
        talk("According myresearch from wikipedia"+info)
    elif 'what is ' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 5)
        print(info)
        talk("According myresearch from wikipedia"+info)
    elif 'gana' in command:
        n = random2.randint(0, 35)
        music_dir = 'C:\\Users\\pramila khopade\\Videos\\video'
        song = os.listdir(music_dir)
        print(song[n])
        os.startfile(os.path.join(music_dir, song[n]))
    elif 'what can you do' in command:
        print()
    elif 'mean by' in command:
        word = command.replace('mean by', '')
        talk('seaching ... ' + word)
        pywhatkit.search('mean by'+word)
    elif 'search for' in command:
        find = command.replace('search for', '')
        talk('searching for ' + find)
        pywhatkit.search(find)

        talk("okay techno do you like maths")
        codePath = "C:\\Users\\pramila khopade\\Desktop\\my life\\app\\Calculator.ink"
        os.startfile(codePath)
    elif 'translate for me' in command:
        talk('yes, what is the message ?')
        message = take_command()
        print(message)
        talk('okay , In which language you want to change...')
        vani = take_command()
        boli = bhasha1[vani]
        print(vani)
        print(boli)
        Translator = googletrans.Translator()
        sentence =Translator.translate(message ,dest= boli)
        converted_audio = gtts.gTTS(sentence.text, lang=boli)
        converted_audio.save('message.mp3')
        playsound.playsound('message.mp3')
    elif 'detect language' in command:
        talk('yes, what is the message ?')
        detect = take_command()
        Translator = googletrans.Translator()
        result = Translator.translate(detect, lang_tgt='en') 
        detected = bhasha2[result.src]
        print(detect)
        talk('language is ...')
        talk(detected)
        print(detected)
        talk(result.text)
        print(result.text)
    elif 'maths' in command:
        talk('no techno,do maths your own')
        codePath = "C:\\Program Files\\Epic Games\\UE_4.26\\Engine\\Binaries\\Win64\\UE4Editor.exe"
        os.startfile(codePath)
    # funtion
    # website
    elif 'open youtube' in command:
        talk("okay techno opening youtube")
        webbrowser.open("www.youtube.com")
        talk("hope so you will get what you want.")
    elif "open what's up" in command:
        talk("okay techno opening youtube")
        webbrowser.open("https://web.whatsapp.com/")
        talk("hope so you will get what you want.")
    elif 'show me recent video on youtube' in command:
        talk("okay techno opening youtube")
        webbrowser.open("https://www.youtube.com/feed/history")
        talk("hope so you will get what you want.")
    elif 'open google' in command:
        talk("okay techno opening google")
        webbrowser.open("www.google.com")
        talk("hope so you will get what you want. ")
    elif 'show pip station' in command:
        talk("okay techno opening pypi.org")
        webbrowser.open("www.pypi.org")
    elif 'show me game asset' in command:
        talk("okay opening game asset ")
        webbrowser.open("www.mixamo.com")
        webbrowser.open("https://poly.google.com/")
        webbrowser.open("https://depositphotos.com/")
        webbrowser.open("https://editor.construct.net/")
        talk("let's show them how is best gamedev")
    elif 'show me website asset' in command:
        webbrowser.open("https://getbootstrap.com")
        webbrowser.open("https://icons.getbootstrap.com")
        webbrowser.open("https://pixabay.com")
        webbrowser.open("https://unsplash.com/")
        webbrowser.open("https://www.codingnepalweb.com/")
        webbrowser.open("https://fonts.google.com/")
        talk("let's done our best")
    elif 'game on' in command:
        webbrowser.open("https://venge.io/")
        webbrowser.open("https://www.crazygames.com/game/forward-assault")
        webbrowser.open("https://miniroyale2.io")
        webbrowser.open("https://www.crazygames.com/game/downtown-1930s-mafia")
        webbrowser.open("https://www.youtube.com/watch?v=LaQj636PJh0&t=1081s")
        talk("let's show them who is best gamer")
    elif 'gaming mode activate' in command:
        webbrowser.open("https://venge-io")
        webbrowser.open("https://www.crazygames.com/game/forward-assault")
        webbrowser.open("https://miniroyale2.io")
        webbrowser.open("https://www.crazygames.com/game/downtown-1930s-mafia")
        webbrowser.open("https://www.youtube.com/watch?v=LaQj636PJh0&t=1081s")
        talk("let's show them who is best gamer")
        # website
    # speak
    elif 'good job' in command:
        talk('thank you techno')
    elif 'good girl' in command:
        talk('thank you techno')       
    elif 'thank you' in command:
        talk('your welcome techno')
    elif 'are you listening' in command:
        talk('yes techno')
    elif 'are you there' in command:
        talk('yes i am here for you')
    elif 'you are smart' in command:
        talk('I am smart because you techno ')
    elif 'best gamer' in command:
        talk('I am sure you are not best gamer ')
    elif "don't like this" in command:
        talk('sorrrry! I was joking. ')
    elif 'smartest person' in command:
        talk('I know you are 7th smartest person in world')
    elif 'great' in command:
        talk('thank you techno. can we move on')
    elif 'hi caroline' in command:
        talk('hello techno,how are you ')
    elif 'hello caroline' in command:
        talk('hello techno,how are you ')
    elif 'good morning' in command:
        talk('good morning techno,let start our work')
    # speak
    # folder
    elif 'show me website folder' in command:
        talk("okay opening ")
        codePath = "C:\\Users\\pramila khopade\\Desktop\\my life\\invention\\workplace\\website\\project"
        os.startfile(codePath)
    elif 'show python project' in command:
        codePath = "C:\\Users\\pramila khopade\\AppData\\Local\\Programs\\Microsoft VS Code\atom.exe"
        os.startfile(codePath)
    elif 'show unreal project' in command:
        codePath = "C:\\Users\\pramila khopade\\Desktop\\my life\\invention\\workplace\\gamedev\\unreal projects"
        os.startfile(codePath)
    elif 'show me resource file' in command:
        codePath = "C:\\Users\\pramila khopade\\Desktop\\my life\\youtube\\Resource file"
        os.startfile(codePath)
    elif 'show me recent project' in command:
        codePath = "C:\\Users\\pramila khopade\\Desktop\\use"
        os.startfile(codePath)
    elif 'show me livegamer27 folder' in command:
        codePath = "C:\\Users\\pramila khopade\\Desktop\\my life\\youtube\\my channel\\live gamer"
        os.startfile(codePath)
    elif 'show me technoCraft folder' in command:
        codePath = "C:\\Users\\pramila khopade\\Desktop\\my life\\youtube\\my channel\\techno craft"
        os.startfile(codePath)
    # folder
    # application
    elif 'open unreal engine' in command:
        talk("okay techno let's make game")
        codePath = "C:\\Program Files\\Epic Games\\UE_4.26\\Engine\\Binaries\\Win64\\UE4Editor.exe"
        os.startfile(codePath)
    elif 'open code' in command:
        talk("okay techno let's coding")
        codePath = "C:\\Users\\pramila khopade\\AppData\\Local\\Programs\\Microsoft VS Code\code.exe"
        os.startfile(codePath)
    elif 'open bluestacks' in command:
        talk("your wish is my command")
        codePath = "C:\\Program Files\\BlueStacks\\Bluestacks.exe"
        os.startfile(codePath)
    elif 'open brave browser' in command:
        talk("your wish is my command")
        codePath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        os.startfile(codePath)
    elif 'open Opera GX' in command:
        talk("your wish is my command")
        codePath = "C:\\Users\\pramila khopade\\Desktop\my life\\app\\picsArt.ink"
        os.startfile(codePath)
    elif 'open construct 3' in command:
        talk("okay techno let' make game")
        codePath = "C:\\Users\\pramila khopade\\Desktop\my life\\app\\construct 3.ink"
        os.startfile(codePath)
    elif 'open picsArt' in command:
        talk("okay techno let's start photo editing")
        codePath = "C:\\Users\\pramila khopade\\Desktop\my life\\app\\picsArt.ink"
        os.startfile(codePath)
    elif 'open Epic Games Launcher' in command:
        talk("okay techno do you like maths")
        codePath = "C:\\Users\\pramila khopade\\Desktop\\my life\\app\\Epic Games Launcher.ink"
        os.startfile(codePath)
    elif 'open PhotoScape X' in command:
        talk("okay techno opening PhotoScape X")
        codePath = "C:\\Users\\pramila khopade\\Desktop\\my life\\youtube\\editor app\\PhotoScape x.ink"
        os.startfile(codePath)
    elif 'open video editor' in command:
        talk("okay techno opening video editor")
        codePath = "C:\\Users\\pramila khopade\\Desktop\\my life\\youtube\\editor app\\VSDC Free Video Editor.lnk"
        os.startfile(codePath)
    elif 'open blender' in command:
        talk("okay techno opening Blender")
        codePath = "C:\\Users\\pramila khopade\\Desktop\\my life\\youtube\\editor app\\blender.lnk"
        os.startfile(codePath)
    elif 'open OBS Studio' in command:
        talk("okay techno opening OBS Studio")
        codePath = "C:\\Users\\pramila khopade\\Desktop\\my life\\youtube\\editor app\\OBS Studio.lnk"
        os.startfile(codePath) 
    # application
    else:
        talk('what to say, can you repeat again')
# main part
# The end
while True:
    run_Caroline()
# the end
