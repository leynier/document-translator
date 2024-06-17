from json import dumps, loads

from openai import OpenAI
from openai.types import ChatModel
from openai.types.chat import ChatCompletionMessageParam

from ..settings import settings

openai = OpenAI(api_key=settings.openai_api_key)


def translate(
    texts: list[str],
    language_source: str,
    language_target: str,
    model: ChatModel = "gpt-4o",
    repeat: int = 5,
) -> list[str]:
    return __translate(
        texts,
        language_source.title(),
        language_target.title(),
        model,
        0,
        repeat,
    )


def __translate(
    texts: list[str],
    language_source: str,
    language_target: str,
    model: ChatModel,
    iteration: int,
    repeat: int,
) -> list[str]:
    try:
        if iteration == 0:
            print(f"Translating texts: try {iteration + 1}")
        messages: list[ChatCompletionMessageParam] = [
            {
                "role": "system",
                "content": f"""
                    You are an expert translator from {language_source} to {language_target}.
                    Everything the user writes should simply be translated into {language_target}.
                    The user will send a JSON with a list of texts, and the response should
                    be another JSON with the list of translations.

                    For example, a translation from Spanish to English would look like this:

                    Input example: ["Hola, ¿cómo estás?", "Estoy bien, gracias."]
                    Output example: ["Hello, how are you?", "I'm fine, thank you."]
                """,
            },
            {
                "role": "user",
                "content": dumps(texts),
            },
        ]
        response = openai.chat.completions.create(
            model=model,
            messages=messages,
            response_format={"type": "json_object"},
        )
        if not response.choices or not response.choices[0].message.content:
            raise ValueError("Invalid response")
        translate_text = response.choices[0].message.content
        result = loads(translate_text)
        if isinstance(result, dict):
            result = list(result.values())
        if (
            isinstance(result, list)
            and len(result) == 1
            and isinstance(result[0], list)
        ):
            result = result[0]
        if (
            not isinstance(result, list)
            or len(result) != len(texts)
            or any(not isinstance(text, str) for text in result)
        ):
            raise ValueError("Invalid response")
        print(f"Translated texts successfully in the iteration {iteration + 1}")
        return result
    except Exception:
        if iteration < repeat:
            return __translate(
                texts,
                language_source,
                language_target,
                model,
                iteration + 1,
                repeat,
            )
        print("Failed to translate texts")
        return texts
