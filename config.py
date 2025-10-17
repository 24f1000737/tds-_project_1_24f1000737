# config.py
from pydantic_settings import BaseSettings
from functools import lru_cache

# Define the structure for all required secrets/config
class Settings(BaseSettings):
    # API Keys/Tokens
    GEMINI_API_KEY: str = "AIzaSyDvF6Atg6RpSnGDH814wsdg6JnjxlTkQJA"
    GITHUB_TOKEN: str = "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"
    
    # Project-specific variables
    STUDENT_SECRET: str = "hi_avisikta"
    GITHUB_USERNAME: str = "24f1000737"
    
    # Define which file to load settings from
    model_config = {"env_file": ".env", "extra": "ignore"}

# Use lru_cache to load the settings only once, improving performance
@lru_cache()
def get_settings():
    """Returns the cached settings object."""
    return Settings()