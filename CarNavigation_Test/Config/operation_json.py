import json
#根据id获取json文件种的资源进行操作
class OperationJson:
    # 根据关键词获取id
    def get_data(self,id,file):
        with open(file) as fp:
            data = json.load(fp)
        data_json = data[id]
        return data_json
if __name__ == '__main__':
      opjson = OperationJson()
      print(opjson.get_data("QQ_music","../Helper/Start.json"))

