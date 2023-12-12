import threading
import time
import requests
import pyaudio
import array
from pydub import AudioSegment
from pydub.playback import play
import pyaudio
from io import BytesIO
import noisereduce

class AudioStreamer (threading.Thread):

   stream_url = None
   play_audio = True

   chunk_num = 0
   
   def __init__(self, iteration=0, stream_url=None, play_audio=True):

        threading.Thread.__init__(self, daemon=True)
        self.name = "audio_streamer_{iteration}".format(iteration="iteration")

        self.stream_url = stream_url
        self.play_audio = play_audio

        self.chunk_num = 0

   def run(self):
      
        print("Starting stream")
        
        if self.stream_url is None:

            print("Must set Stream URL")

            return

        r = requests.get(self.stream_url, stream=True)

        for chunk in r.iter_content(chunk_size=8096):

            audio_seg = AudioSegment.from_file(BytesIO(chunk), "mp3")

            # print(type(audio_seg))

            #audio_seg_nr = noisereduce.reduce_noise(y=audio_seg, sr=7000)

            play(audio_seg)

            with open("audio_chunks/chunk_{cn}.mp3".format(cn=self.chunk_num), 'wb') as f: 
                f.write(chunk)

            self.chunk_num += 1

        output_stream.stop_stream()
        output_stream.close()

        print("Ending stream")
        
        return