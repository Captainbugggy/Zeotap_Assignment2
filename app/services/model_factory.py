from app.services.gemini_service import GeminiService

class ModelFactory:
    def __init__(self):
        # Register models here
        self.models = {
            "gemini": GeminiService()
        }

    def get_model(self, model_name):
        if model_name not in self.models:
            raise ValueError(f"Model '{model_name}' not found.")
        return self.models[model_name]
