from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

client = InferenceClient(
    token=os.getenv("HF_TOKEN")
)


def ask_llm(system_prompt,
            user_prompt):

    response = (
        client.chat.completions.create(
            model="Qwen/Qwen2.5-7B-Instruct",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            max_tokens=1200
        )
    )

    return (
        response
        .choices[0]
        .message.content
    )