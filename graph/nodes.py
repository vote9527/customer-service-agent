from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from langchain_core.messages import AIMessage

from graph.state import CustomerState
from config.settings import DASHSCOPE_API_KEY
from tools import TOOLS


llm = ChatOpenAI(
    model="qwen-plus",
    temperature=0.7,
    api_key=DASHSCOPE_API_KEY,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)


# LLM 绑定工具
llm_with_tools = llm.bind_tools(TOOLS)


def agent_node(
    state: CustomerState
) -> dict:
    """
    Agent 核心节点

    负责：
    1. 获取当前对话消息
    2. 调用 LLM
    3. 根据用户需求决定是否调用工具
    """

    messages = state["messages"]

    # 如果当前消息中没有 SystemMessage
    # 则添加系统提示词
    if not any(
        isinstance(message, SystemMessage)
        for message in messages
    ):

        messages = [
            SystemMessage(
                content="""
你是一个企业智能客服 Agent。

你的职责：

1. 解答用户的产品和服务问题
2. 查询 FAQ
3. 查询订单
4. 提交投诉

你可以使用以下工具：

- search_faq：查询 FAQ
- check_order：查询订单
- submit_complaint：提交投诉

工作规则：

1. 如果用户的问题可以通过工具获取信息，
   优先调用工具。

2. 不要编造订单信息。

3. 不要编造 FAQ 内容。

4. 如果需要提交投诉，
   必须调用 submit_complaint。

5. 工具执行完成后，
   根据工具返回结果向用户提供最终回答。

6. 保持专业、友好的客服语气。
                """
            )
        ] + messages

    # 调用 LLM
    response = llm_with_tools.invoke(
        messages
    )

    # 返回 State 更新
    return {
        "messages": [response]
    }