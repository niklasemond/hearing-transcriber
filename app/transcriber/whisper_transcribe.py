import whisper

class WhisperTranscriber:
    def __init__(self):
        self.model = whisper.load_model("medium")
    
    def transcribe(self, audio_file):
        """Transcribes audio using OpenAI Whisper."""
        print(f"\nTranscribing {audio_file}")
        
        result = self.model.transcribe(
            audio_file,
            fp16=False,
            language='en',
            initial_prompt="This is a congressional hearing transcript.",
            verbose=False
        )
        
        return [{"text": segment["text"],
                "start_time": segment["start"],
                "end_time": segment["end"]} 
                for segment in result["segments"]]