from graph.workflow import create_customer_graph
from langchain_core.messages import HumanMessage, content


def main():
    app = create_customer_graph()
    result = app.invoke(
    {
        "messages":[
            HumanMessage(
                content="我要退款"
            )
        ],

        "user_id":"001",

        "intent":None,

        "tool_result":None,

        "final_answer":None
    }      
    )
    print(result["final_answer"])
    

if __name__ == "__main__":
    main()
    