import google.generativeai as genai
from google.generativeai import types


async def exec_gemini_async(model_name: str, prompt: str) -> str:
    try:
        model = genai.GenerativeModel(
            model_name=model_name,
            generation_config=types.GenerationConfig(
                response_mime_type="text/plain",
            ),
        )
        print(f"🧠 firing model: {model_name}")
        response = await model.generate_content_async(
            contents=[
                prompt,
            ]
        )

        print(f"✅ model finished: {model_name}")
        return response.text
    except Exception as e:
        print(f"⚠️  error call gemini model {model_name}: {e}")
        return ""
