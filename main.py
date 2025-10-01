import asyncio
import datetime
import google.generativeai as genai

from src.dtos.sintetizer import ProviderEnum, Sintetizer
from src.openai import exec_openai_async
from src.env import get_gemini_api_key
from src.gemini import exec_gemini_async
from src.args import get_args
from src.prompt import aggregate_responses

MODELS_TO_EXECUTE = {
    "gemini": {
        "func": exec_gemini_async,
        "models": [
            "gemini-2.5-flash-preview-05-20",
            "gemini-2.5-pro",
            "gemini-2.5-flash-lite",
        ],
    },
    "openai": {
        "func": exec_openai_async,
        "models": [
            "gpt-4o",
        ],
    },
}

SINTETIZER = Sintetizer(provider=ProviderEnum.GEMINI, model="gemini-2.5-pro")


async def main():
    args = get_args()

    genai.configure(api_key=get_gemini_api_key())

    tasks = []
    all_models_list = []
    for provider_config in MODELS_TO_EXECUTE.values():
        exec_func = provider_config["func"]
        for model in provider_config["models"]:
            tasks.append(exec_func(model, args.prompt))
            all_models_list.append(model)

    results_from_models = await asyncio.gather(*tasks)

    prompt_with_aggregated_response = aggregate_responses(results_from_models)

    execution_map = {
        ProviderEnum.GEMINI: exec_gemini_async,
        ProviderEnum.OPENAI: exec_openai_async,
    }

    if SINTETIZER.provider in execution_map:
        print(
            f"📦 using model {SINTETIZER.model} of {SINTETIZER.provider.name} as synthesizer"
        )
        sintetizador_func = execution_map[SINTETIZER.provider]
        sintetized_response = await sintetizador_func(
            SINTETIZER.model, prompt_with_aggregated_response
        )

        print("🧾 final synthesized response:")
        print(sintetized_response)
    else:
        print(f"✖️ provider dont support: {SINTETIZER.provider}")


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    print(f"🚀 starting process at {start_time}")

    asyncio.run(main())

    end_time = datetime.datetime.now()
    total_time = end_time - start_time
    print(f"⏱️  execution finished at {end_time}. Total time: {total_time}")
