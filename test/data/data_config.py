class global_val:
    #case_id
    Id = "0"
    Module_name = '1'
    url = "2"
    run = '3'
    request_way = '4'
    header = '5'
    case_depend = '6'
    data_depend = '7'
    field_depend = '8'
    data = '9'
    expect = '10'
    result = '11'
#获取case_id
def get_id():
    return global_val.Id
#获取模块名称
def get_name():
    return global_val.Module_name
#获取url
def get_url():
    return global_val.url
#获取执行条件
def get_run():
    return global_val.run
#获取请求方式
def get_request_way():
    return global_val.request_way
#获取请求头
def get_header():
    return global_val.header
#获取依赖id
def get_case_depend():
    return global_val.case_depend
#获取依赖数据
def get_data_depend():
    return global_val.data_depend
#获取依赖数据请求字段
def get_field_depend():
    return global_val.field_depend
#获取请求数据
def get_data():
    return global_val.data
#获取预期结果
def get_expect():
    return global_val.expect
#获取实际结果
def get_result():
    return global_val.result

#获取header数值

def get_hearder_value():
    data = {
        'name':"zhangyuanzhou",
        'password':'123456'
    }