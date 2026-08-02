from utils.logger import logger


def select_skill(query, skills):

    query = query.lower()


    # 1. 投诉优先
    if any(
        word in query
        for word in [
            "投诉",
            "申诉",
            "举报"
        ]
    ):

        skill="complaint_skill"


    # 2. 退款售后
    elif any(
        word in query
        for word in [
            "退款",
            "退货",
            "售后",
            "换货"
        ]
    ):

        skill="refund_skill"


    # 3. 订单物流
    elif any(
        word in query
        for word in [
            "订单",
            "物流",
            "发货",
            "配送"
        ]
    ):

        skill="order_skill"


    else:

        skill="default_skill"



    logger.info(
        f"""
========== SKILL ROUTER ==========

User Query:
{query}

Selected Skill:
{skill}

==================================
"""
    )


    return skills.get(skill)