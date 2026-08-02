from utils.logger import logger


def select_skill(
    query: str,
    skills: dict
):

    query = query.lower()


    if any(
        keyword in query
        for keyword in [
            "退款",
            "退货",
            "退款怎么办",
            "申请退款",
            "售后"
        ]
    ):

        skill_name = "refund_skill"



    elif any(
        keyword in query
        for keyword in [
            "订单",
            "物流",
            "发货",
            "快递",
            "什么时候到",
            "多久到"
        ]
    ):

        skill_name = "order_skill"



    elif any(
        keyword in query
        for keyword in [
            "投诉",
            "举报",
            "客服态度",
            "物流异常"
        ]
    ):

        skill_name = "complaint_skill"



    else:

        skill_name = "default_skill"



    skill = skills.get(
        skill_name
    )


    logger.info(
        f"""
========== SKILL ROUTER ==========

User Query:
{query}

Selected Skill:
{skill_name}

==================================
"""
    )


    return skill