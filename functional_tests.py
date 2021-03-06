from selenium import webdriver
import unittest

"""
selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.
http://d.hatena.ne.jp/rougeref/20161014

selenium.common.exceptions.WebDriverException: Message: Unable to find a matching set of capabilities
https://stackoverflow.com/questions/43713445/selenium-unable-to-find-a-matching-set-of-capabilities-despite-driver-being-in
"""


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is typing fly-fishing lures)

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep.


if __name__ == '__main__':
    unittest.main(warnings='ignore')
