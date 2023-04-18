import openai

def take_response(text):
    openai.api_key = "Your api key"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a chatbot"},
                {"role": "user", "content": text},
            ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    message = take_response("hi")
    print(f"Bot: {message}")
