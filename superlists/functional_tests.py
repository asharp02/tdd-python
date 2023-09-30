from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()
	def test_can_start_a_list_and_retrieve_it_later(self):
		# User goes to access a new online to-do app via the homepage.
		self.browser.get('http://localhost:8000')

	
		# user notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')
		# user is invited to enter a to-do item straight away
		
		# user types into a text box
	
		# upon hitting enter, the page updates and now the page lists the item

		# there is still a text box inviting user to add another item

		# page updates again after user adds another item, now shows both

		# user sees site has generated a unique URL specific to user via 
		# explanatory text

		# user visits that URL and sees same to-do list

if __name__ == '__main__':
	unittest.main(warnings='ignore')

