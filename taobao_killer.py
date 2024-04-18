from DrissionPage import ChromiumPage
import datetime

# 创建对象
page = ChromiumPage()

# 指定秒杀时间
kill_time = "2024-04-18 15:19:00.00000000"

# 打开淘宝网页
page.get("https://www.taobao.com")
# 点击购物车
page.ele('x://*[@id="J_MiniCart"]/div[1]/a/span[2]').click()
# 等待登录完成，直到购物车全选按钮出现，超时时间我设置为1分钟
page.wait.ele_displayed('x://*[@id="J_SelectAll1"]/div/label',timeout=60)
# 点击购物车全选按钮
page.ele('x://*[@id="J_SelectAll1"]/div/label').click()

while(True):
    # 获取当前时间
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(now)
    # 判断当前时间是否到达了秒杀时间
    if(now>kill_time):
        # 点击结算按钮
        page.ele('x://*[@id="J_SmallSubmit"]').click()
        break

# 测试时的程序暂停
input()
