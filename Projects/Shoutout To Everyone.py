import win32com.client

def Shoutout_Everyone(Name):
    speaker=win32com.client.Dispatch("SAPI.SpVoice")
    y=(f"Shoutout To {Name} !!")
    speaker.Speak(y)    
Shoutout_Everyone("Yash")









# import win32com.client
  
# # Calling the Dispatch method of the module which 
# # interact with Microsoft Speech SDK to speak
# # the given input from the keyboard
  
# speaker = win32com.client.Dispatch("SAPI.SpVoice")
  
# while 1:
#     print("Enter the word you want to speak it out by computer")
#     s = input()
#     speaker.Speak(s)
  