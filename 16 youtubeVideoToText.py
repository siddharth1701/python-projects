import pafy
import os  
from pydub import AudioSegment
import speech_recognition as sr

# audio file output name
src = "audio.m4a"
dst = "audio.wav"

url = input("Please enter Youtube URL: ")
video = pafy.new(url)

# allstreams = video.allstreams
# for s in allstreams:
#     print(s.mediatype, s.extension, s.quality)


try:
    print("Step - 1 : Downloading Youtube audio from source")
    try:
        bestaudio = video.getbestaudio()    # selecting best audio
        value = video.getbestaudio().generate_filename()   # generating filename
        print("Download begins...")
        bestaudio.download()   # downloading audio 
        print("File downloaded and renaming...")
        print("File Name : " + str(value))   # printing the value
        os.rename(value,'audio.'+value[-3:])   # renaming with default name
        print("Successfully file downloaded and renamed.")
    except sr.UnknownValueError:
        print("Error")
    except sr.RequestError:
        print("Failed".format(e))
    except:
        print("Failed to Download youtube audio.")

    
    print("#"*60)
    print("Step - 2 : Now converting audio format to suitable format")
    # convert m4a to wav
    print("Converting m4a to wav... ")
    try:
        sound = AudioSegment.from_file(src, "m4a")
        sound.export(dst, format="wav")
        os.remove("audio.m4a")
        print("Successfully converted to wav format.")
    except:
        print("Failed to convert audio format")
    
    print("#"*60)
    print("Step - 3 : Converting audio to text ...")
    speech_r = sr.Recognizer()
    with sr.AudioFile("audio.wav") as source:
        # speech_audio = speech_r.listen(source)
        speech_audio = speech_r.record(source)
        try:
            speech_text = speech_r.recognize_google(speech_audio)   # convert audio file into text and store it in speech_audio
            print("Print text from audio")
            print(speech_text)

            with open("Output.txt", "w") as text_file:
              print(f"Speech to Text: {speech_text}", file=text_file)
        except Exception as e:
            print("Audio file deleted", os.remove("audio.wav"))
            print("Exception: "+ str(e))
            print("Please try again!")
        
# except:
except Exception as e:
    print("Audio file deleted", os.remove("audio.wav"))
    print("Exception: "+ str(e))
    print('Sorry could not download or failed to convert to failed to convert text.')