from langchain_openai import ChatOpenAI

from langchain_core.messages import (
    SystemMessage,
)

from graph.state import CustomerState

from config.settings import (
    DASHSCOPE_API_KEY,
    BASE_URL,
    MODEL_NAME,
    TEMPERATURE,
)

from tools import TOOLS

from utils.trace import AgentTracer


llm = ChatOpenAI(
    model=MODEL_NAME,
    temperature=TEMPERATURE,
    api_key=DASHSCOPE_API_KEY,
    base_url=BASE_URL
)


llm_with_tools = llm.bind_tools(
    TOOLS
)


SYSTEM_PROMPT = """

你是一个企业智能客服 Agent。


你的职责：

1. 解答用户产品问题
2. 查询 FAQ
3. 查询订单
4. 查询企业政策
5. 提交售后投诉


你可以使用：

- search_faq
- search_policy
- check_order
- submit_complaint


规则：

1.
可以通过工具获取的信息，必须调用工具。


2.
禁止编造订单信息。


3.
禁止编造企业政策。


4.
投诉问题必须调用 submit_complaint。


5.
工具返回后，根据工具结果回答。


6.
保持专业客服语气。


严格要求：

退款、售后、保修、优惠、支付等问题：
必须调用 search_policy。


回答政策问题：
只能使用工具返回内容。


知识库没有内容：
明确说明。


"""


def agent_node(
    state: CustomerState
):

    tracer = AgentTracer()

    


    try:

        messages = list(
            state["messages"]
        )
        tracer.start(
            node="agent_node",
            input=messages[-1].content
        )

        # 添加 System Prompt

        if not any(
            isinstance(
                m,
                SystemMessage
            )
            for m in messages
        ):

            messages.insert(
                0,
                SystemMessage(
                    content=SYSTEM_PROMPT
                )
            )


        response = (
            llm_with_tools
            .invoke(messages)
        )

        tracer.end(
            response.content
        )
        return {
            "messages":[
                response
            ]
        }


    except Exception as e:
        tracer.end(f"ERROR: {e}")
        raise

        