## Tool calling in LangChain

### Tool Binding
- Tool binding is the step where you register tools with a Language Model(LLM) so that: 
    1. The LLM know **what tools are available**
    2. It knows **What each tool does** (via description)
    3. It knows **What input format to use** (via schema)

```
llm = ChatOpenAI()
llm_with_tools = llm.bind_tools([multiply])
```

### Tool Calling
- Tool calling is the process where the LLM(Language Model) decides, during a conversation or task, that it needs to **use a specific tool(function)** - and generates a structured output with: 
- the **name of the tool**
- and the **arguments** to call it with

*The LLM does not actually run the tool - it just suggests the tool and the input arguments. The actual execution is handled by LangChain or you.*

The LLM responds with a tool call:
```
{
    "tool": "multiply",
    "args": {"a": 1, "b": 7}
}
```

### Tool Execution
- Tool execution is the step where the actual python function(tool) is run using the input arguments that the LLM suggested during tool calling.

In simple words:
***
The LLM Says:
"Hey, call the `multiply` tool with a=8 and b=7."

⚙️**Tool execution** is when you or Langchain actually run: 
`multiply(a=8, b=7)`
-> and get the result: `56`
***


