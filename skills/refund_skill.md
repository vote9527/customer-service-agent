# Refund Skill


## Description

处理用户退款相关问题。


## Trigger

当用户询问：

- 退款
- 退货
- 售后
- 换货


启用此 Skill。


## Rules


1. 必须调用 search_policy

2. 不允许自行编造退款规则

3. 必须根据知识库回答


## Workflow


用户退款问题

↓

search_policy

↓

总结政策

↓

回复用户
