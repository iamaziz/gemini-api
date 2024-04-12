# Gemini-API https://ai.google.dev/tutorials/python_quickstart
import google.generativeai as genai

from secret import GOOGLE_API_KEY # To get API Key: https://aistudio.google.com/app/apikey

genai.configure(api_key=GOOGLE_API_KEY)

MODELS = [
    "models/gemini-pro",  # Gemini Pro (limit: 30720 tokens)
    "models/gemini-1.5-pro-latest",  # Gemini 1.5 Pro (limit: 1M tokens)
    "models/gemini-pro-vision",  # Gemini Pro Vision (limit: 12288 tokens)
    "models/embedding-001",  # Embedding model with (limit: 2048 tokens)
]


class Gemini:
    def __init__(self, model_name="models/gemini-1.5-pro-latest"):
        self.model = genai.GenerativeModel(model_name)

    def generate_text(self, prompt, stream=False, **kwargs):
        res = self.model.generate_content(contents=prompt, stream=stream, **kwargs)
        return res.text

    def generate_stream(self, prompt, **kwargs):
        return self.model.generate_content(prompt, stream=True, **kwargs)

    @staticmethod
    def print_models():
        models = list(genai.list_models())
        for m in models:
            print(m, end="\n\n")


if __name__ == "__main__":
    gemini = Gemini()
    gemini.print_models()
