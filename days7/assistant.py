from openai import OpenAI;
from dotenv import load_dotenv
import os
load_dotenv()

from planner import choose_tool

from tools import (
    get_current_time,
    roll_dice,generate_password
)

client=OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

print("="*40)
print(" My Ai Assistant")
print("="*40)

while True:
    user_input=input("\n you: ")
    if user_input.lower()=='quit':
        print('\nAI:Thank you 🥰 see you again')
        break
    tool=choose_tool(user_input)
    if tool=="get_current_time":
        result=get_current_time()
    elif tool=="roll_dice":
        result=roll_dice()
    elif tool=="generate_password":
        result=generate_password()
    else:
        result=None

    prompt=f"""
    The user asked:
    {user_input}
    The tool return:
    {result}
    Answer the user naturally.
    """
    response=client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[
            {
                "role":"system",
                "content":"Answer the question from the tools"
            },{
                "role":"user",
                "content":prompt
            }
        ]
    )
    print("\nAI:",response.choices[0].message.content)