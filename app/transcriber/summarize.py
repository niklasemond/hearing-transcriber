from openai import OpenAI

class Summarizer:
    def __init__(self):
        self.client = OpenAI()
    
    def generate_summary(self, transcript):
        """Generates an analytical summary of the congressional hearing."""
        text_data = "\n".join(f"{t['speaker']}: {t['text']}" for t in transcript)
        
        prompt = """Please provide an analytical summary of this congressional hearing that includes:
        1. Main topics discussed
        2. Key arguments or positions presented
        3. Notable exchanges between speakers
        4. Important policy implications
        5. Any significant decisions or conclusions reached"""
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert political analyst summarizing congressional hearings."},
                {"role": "user", "content": f"{prompt}\n\nHearing transcript:\n{text_data}"}
            ]
        )
        
        return response.choices[0].message.content