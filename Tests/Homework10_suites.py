import unittest
import HtmlTestRunner

from Tests.Alerts import Aler
from Tests.Context_Menu import Context_menu
from Tests.Homework9 import Login
from Tests.Keys import Keyboard
from Tests.test_auth import Authentication_in_Firefox


class TestSuite(unittest.TestCase):
    def test_suite(self):
        tests_run = unittest.TestSuite()

        tests_run.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Context_menu),
                         unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard),
                         unittest.defaultTestLoader.loadTestsFromTestCase(Login),
                         unittest.defaultTestLoader.loadTestsFromTestCase(Authentication_in_Firefox),
                         unittest.defaultTestLoader.loadTestsFromTestCase(Aler)])
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports= True,
            report_title= "Test Execution Report",
            report_name = "Test Results"

        )

        runner.run(tests_run)