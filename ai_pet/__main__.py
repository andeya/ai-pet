# type: ignore[attr-defined]
# Use a pipeline as a high-level helper
from gpt4all import GPT4All
from transformers import AutoModel, Pipeline, pipeline

from ai_pet.config import app_config, logger, wrap_log
from ai_pet.gpt4all_app import app

MODEL_ROOT = "/Users/andeya/Library/Application Support/nomic.ai/GPT4All/"


def main():
    app()
    # chat = gpt4all_chat()
    # while True:
    #     user_input = input("User: ")  # 获取用户的输入
    #     model_output = chat(user_input)
    #     print(f"Bot: {model_output}")


if __name__ == "__main__":
    main()


def standard_chat():
    model = AutoModel.from_pretrained(MODEL_ROOT + "phi-2.Q4_0.gguf")
    pipe = pipeline(
        "text-generation",
        model=model,
        trust_remote_code=True,
    )

    def chat(user_input: str) -> str:
        return pipe(user_input)[0]["generated_text"]

    return chat


def gpt4all_chat():
    """
    https://pypi.org/project/gpt4all/
    """
    model_name = "phi-2.Q4_0.gguf"
    model = GPT4All(model_name=model_name, model_path=MODEL_ROOT)

    def chat(user_input: str) -> str:
        response_generator = model.generate(
            user_input,
            max_tokens=1000,
            temp=0.9,
            top_k=40,
            top_p=0.9,
            min_p=0.0,
            repeat_penalty=1.1,
            repeat_last_n=64,
            n_batch=9,
        )
        return response_generator

    return chat
