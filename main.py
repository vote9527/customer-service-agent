from graph.workflow import build_graph
from langchain_core.messages import HumanMessage


app = build_graph()


config = {
    "configurable": {
        "thread_id": "user_001"
    }
}


def main():

    print("企业客服 Agent 启动")


    while True:

        user_input = input("\n用户：").strip()


        if user_input.lower() in [
            "quit",
            "exit",
            "退出",
        ]:
            break


        result = app.invoke(
            {
                "messages": [
                    HumanMessage(
                        content=user_input
                    )
                ]
            },
            config=config
        )


        print(
            "客服：",
            result["messages"][-1].content
        )


if __name__ == "__main__":
    main()