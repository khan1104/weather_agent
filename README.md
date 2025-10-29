# weather AI agent using langchain + FastAPI

## To run the project locally

### 1. Clone the repository
```bash
git clone https://github.com/khan1104/weather_agent.git
```
### 2. Navigate to the project directory
```bash
cd weather_agent
```
### 3. create a .env in the root folder and add open ai key
```bash
OPEN_AI_KEY=
```
### 4. sync dependencies (it will create virtual enviornment and install all the dependencies)
```bash
uv sync
```
### 5. run the server
```bash
uv run main.py
```
### 6. open the swagger ui on http://127.0.0.1:8000/docs

---

## API used 
* https://wttr.in -> for fetching weather data by city name (free) 
* opne ai -> gpt-4o-mini as a LLM

  ---

## Working 

**1. User Query → FastAPI Endpoint**
   - The user sends a query (e.g., “What’s the weather in Delhi?”) to the /ask endpoint.

**2. LLM Initialization (OpenAI GPT)**
   - The app uses LangChain’s init_chat_model() to initialize the GPT-4o-mini model from OpenAI

**3. Tool Binding (Weather Function)**
   - A custom Python function get_weather(city: str) is defined as a LangChain tool using the @tool decorator.
   - This function fetches real-time weather data from the wttr.in API.
   - he tool is then bound to the LLM using llm.bind_tools([get_weather]).

**4. System and Human Messages Setup**
   - A system prompt defines the assistant’s behavior.
   - The user query is wrapped as a HumanMessage

**5. Reasoning & Tool Calling Loop**
   - The model analyzes the user query.
   - If it needs external data, it automatically triggers a tool call (e.g., calls get_weather for “Delhi”).
   - The app executes that tool, retrieves the data, and passes the result back to the model via a ToolMessage

**6.Multi-Step Reasoning**
   - If multiple cities or calculations are involved (e.g., “Sum of temperatures in Delhi and Mumbai”),
the LLM calls the weather tool multiple times, gets results for each city, and performs reasoning to combine them.

**7. Final Response Generation**
   - Once all tool calls are completed, the model generates a natural-language answer (e.g.,
“The temperature in Delhi is +28°C and in Mumbai is +33°C. Their sum is 61°C.”).

**8. Clean Output to Client**
  - The final message is stripped of unnecessary newline characters and returned as a clean string JSON response:


