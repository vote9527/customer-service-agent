from langchain_openai import ChatOpenAI

from langchain_core.messages import (
    SystemMessage,
    ToolMessage
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
from .harness import AgentHarness


# =========================
# LLM
# =========================

llm = ChatOpenAI(
    model=MODEL_NAME,
    temperature=TEMPERATURE,
    api_key=DASHSCOPE_API_KEY,
    base_url=BASE_URL
)


llm_with_tools = llm.bind_tools(
    TOOLS
)


# =========================
# Skill Runtime
# =========================

skills = load_skills()


harness = AgentHarness(
    skills
)


logger.info(
    f"""
========== SKILL LOADER ==========

Loaded Skills:

{list(skills.keys())}

===================================
"""
)


# =========================
# Base Prompt
# =========================

BASE_PROMPT = """

你是企业智能客服 Agent。

职责：

1. 解答用户产品问题
2. 查询 FAQ
3. 查询订单
4. 查询企业政策
5. 提交售后投诉


规则：

1.
必须遵守当前 Skill 的流程。


2.
Skill 要求调用工具时，
必须调用工具。


3.
只能使用工具返回的信息。


4.
禁止编造订单信息。


5.
禁止编造企业政策。


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

        messages = list(
            state["messages"]
        )


        last_message = messages[-1]


        # =====================
        # 判断执行阶段
        # =====================

        is_tool_result=isinstance(
            last_message,
            ToolMessage
        )


        if is_tool_result:

            user_query = None

        else:

            user_query = last_message.content



        tracer.start(
            node="agent_node",
            input=(
                user_query
                if user_query
                else "TOOL_RESULT"
            )
        )


        # =====================
        # Skill处理
        # =====================

        current_skill = state.get(
            "current_skill"
        )


        if user_query:


            # 用户第一次进入
            # 选择Skill

            context = harness.prepare(
                user_query
            )


            if context["skill"]:


                current_skill = (
                    context["skill"]["name"]
                )


                skill_prompt = (
                    context["prompt"]
                )


            else:

                skill_prompt=""


        else:


            # Tool返回阶段
            # 不重新Router

            if current_skill:


                skill_prompt = skills.get(
                    current_skill,
                    {}
                ).get(
                    "content",
                    ""
                )


                logger.info(
                    f"""
========== TOOL RESULT ==========

Reuse Skill:

{current_skill}

==================================
"""
                )


            else:

                skill_prompt=""


                logger.warning(
                    """
========== TOOL RESULT ==========
No Current Skill
================================
"""
                )



        # =====================
        # System Prompt
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
        # 删除旧 SystemMessage
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
        # LLM
        # =====================

        response = (
            llm_with_tools
            .invoke(messages)
        )



        tracer.end(
            response.content
        )


        # =====================
        # 更新State
        # =====================

        return {

            "messages":[
                response
            ],

            "current_skill":
                current_skill,
                
             "skill_prompt":
                skill_prompt

        }



    except Exception as e:


        tracer.end(
            f"ERROR:{e}"
        )


        raise