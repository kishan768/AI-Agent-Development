from openai import OpenAI
import asyncio
from dotenv import load_dotenv

import os

load_dotenv()

# create Ai client

client=OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)
from mcp_client import (
    connect,disconnect,discover_tools,execute_tool
)
def build_tool_descriptions(tools):
    descriptions=""
    for tool in tools:
        descriptions +=f"""
        Tool:{tool.name}
        Description:{tool.description}
        -----------------------------
    """
    return descriptions

def planner(user_request,tools):
    tool_descriptions=build_tool_descriptions(
        tools
    )
    prompt=f"""
    You are an AI Planner.
    Available Tools
    {tool_descriptions}
    Instructions
    1. Select the best tool.
    2.Reply ONLY with the tool name.
    3.Do not explain.
    User_request
    {user_request}
    """
    response=client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )
    tool_name=response.choices[0].message.content
    return tool_name.strip()

def generate_response(user_request,tool_result):
    prompt=f"""
    The User asked:{user_request}
    The tool return:{tool_result}
    Answer naturally.
        """
    response=client.chat.completions.create(
    model=os.getenv("MODEL"),
    
    messages=[
        {
            "role":"user",
            "content":prompt
        }
    ]
    )
    return response.choices[0].message.content

async def main():
    client=await connect()
    tools=await discover_tools(client)
    print()
    print("Available tools")
    print("================")
    for tool in tools:
        print(tool.name)

    # await discover_tools(client)
    user_request=input("User:")
    tool_name=planner(
        user_request,
        tools
    )
    print()
    print(
        "Planner Selected:",
        tool_name
    )
    tool_result=await execute_tool(client,tool_name)

    final_answer=generate_response(user_request,tool_result)
    print()
    print(final_answer)

    await disconnect(client)


if __name__=="__main__":
    asyncio.run(main())