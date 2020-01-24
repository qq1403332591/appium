# 导入
import time
from appium import webdriver
from appiumtools import find_element

desired_caps = {}
desired_caps['platformName'] = 'Android'                    # 打开什么平台的app，固定的 > 启动安卓平台
desired_caps['platformVersion'] = '5.1.1'                   # 安卓系统的版本号：adb shell getprop ro.build.version.release
desired_caps['deviceName'] = 'vivo x6plus d'                # 手机/模拟器的型号：adb shell getprop ro.product.model
desired_caps['appPackage'] = 'com.zhihu.android'       # app的名字：
                                                            # 安卓8.1之前：adb shell dumpsys activity | findstr "mFocusedActivity"
                                                            # 安卓8.1之后：adb shell dumpsys activity | findstr "mResume"
desired_caps['appActivity'] = '.app.ui.activity.MainActivity'                   # 同上↑
desired_caps['unicodeKeyboard'] = True                      # 为了支持中文
desired_caps['resetKeyboard'] = True                        # 设置成appium自带的键盘
# 去打开app，并且返回当前app的操作对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


password = ("id", "com.zhihu.android:id/password")
username = ("id", "com.zhihu.android:id/email_input_view")
go_to_btn = ("id", "com.zhihu.android:id/go_to_btn")

cacelbutn = ("aui", "取消")
userlogin = ("id", "com.zhihu.android:id/btn_progress")
questions = ("id", "com.zhihu.android:id/ask_question")

find_element(driver, go_to_btn).click()
find_element(driver, username).send_keys('17712829356')
find_element(driver, password).send_keys('scr5338287')
find_element(driver, userlogin).click()

try:
    find_element(driver, cacelbutn).click()
    print("找到取消按钮，已点击取消按钮！")
except:
    print("没有找到取消按钮！")

try:
    find_element(driver, questions)
    print("登录成功！")
except:
    print("登录失败！")


# driver.find_element_by_id('com.zhihu.android:id/go_to_btn').click()
# driver.find_element_by_id('com.zhihu.android:id/email_input_view').send_keys('17712829356')
# driver.find_element_by_id('com.zhihu.android:id/password').send_keys('scr5338287')
# driver.find_element_by_id('com.zhihu.android:id/btn_progress').click()

# # time.sleep(5)
# # driver.implicitly_wait(10)

# try:
#     driver.find_element_by_android_uiautomator('new UiSelector().text("取消")').click()
#     print("找到取消按钮，已点击取消按钮！")
# except:
#     print("没有找到取消按钮！")

# try:
#     driver.find_element_by_id('com.zhihu.android:id/ask_question')
#     print("登录成功！")
# except:
#     print("登录失败！")