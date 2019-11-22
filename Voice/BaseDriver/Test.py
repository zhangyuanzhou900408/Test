# from conf.Driver_app import  AndrionTest
# from utg.operation_json import OperationJson
# class Action(AndrionTest):
#     text2_id:"com.hongfans.voice:id/text"
#     text3_: "\\android.widget.FrameLayout\\android.widget.TextView"
#     def __init__(self):
#         AndrionTest.__init__(self)
#         self.json_id = OperationJson()
#     def Voices_txt(self, id):
#         text = None
#         # time.sleep(5)
#         if self.driver.find_element_xpath(id):  # 是否出现语音文本界面
#             print("出现了")
#             text = self.find_element_id(id).get_attribute("text")
#             print(text)
#         else:
#             text = False
#             #self.system_player('H:\\music3', 1)
#         return text
# cm = Action()
# cm.Voices_txt("text2_id")