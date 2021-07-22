import os
import time
import getpass
from collections import Counter
import socket
import threading
try:
    import speech_recognition as sr
    import pyttsx3
    from winrt.windows.ui.notifications import ToastNotificationManager, ToastNotification
    import winrt.windows.data.xml.dom as dom
    from scapy.all import sniff
except Exception as AttributeError:
    if(str(AttributeError)=="No module named 'pyttsx3'"):
        os.system("pip install pyttsx3")
        import pyttsx3
    elif(str(AttributeError)=="No module named 'speech_recognition'"):
        os.system("pip install SpeechRecognition")
        import speech_recognition as sr
    elif(str(AttributeError)=="No module named 'winrt'"):
        os.system("pip install winrt")
        from winrt.windows.ui.notifications import ToastNotificationManager, ToastNotification
        import winrt.windows.data.xml.dom as dom
    elif("scapy"in str(AttributeError)):
        os.system("pip install scapy")
        from scapy.all import sniff

USER_NAME = getpass.getuser()
def add_to_startup(file_path=""):
    if file_path == "":
        file_path = __file__
        file_path=f'"{file_path}"'
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start pyw %s \n exit' % file_path )
        bat_file.write('\nexit')
    print(__file__)
add_to_startup()

nonosite=str(socket.gethostbyname("pornhub.com"))

packet_counts = Counter()

appid=r'Anti HARAM 2.0'
notifier = ToastNotificationManager.create_toast_notifier(appid)
titleonsu="ANTI-HARAM 2.0 LOADED"
desc="You better not say any nono words!!!"
tString = """<toast duration='short'><audio src  = 'ms-winsoundevent:Notification.Reminder' loop = 'false' silent = 'false'/><visual><binding template='ToastText02'><text id="1">""" + titleonsu + """</text><text id="2">""" + desc + """</text></binding></visual></toast>"""

xDoc = dom.XmlDocument()
xDoc.load_xml(tString)
notifier.show(ToastNotification(xDoc))
def Microphoneharam():
    recognizer=sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic)
                audio=recognizer.listen(mic,timeout=8,phrase_time_limit=8)
                text=recognizer.recognize_google(audio)
                text= text.lower()
                print(str(text))
                if "***" in str(text):
                    appid=r'Anti HARAM 2.0'
                    notifier = ToastNotificationManager.create_toast_notifier(appid)
                    title="ANTI-HARAM 2.0 bad word spotted"
                    descreal="I hope that Allah has mercy on your soul!"
                    tString = """<toast duration='short'><audio src  = 'ms-winsoundevent:Notification.Reminder' loop = 'false' silent = 'false'/><visual><binding template='ToastText02'><text id="1">""" + title + """</text><text id="2">""" + descreal + """</text></binding></visual></toast>"""
                    xDoc = dom.XmlDocument()
                    xDoc.load_xml(tString)
                    notifier.show(ToastNotification(xDoc))
                    os.system("shutdown -s")
                    print("you said a nono word")

                elif "shutdown" in str(text):
                    appid=r'Anti HARAM 2.0'
                    notifier = ToastNotificationManager.create_toast_notifier(appid)
                    title="ANTI-HARAM 2.0 bad word spotted"
                    descreal="I hope that Allah has mercy on your soul!"
                    tString = """<toast duration='short'><audio src  = 'ms-winsoundevent:Notification.Reminder' loop = 'false' silent = 'false'/><visual><binding template='ToastText02'><text id="1">""" + title + """</text><text id="2">""" + descreal + """</text></binding></visual></toast>"""
                    xDoc = dom.XmlDocument()
                    xDoc.load_xml(tString)
                    notifier.show(ToastNotification(xDoc))
                    os.system("shutdown -s")
                    print("you said a nono word")
                else:
                    continue
        except Exception as e:
            recognizer=sr.Recognizer()
            print(e)
            continue
def custom_action(packet):
    key = tuple(sorted([packet[0][1].src, packet[0][1].dst]))
    packet_counts.update([key])
    if str(nonosite) in str(packet[0][1].src):
        appid=r'Anti HARAM 2.0'
        notifier = ToastNotificationManager.create_toast_notifier(appid)
        title="ANTI-HARAM 2.0 bad site"
        descreal="Bad site is sending you requests;(("
        tString = """<toast duration='short'><audio src  = 'ms-winsoundevent:Notification.Reminder' loop = 'false' silent = 'false'/><visual><binding template='ToastText02'><text id="1">""" + title + """</text><text id="2">""" + descreal + """</text></binding></visual></toast>"""
        xDoc = dom.XmlDocument()
        xDoc.load_xml(tString)
        notifier.show(ToastNotification(xDoc))
        #os.system("shutdown -s")
    elif str(nonosite) in str(packet[0][1].dst):
        appid=r'Anti HARAM 2.0'
        notifier = ToastNotificationManager.create_toast_notifier(appid)
        title="ANTI-HARAM 2.0 bad site"
        descreal="I hope that Allah has mercy on your soul!"
        tString = """<toast duration='short'><audio src  = 'ms-winsoundevent:Notification.Reminder' loop = 'false' silent = 'false'/><visual><binding template='ToastText02'><text id="1">""" + title + """</text><text id="2">""" + descreal + """</text></binding></visual></toast>"""
        xDoc = dom.XmlDocument()
        xDoc.load_xml(tString)
        notifier.show(ToastNotification(xDoc))
        os.system("shutdown -s")
    else:
        pass
def haramdetector():
    while True:
        sniff(filter="ip", prn=custom_action, count=10)

threads = list()
x = threading.Thread(target=haramdetector)
threads.append(x)
x.start()
x2 = threading.Thread(target=Microphoneharam)
threads.append(x2)
x2.start()
for thread in threads:
    thread.join()
