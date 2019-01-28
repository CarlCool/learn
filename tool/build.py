from distutils.core import setup
import py2exe

setup( console=['test.py']
    #    zipfile = None,
    #    options = {'py2exe' : { 
    #                  "bundle_files": 1,
    #                  "dll_excludes": ["MSVCP90.dll","w9xpopen.exe"]
    #                  }
    #               }
 )

# 作者：Jerry Jho
# 链接：https://www.zhihu.com/question/29738031/answer/45431132
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。