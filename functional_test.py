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

        # Checks to see if the base.html is extended by the home_page
        home_page_link = self.browswer.find_element_by_id('home_page')
        self.assertIn(home_page_link, self.browswer)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
