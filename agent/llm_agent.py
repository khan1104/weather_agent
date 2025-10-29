import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from tools.get_weather import get_weather
load_dotenv()
open_api_key = os.getenv("OPEN_AI_KEY")

# initialize model
llm = init_chat_model(
    model="gpt-4o-mini",
    model_provider="openai",
    temperature=0.0,
    openai_api_key=open_api_key
)

llm_with_tools = llm.bind_tools([get_weather])

def ask(query: str):
    messages = [
        SystemMessage(
            content="You are a helpful assistant. You can call tools to get weather information "
                    "for multiple cities. If the user asks for comparisons or calculations, "
                    "use the tool for each city and reason about the results. "
                    "If the question is not about weather, politely say you can only handle weather queries."
        ),
        HumanMessage(content=query)
    ]
    while True:
        response = llm_with_tools.invoke(messages)

        if getattr(response, "tool_calls", None):
            messages.append(response)
            for tool_call in response.tool_calls:
                if tool_call["name"].lower() == "get_weather":
                    tool_result = get_weather.invoke(tool_call["args"])
                    messages.append(
                        ToolMessage(content=tool_result, tool_call_id=tool_call["id"])
                    )
            continue 
        final_response = response.content.replace("\n","").strip()
        return final_response
