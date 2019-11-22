import json
class OperetionJson:
    def __init__(self):
        self.data = self.read_data()
    #读取json文件，返回内容
    def read_data(self):
        with open("../dataconfig/login.json") as fp:
            data = json.load(fp)
            print(type(data))
            return data
    #根据关键词获取内容
    def get_data(self,id):
        data_json = self.data[id]
        return data_json
if __name__ == '__main__':
    opjson = OperetionJson()
    print(opjson.get_data("data_one"))