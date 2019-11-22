import json
#根据id获取json文件种的资源进行操作
class OperationJson:
    def __init__(self):
        self.data = self.read_data()
    #获取json文件
    def read_data(self):
        with open("../file/data.json") as fp:
            data = json.load(fp)
            return data
    #根据关键词获取id
    def get_data(self,id):
        data_json = self.data[id]
        return data_json
if __name__ == '__main__':
      opjson = OperationJson()
      print(opjson.get_data("text1_id"))

