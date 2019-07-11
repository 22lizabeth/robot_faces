"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech
from google.cloud import storage


from google.cloud.texttospeech import enums
import os
import sys
import pprint
import shlex
import subprocess
import time
import os
import subprocess
import sys
from pygame import mixer
from mutagen.mp3 import MP3

class Synthesizer:
    def __init__(self):
        if os.path.exists(os.path.dirname(__file__) + "/sawyer-demo.json"):
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.dirname(__file__) + "/sawyer-demo.json"
        else:
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "sawyer-demo.json"


        # os.system("echo $GOOGLE_APPLICATION_CREDENTIALS")
        self.client = texttospeech.TextToSpeechClient()
        self.synthesis_input = texttospeech.types.SynthesisInput(text="Hello World!")
        # Build the voice request, select the language code ("en-US") and the ssml
        # voice gender ("neutral")
        self.voice = texttospeech.types.VoiceSelectionParams(language_code='en-US', name='en-US-Wavenet-D',
                                                             ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)
        # Select the type of audio file you want returned
        self.audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)
        self.filesArray = []
        self.mixer = mixer
        self.mixer.init()

    def getMP3Length(self):
        length = 0.0
        for f in self.filesArray:
            audio = MP3(f)
            length = length + float(audio.info.length)
        return length

    def createFilePath(self, phrase):
            path = ""
            if (os.path.dirname(__file__) == ""):
                path = 'Speech_Files/'
            else:
                path = os.path.dirname(__file__) + '/Speech_Files/'
            # print path
            # print phrase
            filePath = phrase
            filePath = filePath.replace(".", "")
            filePath = filePath.replace("!", "")
            filePath = filePath.replace("'", "")
            filePath = filePath.replace(",", "")
            filePath = filePath.replace("?", "")
            filePath = filePath.replace(" ", "_")
            filePath = filePath.replace("\n", "")
            filePath = path + filePath + ".mp3"
            return filePath

    def createFiles(self, phrase):
        if len(phrase) >= 200:
            index = 100
            while phrase[index] != " ":
                index = index + 1
            self.createFiles(phrase[:index])
            self.createFiles(phrase[index + 1:])
        else:
            phrase = phrase.replace("\\", "")
            filePath = self.createFilePath(phrase)
            # print filePath
            if os.path.exists(filePath):
                self.filesArray.append(filePath)
            else:
                print ("Creating file")
                self.synthesis_input = texttospeech.types.SynthesisInput(
                    text=phrase)
                # Perform the text-to-speech request on the text input with the selected
                # voice parameters and audio file type
                response = self.client.synthesize_speech(
                    self.synthesis_input, self.voice, self.audio_config)

                # The response's audio_content is binary.
                with open(filePath, 'wb') as out:
                    # Write the response to the output file.
                    out.write(response.audio_content)
                    print('Audio content written to file ' + filePath)
                self.filesArray.append(filePath)
    
    def numFiles(self):
        return len(self.filesArray) - 1

    def say(self, phrase):
        x = 0
        self.mixer.music.load(self.filesArray[x])
        # time.sleep(1.5)
        self.mixer.music.play()
        # print len(self.filesArray)
        while True:
            pos = self.mixer.music.get_pos()
            if int(pos) == -1:
                x += 1
                if x == len(self.filesArray):
                    break
                self.mixer.music.load(self.filesArray[x])
                self.mixer.music.play()

        self.filesArray = []

    def list_voices(self):
        """Lists the available voices."""

        # Performs the list voices request
        voices = self.client.list_voices()

        for voice in voices.voices:
            # Display the voice's name. Example: tpc-vocoded
            print('Name: {}'.format(voice.name))

            # Display the supported language codes for this voice. Example: "en-US"
            for language_code in voice.language_codes:
                print('Supported language: {}'.format(language_code))

            ssml_gender = enums.SsmlVoiceGender(voice.ssml_gender)

            # Display the SSML Voice Gender
            print('SSML Voice Gender: {}'.format(ssml_gender.name))

            # Display the natural sample rate hertz for this voice. Example: 24000
            print('Natural Sample Rate Hertz: {}\n'.format(
                voice.natural_sample_rate_hertz))


def main(args):

    synthesizer = Synthesizer()
    fileName = "Speech_Files/" + args[1] + ".mp3"
    synthesizer.say(args[1])
    # f = open("phrases.txt", "r+")
    # f1 = f.readlines()
    # for x in f1:
    #     fileName = x.replace("\n", "") + '.mp3'
    #     print x
    #     print fileName
    #     synthesizer.say(fileName, x)
    # synthesizer.list_voices()


if __name__ == '__main__':
    main(sys.argv)
