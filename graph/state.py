from typing import TypedDict, Annotated, Optional
from langgraph.graph import add_messages
from langchain_core.messages import BaseMessage

class CustomerState(TypedDict):
    # 对话历史
    messages: Annotated[
        list[BaseMessage],
        add_messages
    ]
    # 用户信息
    user_id: Optional[str]
    # 当前意图
    intent: Optional[str]
    # 工具执行结果
    tool_result: Optional[str]
    # 最终回复
    final_answer: Optional[str]
    # 当前技能名字
    current_skill: Optional[str]
    # 技能内容
    skill_prompt: Optional[str]