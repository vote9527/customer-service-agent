from langchain_core.tools import tool

@tool
def search_faq(query: str) -> str:
    """
    搜索企业 FAQ 知识库。
    适合查询退款、发货、保修、优惠、支付等常见问题。
    """
    faq_data = {
        "退款": "退款政策：7天内无理由退款，需要原包装。申请退款请联系客服。",
        "发货": "一般1-3个工作日发货，节假日顺延。",
        "保修": "正规渠道购买享有官方1年保修。",
        "优惠": "新用户首单8折优惠。",
        "支付": "支持微信、支付宝、银行卡。",
    }
    for keyword,answer in faq_data.items():
        if keyword in query:
            return answer
    return "未找到相关 FAQ。"
