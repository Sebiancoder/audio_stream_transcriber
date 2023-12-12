# Audio Stream Transcriber

A python application that transcribes a realtime mp3 audio stream, such as an internet radio source, in realtime. 

## Implementation

This project uses the python requests library to open a streaming connection with an HTTP GET request. Audio is then decoded with pydub, and audio chunks are placed in a transcription queue. An asynchronous process uses a local instance of the OpenAI Whisper model to transcribe the audio. Depending on the model being used and the processing power of your machine, the transcription queue may clear audio chunks at a slower rate than they arrive, leading to a backlog.

## Dependencies

First, install ffpmeg by downloading the source files [here](https://ffmpeg.org/). Move to a desired location, extract the files, and add the /bin folder inside to your path environment variable.

Then install all pip dependencies by running `pip install -r requirements.txt` and you should be good to go.
