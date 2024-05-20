# taobao-killer

一个基于DrissionPage的淘宝秒杀python脚本

# 安装环境

1. 自行安装谷歌浏览器
2. 自行安装python
3. 使用 pip 安装 DrissionPage：`pip install DrissionPage`

# 使用

1. **自动输入支付密码需要提前设置你的密码**，修改第30行`input("123456")`，把`123456`换成你的支付密码。如果**想手动输入密码，加`#`注释或删除30和32行即可**

```python
# 输入支付密码
page.ele('x://*[@id="payPassword_rsainput"]').input("123456")
# 确定
page.ele('x://*[@id="validateButton"]').click()
```

2. 修改变量`killer_time`为你的秒杀时间，直接用python运行即可(需要提前选择好你要购买的商品型号并添加到淘宝购物车以及设置好默认的发货地址等信息)

```python
python taobao_killer.py
```



【淘宝抢购秒杀，基于DrissionPage的python脚本】 https://www.bilibili.com/video/BV16m421x7GZ/?share_source=copy_web&vd_source=d34abe3786a6b85ecc07875a85795885
