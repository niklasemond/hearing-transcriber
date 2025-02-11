from pyannote.audio import Pipeline
import os

class SpeakerDiarizer:
    def __init__(self):
        self.pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization",
                                               use_auth_token=os.getenv("HF_TOKEN"))
    
    def diarize(self, audio_file):
        """Performs speaker diarization (who said what)."""
        print("Processing speaker identification...")
        diarization = self.pipeline(audio_file)
        
        speakers = {}
        for turn, _, speaker in diarization.itertracks(yield_label=True):
            speakers.setdefault(speaker, []).append((turn.start, turn.end))
        
        print(f"Found {len(speakers)} distinct speakers")
        return speakers