from langchain_core.tools import tool
import datetime


@tool
def submit_complaint(
    order_id: str,
    complaint_type: str,
    description: str,
) -> str:
    """
    提交售后投诉申请。
    complaint_type 可以是：
    退款申请、质量问题、物流问题、其他。
    """

    ticket_id = (
        f"TKT-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
    )

    return (
        f"投诉已受理！\n"
        f"工单编号：{ticket_id}\n"
        f"类型：{complaint_type}\n"
        f"相关订单：{order_id}\n"
        f"问题描述：{description}\n"
        f"预计24小时内客服跟进处理。"
    )