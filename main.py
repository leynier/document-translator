from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from pydantic_settings import BaseSettings, SettingsConfigDict
from typer import Typer


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    openai_api_key: str


app = Typer()
settings = Settings()  # type: ignore
openai = OpenAI(api_key=settings.openai_api_key)


@app.command()
def main():
    messages: list[ChatCompletionMessageParam] = [
        {"role": "system", "content": "You are a helpful translator."},
    ]
    while True:
        user_input = input("You: ")
        messages.append({"role": "user", "content": user_input})
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        if not response.choices or not response.choices[0].message.content:
            raise ValueError("No completions found")
        answer = response.choices[0].message.content
        print(f"Bot: {answer}")
        messages.append({"role": "assistant", "content": answer})
