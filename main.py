import time

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

        if not user_input:
            continue

        if user_input.lower() in [
            "quit",
            "exit",
            "退出",
        ]:
            logger.info(
                "用户退出 Agent"
            )
            break


        logger.info(
            f"用户输入：{user_input}"
        )


        start_time = time.time()


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


        cost = time.time() - start_time


        answer = (
            result["messages"][-1]
            .content
        )


        logger.info(
            f"Agent耗时:{cost:.2f}s"
        )


        logger.info(
            "客服回复：%s",
            answer
        )


        print(
            "客服：",
            answer
        )



if __name__ == "__main__":
    main()