import base64
import pathlib
from openai import AsyncOpenAI

from src.env import get_openai_api_key
from src.utils.image import get_image_mime_type


async def exec_openai_async(model_name: str, args) -> str:
    try:
        async with AsyncOpenAI(api_key=get_openai_api_key()) as client:
            messages = [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": args.prompt},
                    ],
                }
            ]
            if getattr(args, "input", None):
                mime_type = get_image_mime_type(args.input)
                filepath = pathlib.Path(args.input)
                image_data = filepath.read_bytes()
                base64_image = base64.b64encode(image_data).decode("utf-8")
                image_url = f"data:{mime_type};base64,{base64_image}"
                messages[0]["content"].append({
                    "type": "image_url",
                    "image_url": {"url": image_url}
                })

            print(f"🧠 firing model: {model_name}")
            response = await client.chat.completions.create(
                model=model_name,
                messages=messages,
                response_format={"type": "text"},
                max_tokens=300,
            )

            response_text = response.choices[0].message.content
            print(f"✅ model finished: {model_name}")
            return response_text
    except Exception as e:
        print(f"⚠️  error call openai model {model_name}: {e}")
        return ""
