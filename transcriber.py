import threading
import time
import os
import whisper

class Transcriber (threading.Thread):
   
   model = None
   
   def __init__(self, iteration=0, stream_url=None, play_audio=True):

        threading.Thread.__init__(self, daemon=True)
        name = "audio_streamer_{iteration}".format(iteration="iteration")

        self.model = whisper.load_model("medium")

   def run(self):

        while True:

            if not os.listdir("audio_chunks"):

                #if no audio chunks to describe, continue
                continue

            else:

                target_audio_file = "audio_chunks/{taf}".format(taf=os.listdir("audio_chunks")[0])

                transcribe_result = self.model.transcribe(target_audio_file)

                print(transcribe_result["text"])
                print("")

                os.remove(target_audio_file)

        return

