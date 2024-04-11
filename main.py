import os
import openai
#import sys
#print(sys.executable)

openai.api_key = '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'

chat_log = []

while True:
    user_message = input()
    if user_message.lower() == "quit":
        break
    else:
        chat_log.append({"role": "user","content":user_message})
        response = openai.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = chat_log
        )

        assistant_response = response.choices[0].message.content
        print("ChatGPT: ", assistant_response.strip("\n").strip())
        chat_log.append({"role": "user","content":assistant_response.strip("\n").strip()})

