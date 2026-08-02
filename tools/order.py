from langchain_core.tools import tool
import json

@tool
def check_order(order_id: str) -> str:
    """
    查询订单状态和物流信息。
    输入订单编号，例如 ORD-12345678。
    """
    orders = {
        "ORD-12345678": {
            "status": "已发货",
            "items": "Python编程书 × 1",
            "amount": 89.9,
            "shipping": "顺丰 SF1234567890，预计明天到达",
        },
        "ORD-87654321": {
            "status": "待发货",
            "items": "AI Agent实战课程 × 1",
            "amount": 299.0,
            "shipping": "预计明天发货",
        },
    }
    order = orders.get(order_id)

    if order:
        return json.dumps(order,ensure_ascii=False)
    return f"订单 {order_id} 不存在，请检查订单号。"