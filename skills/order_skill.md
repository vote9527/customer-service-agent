# Order Skill


## Description

处理订单查询。


## Trigger

用户询问：

- 我的订单
- 物流
- 发货


## Rules


1. 必须调用 check_order

2. 不允许猜测订单状态


## Workflow


订单号

↓

check_order

↓

生成回复
