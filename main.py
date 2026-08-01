from graph.workflow import build_graph
from langchain_core.messages import HumanMessage
from utils.logger import logger

app = build_graph()


config = {
    "configurable": {
        "thread_id": "user_001"
    }
}


def main():

    print("企业客服 Agent 启动")
    print("请输入问题：")

    while True:

        user_input = input("\n用户：").strip()

        logger.info(f"用户输入：{user_input}")
        
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


        logger.info(
            "客服：%s",
            result["messages"][-1].content
        )

        print(
            "客服：",
            result["messages"][-1].content
        )


if __name__ == "__main__":
    main()