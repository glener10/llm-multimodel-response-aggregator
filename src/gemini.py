import pathlib
import google.generativeai as genai
from google.generativeai import types

from src.utils.image import get_image_mime_type


async def exec_gemini_async(model_name: str, args) -> str:
    try:
        contents = [args.prompt]
        if getattr(args, "input", None):
            mime_type = get_image_mime_type(args.input)
            filepath = pathlib.Path(args.input)
            contents.append({"mime_type": mime_type, "data": filepath.read_bytes()})
        
        model = genai.GenerativeModel(
            model_name=model_name,
            generation_config=types.GenerationConfig(
                response_mime_type="text/plain",
            ),
        )
        print(f"🧠 firing model: {model_name}")
        response = await model.generate_content_async(
            contents=[
                args.prompt,
            ]
        )

        print(f"✅ model finished: {model_name}")
        return response.text
    except Exception as e:
        print(f"⚠️  error call gemini model {model_name}: {e}")
        return ""
