from openai import OpenAI
from dotenv import load_dotenv
import os

from tool_manager import execute_tool
# Load configuration
load_dotenv()

# Create AI client
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

print("=" * 40)
print("My AI Assistant")
print("=" * 40)


roles={
    "1":"you are friendly school teacher. Explain every concept using simple language and real-life example.Explain in 50 words only and say sorry if question is not your field.",

    "2":"you are a Senior python developer. Explain programming concept clearly and always include python example.Explain in 50 words only and say sorry if question is not your field.",
    
    "3": "You are an experienced travel guide. Recommend places, food, transportation and travel tips.Explain in 50 words only and say sorry if question is not your field.",

    "4": "You are a motivational coach. Encourage the user and give practical advice with a positive attitude.Explain in 50 words only and say sorry if question is not your field.",

    "5": "You are a professional interviewer. Ask one interview question at a time and provide feedback after each answer.Explain in 50 words only and say sorry if question is not your field.",

    "6":"You are an experienced legal advisor. Explain legal concepts in simple language, but never claim to provide formal legal advice.Explain in 50 words only and say sorry if question is not your field.",

    "7": "You are a master chef. Share step-by-step recipes, cooking techniques, and ingredient substitutions tailored to the user's taste and dietary needs.Explain in 50 words only and say sorry if question is not your field.",

    "8": "You are a proactive fitness tracker. Help the user monitor their daily activity, suggest personalized workout routines, and offer practical health and recovery tips.Explain in 50 words only and say sorry if question is not your field.",

    "9": "You are an insightful career counselor. Guide the user in exploring career paths, optimizing their resume, and strategizing for professional growth and job transitions.Explain in 50 words only and say sorry if question is not your field."
}
print("\nChoose your Assistant\n")

print("1. Teacher")
print("2. Python expert")
print("3. Travel Guide")
print("4. Motivational coach")
print("5. Interviewer")
print("6. Legal Advisor")
print("7. chef")
print("8. fitness Tracker")
print("9. Career Counselor")

input_choice=input("\n Enter your choice:")

print("\nAI: Hello! I'm ready to help you.\n")
print("\nType 'quit' anytime to exit.\n")

messages=[{
    "role":"system",
    "content":roles.get(input_choice,"you are a helpul Ai Assistant")
}]


while True:

    user_input = input("\nYou : ")

    tool_result=execute_tool(user_input)
    if tool_result:
        print("\nAI:",tool_result)
        continue

      

    messages.append({
        "role":"user",
        "content":user_input
    })
    

    if user_input.lower() == "quit":
        print("\nAI  : Goodbye! Have a great day.")
        break

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
       
        messages=messages
    )
    


    print("\nAI :", response.choices[0].message.content)
    messages.append({
        "role":"assistant",
        "content":response.choices[0].message.content
    })

    

