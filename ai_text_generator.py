import openai

def generate_text(prompt):
    openai.api_key = "my_api"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    user_prompt = input("Введіть запит: ")
    generated_text = generate_text(user_prompt)
    print("AI відповідає:", generated_text)
