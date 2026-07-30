from graph.state import CustomerState
from langchain_core.messages import AIMessage

def intent_node(
    state: CustomerState
):
    """
    意图识别节点

    输入:
    用户消息

    输出:
    intent
    """
    last_message = state["messages"][-1]
    text = last_message.content

    if "退款" in text:
        intent = "refund"

    elif "订单" in text:
        intent = "order"

    else:
        intent = "general"

    return {
        "intent": intent
    }

def agent_node(
    state: CustomerState
):
    """
    Agent核心节点

    后续这里接LLM
    """
    intent = state.get("intent")

    if intent == "refund":

        answer = (
            "您的退款申请已经收到，"
            "退款政策是7天内无理由退款。"
        )


    elif intent == "order":

        answer = (
            "正在帮您查询订单状态。"
        )


    else:

        answer = (
            "您好，请问有什么可以帮助您的？"
        )

    return {
        "messages":[
            AIMessage(
                content=answer
            )
        ],
        "final_answer":answer
    }
