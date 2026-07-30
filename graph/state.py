from typing import TypedDict, Annotated, Optional
from langgraph.graph import add_messages, message
from langchain_core.messages import BaseMessage

class CustomerState(TypedDict):
    # 对话历史
    messages: Annotated[
        list[BaseMessage],
        add_messages
    ]
    # 用户信息
    used_id: Optional[str]
    # 当前意图
    intent: Optional[str]
    # 工具执行结果
    tool_result: Optional[str]
    # 最终回复
    final_answer: Optional[str]