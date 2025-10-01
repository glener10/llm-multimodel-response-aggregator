from dotenv import load_dotenv
import os

load_dotenv()


def get_gemini_api_key():
    api_key = os.getenv("API_KEY_GEMINI")
    if not api_key:
        raise Exception("❌ missing API_KEY_GEMINI in .env")
    return api_key


def get_openai_api_key():
    api_key = os.getenv("API_KEY_OPENAI")
    if not api_key:
        raise Exception("❌ missing API_KEY_OPENAI in .env")
    return api_key
