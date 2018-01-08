from selenium import webdriver
import unittest


class UserVisitTest(unittest.TestCase):

    def setUp(self):
        self.browswer = webdriver.Firefox()

    def tearDown(self):
        self.browswer.quit()

    def test_user_can_visit_our_site(self):
        # User comes to visit our site
        self.browswer.get('http://localhost:8000')

        # User looks at the title and header and sees `Home | JonnyJE Technical
        # Support`
        title = self.browswer.title
        correct_title = 'JonnyJE Technical Support'
        header_text = self.browswer.find_element_by_tag_name('h1').text

        self.assertIn(correct_title, title)
        self.assertIn(correct_title, header_text)

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
