import unittest
import HTMLTestRunner
import os
import time
from testsuits.test_baidu_search import Baidu_Search
from testsuits.test_get_page_title import GetPageTitle
report_path = os.path.dirname(os.path.abspath('.')) + '/report/'
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

HtmlFile = report_path + now +"HTMLtemplate.html"
fp = open(HtmlFile, "wb")

suite = unittest.TestSuite()
suite.addTest(Baidu_Search("test_baidu_search2"))
suite.addTest(Baidu_Search("test_baidu_search1"))
suite.addTest(GetPageTitle("test_get_title"))

# suite = unittest.TestSuite(unittest.makeSuite(Baidu_Search))
# suite.addTest(GetPageTitle("test_get_title"))

#suite = unittest.TestLoader().discover("testsuits")
if __name__=='__main__':
    run = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"百度测试报告",description="练习专用")
    run.run(suite)
