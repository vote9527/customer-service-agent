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
from utils.logger import logger

from skills.loader import load_skills
from skills.router import select_skill


# =========================
# LLM
# =========================

llm = ChatOpenAI(
    model=MODEL_NAME,
    temperature=TEMPERATURE,
    api_key=DASHSCOPE_API_KEY,
    base_url=BASE_URL
)


# 绑定工具

llm_with_tools = llm.bind_tools(
    TOOLS
)


# =========================
# Skill Loader
# =========================

skills = load_skills()


logger.info(
    f"""
========== SKILL LOADER ==========

Loaded Skills:

{list(skills.keys())}

===================================
"""
)


# =========================
# Base System Prompt
# =========================

BASE_PROMPT = """

你是企业智能客服 Agent。

你的职责：

1. 解答用户产品问题
2. 查询 FAQ
3. 查询订单
4. 查询企业政策
5. 提交售后投诉


工作规则：

1.
必须根据当前 Skill 执行业务流程。


2.
工具返回的信息才能用于回答。


3.
禁止编造企业政策。


4.
禁止编造订单信息。


5.
如果需要查询信息，必须调用对应工具。


6.
保持专业客服语气。

"""


# =========================
# Agent Node
# =========================

def agent_node(
    state: CustomerState
):

    tracer = AgentTracer()


    try:

        # 获取消息

        messages = list(
            state["messages"]
        )

        last_message = messages[-1]
        
        if last_message.type == "tool":
            user_query = ""
        else: 
            user_query = (last_message.content)


        tracer.start(
            node="agent_node",
            input=user_query
        )


        # =====================
        # Skill Router
        # =====================
        if user_query:
            skill = select_skill(user_query,skills)
        else:
            skill = ""


        if skill:

            skill_prompt = (
                skill["content"]
            )


            logger.info(
                f"""
========== SKILL LOADED ==========

Skill:

{skill["name"]}


Prompt:

{skill_prompt}


===================================
"""
            )


        else:

            skill_prompt = ""


            logger.warning(
                f"""
========== NO SKILL ==========

Query:
{user_query}

==============================
"""
            )


        # =====================
        # Dynamic System Prompt
        # =====================

        system_prompt = (
            BASE_PROMPT
            +
            """

当前业务 Skill:

"""
            +
            skill_prompt
        )


        # =====================
        # 关键修复:
        # 删除旧 SystemMessage
        # 防止 Memory 保存旧 Skill
        # =====================

        messages = [
            m
            for m in messages
            if not isinstance(
                m,
                SystemMessage
            )
        ]


        messages.insert(
            0,
            SystemMessage(
                content=system_prompt
            )
        )


        # =====================
        # LLM + Tool Calling
        # =====================

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


        tracer.end(
            f"ERROR:{e}"
        )


        raise