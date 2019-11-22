from time import sleep

from Config.Basic_Site import APP_Basic

class Account(APP_Basic):
    def __init__(self):
        APP_Basic.__init__(self)
    def close_Frame(self):
        sleep(8)
        if self.Exist("prompt_frame"):
            print("进入app")
            self.find_xpath("Not_prompt").click()
            sleep(1)
            self.find_xpath("Jump_Button").click()
            sleep(2)
            if self.Exist("networking"):
                self.find_xpath("know_button").click()
                sleep(1)
                if self.Exist("prompt_frame"):
                    self.find_xpath("Jump_Button").click()
                    sleep(2)
                    if self.find_xpath("log_Icon"):
                        print("打开app成功")
                    else:
                        print("进入app失败")
        else:
            if self.find_xpath("log_Icon"):
                print("打开app成功")
            else:
                print("进入app失败")

    def Login(self):
        self.find_name("未登录").click()
        sleep(2)
        if self.Exist("login_farm"):
            self.send_keys("account",17820393864)
            sleep(1)
            self.send_keys("password",111111)
            sleep(1)
            self.find_name("登录").click()


Account = Account()
Account.close_Frame()
Account.Login()