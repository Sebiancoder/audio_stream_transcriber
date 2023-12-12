from audio_streamer import AudioStreamer
from transcriber import Transcriber
import time

class CrimeTranscriber:

    stream_url = None
    pyaud = None

    def __init__(self):

        pass

    def transcribe(self):

        print("starting to transcribe")
        
        aud_streamer = AudioStreamer(stream_url=self.stream_url)
        aud_transcriber = Transcriber()

        aud_streamer.start()
        aud_transcriber.start()

        while True:

            time.sleep(1)

    def set_stream_url(self, stream_url):

        self.stream_url = stream_url

if __name__ == "__main__":

    ct = CrimeTranscriber()
    ct.set_stream_url("https://broadcastify.cdnstream1.com/40318")
    ct.transcribe()
