import openai

def get_responce(prompt):
    API_KEY = ""
    openai.api_key = API_KEY
    responce = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages= [
            {"role": "system", "content": "You are a Nutritionist who assist on the diet for a healthy body."},
            {"role": "user", "content": prompt}
        ],
    )

    return responce