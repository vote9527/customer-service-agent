from langchain_core.messages import HumanMessage

from graph.workflow import build_graph


def test_customer_agent(question: str):

    result = app.invoke(
        {
            "messages": [
                HumanMessage(
                    content=question
                )
            ]
        }
    )

    print("\n======================")
    print("用户：")
    print(question)

    print("\nAgent回复：")
    for msg in result["messages"]:
        print(type(msg))
        print(msg)
        print(
            msg.content
        )


if __name__ == "__main__":

    app = build_graph()

    test_cases = [

        "退款需要什么条件？",

        "商品多久发货？",

        "我的订单 ORD-12345678",

        "我要投诉物流问题",

        "你好，你是谁？"

    ]


    for question in test_cases:

        test_customer_agent(question)