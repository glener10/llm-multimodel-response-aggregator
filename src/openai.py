from openai import AsyncOpenAI

from src.env import get_openai_api_key


async def exec_openai_async(model_name: str, prompt: str) -> str:
    try:
        async with AsyncOpenAI(api_key=get_openai_api_key()) as client:
            messages = [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                    ],
                }
            ]

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
