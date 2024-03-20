import sounddevice as sd
import numpy as np
import whisper
import queue
from pydub import AudioSegment
from pydub.playback import play

audiobuffer = queue.SimpleQueue

duration = 5        # Duration of the recording in seconds
fs = 44100          # Sampling frequency
channels = 2        # Number of channels
sample_width = 2    # 16-bit audio
threshold = 0.1


def record_audio(duration, fs, channels):
    print("Recording.")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=channels, dtype='float32')
    sd.wait()
    print("Finished.")
    return audio_data

def prepare_audio(audio_data, sample_width, channels, framerate):

    # TODO: Check if audio is only silence.
    if (np.sqrt(np.mean(audio_data**2)) > threshold):
        pass

    # Convert audio data to bytes
    audio_bytes = (audio_data * (2 ** (8 * sample_width - 1))).astype(np.int16).tobytes()

    # Create an AudioSegment object from the bytes
    audio_segment = AudioSegment(
        audio_bytes,
        sample_width=sample_width,
        channels=channels,
        frame_rate=framerate
    )

    if audio_segment.frame_rate != 16000: # 16 kHz
        audio_segment = audio_segment.set_frame_rate(16000)
    if audio_segment.sample_width != 2:   # int16
        audio_segment = audio_segment.set_sample_width(2)
    if audio_segment.channels != 1:       # mono
        audio_segment = audio_segment.set_channels(1)        
    arr = np.array(audio_segment.get_array_of_samples())
    return arr.astype(np.float32)/32768.0


audio_data = record_audio(duration, fs, channels)
audio = prepare_audio(audio_data, sample_width, channels, fs)
model = whisper.load_model("base")
result = model.transcribe(audio, fp16=False)
print(result['text'])