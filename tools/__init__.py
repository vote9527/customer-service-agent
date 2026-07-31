from .faq import search_faq
from .order import check_order
from .complaint import submit_complaint
from .rag_tool import search_policy

TOOLS = [
    search_faq,
    check_order,
    submit_complaint,
    search_policy
]