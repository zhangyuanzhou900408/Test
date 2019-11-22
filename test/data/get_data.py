from utg.xlsx_test import OperationExcel
from data import data_config
from utg.operation_json import OperetionJson

class GetData:
    def __init__(self):
        file_name = '../dataconfig/API.xls'
        sheet_id = 0
        self.opera_excel = OperationExcel(file_name,sheet_id)
        self.operation_json = OperetionJson()
    #去获取excel的行数,我们的case个数
    def get_case_line(self):
        return self.opera_excel.get_rows()
    #获取是否执行数据
    def get_is_run(self,row):
        flag = None
        col =int(data_config.get_run())
        run_data = self.opera_excel.get_value(row,col)
        if run_data == 'yes':
             flag = True
        else:
            flag = None
        return flag

    # 获取url
    def get_url(self,row):
        col = int(data_config.get_url())
        url_data = self.opera_excel.get_value(row,col)
        if url_data == '':
            return None
        return url_data
    #获取请求数据
    def get_request_data(self,row):
        col = int(data_config.get_data())
        request_data = self.opera_excel.get_value(row,col)
        return request_data
    #获取请求方式
    def get_method(self,row):
        col = int(data_config.get_request_way())
        method_data = self.opera_excel.get_value(row,col)
        return method_data
    #获取是否需要请求头
    def get_request_heared(self,row):
        col = int(data_config.get_header())
        header = self.opera_excel.get_value(row,col)
        if header == 'yes':
            return data_config.get_hearder_value()
        else:
            return None
    #通过获取关键字或者data数据
    def get_data_for_jaon(self,row):
        get_json = self.operation_json.get_data(self.get_request_data(row))
        return get_json

    #获取预期结果
    def get_except_data(self,row):
        col = int(data_config.get_expect())
        except_data = self.opera_excel.get_value(row,col)
        return except_data

    # 写入实际结果
    def get_results_value(self,row,value):
        col = int(data_config.get_result())
        results_data = self.opera_excel.write_value(row,col,value)
        return results_data





