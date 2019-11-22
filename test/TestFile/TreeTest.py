import os
import sys
import xml.etree.ElementTree as ET
#遍历xml文件
def traverseXml(element):
    if len(element)>0:
        for i in element:
            print(i.tag,"--------",i.attrib)
            traverseXml(i)
if __name__ == "__main__":

    xmlfilepath = os.path.abspath("Test.xml")
    #解析文件
    try:
        tree = ET.parse(xmlfilepath)
        print(tree)
        #获取根节点
        root = tree.getroot()
    except Exception as e:  # 捕获除与程序退出sys.exit()相关之外的所有异常
        print("parse test.xml fail!")
        sys.exit()
    print("root type:", type(root))
    print(root.tag, "----", root.attrib)
    print(20 * "*")
    # 遍历root的下一层
    for i in root:
        print("root下的",i.tag,"====",i.attrib)
    # 使用下标访问
    print(root[0].text)
    print(root[1][0].text)
    print(root[2][0].text)
    print (20 * "*")
    #遍历xml文件
    traverseXml(root)
    print (20 * "*")
    findroot = root.findall("item")
    for i in findroot:
        print(i.tag, "----", i.attrib, "----", i.text)
        # 修改xml文件，将passwd修改为999999
    login = root.find("login")
    passwdValue = login.get("passwd")
    print(passwdValue)
    login.set("passwd","张元周")
    print("modify passwd:", login.get("passwd"))


