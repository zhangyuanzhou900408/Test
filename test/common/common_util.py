class Common:
    def Contrast_test(self,str_one,str_two):
        '''比较两个值，来判断是否存在包含关系'''
        flag = None
        if str_one in str_two:
            #print("测试通过")
            flag = True
        else:
            flag = False
            #print("测试失败")
        return flag
