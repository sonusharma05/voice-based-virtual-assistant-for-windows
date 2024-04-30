
import azure.cognitiveservices.speech as speechsdk
import os
import subprocess 
from datetime import datetime
import google.generativeai as genai

genai.configure(api_key='#your Gemini API key')
model = genai.GenerativeModel('gemini-pro')

speech_key, service_region = "#your Azure speech recogination key", "#your key region"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)


print("Say something...")
result = speech_recognizer.recognize_once()
print(result.text)
if(result.text==""):
     print("sorry i didn't hear that")
     speech_synthesis_result = speech_synthesizer.speak_text_async("sorry i didn't hear that").get()
     
# Checks result.
elif (result.text=="Open Calculator."):
    speech_synthesis_result = speech_synthesizer.speak_text_async("opening calculator").get()
    print("opening calculator")
    subprocess.Popen("C:\\Windows\\system32\\calc.exe")

elif(result.text=="Open Chrome."):
    speech_synthesis_result = speech_synthesizer.speak_text_async("opening Chrome").get()
    print("opening Chrome")
    subprocess.Popen("C:\\Program Files\\Google\\Chrom\\Application\\chrome.exe")

elif(result.text=="Open Word."):
    speech_synthesis_result = speech_synthesizer.speak_text_async("opening Word").get()
    print("opening Word")
    subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")

elif(result.text=="Open Excel."):
    speech_synthesis_result = speech_synthesizer.speak_text_async("opening Excel").get()
    print("opening Excel")
    
    subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")

elif(result.text=="Open Edge."):
    speech_synthesis_result = speech_synthesizer.speak_text_async("opening Edge").get()
    print("opening Edge")
    subprocess.Popen("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
    
elif(result.text=="Open Notepad."):
    speech_synthesis_result = speech_synthesizer.speak_text_async("opening Notepad").get()
    print("opening Notepad")
    subprocess.Popen("C:\\Windows\\System32\\notepad.exe")

elif(result.text=="Open Outlook."):
    speech_synthesis_result = speech_synthesizer.speak_text_async("opening Outlook").get()
    print("opening Outlook")
    subprocess.Popen("C:\\Program Files\\WindowsApps\\Microsoft.OutlookForWindows_1.2024.403.300_x64__8wekyb3d8bbwe\\olk.exe")

elif(result.text=="Open Paint."):
    speech_synthesis_result = speech_synthesizer.speak_text_async("opening paint").get()
    print("opening Paint")
    subprocess.Popen("C:\\Program Files\\WindowsApps\\Microsoft.Paint_11.2402.32.0_x64__8wekyb3d8bbwe\\PaintApp\\mspaint.exe")

elif(result.text=="Open whiteboard."):
    speech_synthesis_result = speech_synthesizer.speak_text_async("opening Whiteboard").get()
    print("opening Whiteboard")
    subprocess.Popen("C:\\Program Files\\WindowsApps\\Microsoft.Whiteboard_53.21110.548.0_x64__8wekyb3d8bbwe\\MicrosoftWhiteboard\\MicrosoftWhiteboard.exe")

elif(result.text=="Open camera."):
     speech_synthesis_result = speech_synthesizer.speak_text_async("opening Camera").get()
     print("opening Camera")
     subprocess.Popen("C:\\Program Files\\WindowsApps\\Microsoft.WindowsCamera_2024.2402.5.0_x64__8wekyb3d8bbwe\\WindowsCamera.exe")
elif(result.text=="Open whatsApp." or result.text=="Open WhatsApp."):
     print("opening WhatsApp")
     speech_synthesis_result = speech_synthesizer.speak_text_async("opening WhatsApp").get()
     subprocess.Popen("C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2414.8.0_x64__cv1g1gvanyjgm\\WhatsApp.exe")    
    
    

elif (result.text=="Open CMD." or result.text=="Open command prompt."):
    subprocess.Popen("C:\\Windows\\system32\\cmd.exe")

elif(result.text=="Time." or result.text=="What is the time."):
        time=str(datetime.now().time())
        c=time[0:5]
        print("the time is",c)  
        speech_synthesis_result = speech_synthesizer.speak_text_async("the time is").get()
        speech_synthesis_result = speech_synthesizer.speak_text_async(c).get()
        

else:
   
    print("Intialing websearch please Wait")
    speech_synthesis_result = speech_synthesizer.speak_text_async("Intialing websearch please Wait").get()
    text2=model.generate_content(result.text)
    print(text2.text)
    speech_synthesis_result = speech_synthesizer.speak_text_async(text2.text[0:200]).get()

    
