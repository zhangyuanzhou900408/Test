import os
package = input("Please input the package which you want to install!\n")
command = "pip install %s -i http://pypi.mirrors.ustc.edu.cn/simple --trusted-host pypi.mirrors.ustc.edu.cn" % package
os.system(command)