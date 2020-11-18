from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Teste de connexion sur la page d'accueil
        self.browser.get(self.server_url)

        # verifier la mention to-do dans le title de la page
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn('To-Do', header_text)

        # Inviter à entrer des elements dans la todo
        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute("placeholder"),
            "Enter a to-do item"
        )

        # elle tape "Buy peacock feathers" dans le text box
        inputbox.send_keys('Buy peacock feathers')

        # quand on tappe sur enter, la page s'actualise, maintenant la page affiche
        # "1: Buy peacock feathers" est un element de la To Do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # Le text box invite pour saisir un nouvel element
        # Elle entre "Use peacock feathers to make a fly"
        inputbox = self.get_item_input_box()
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # La page se met à jour, elle affiche les deux elements
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table(
            '2: Use peacock feathers to make a fly')

        # Maintenant un nouvel utilisateur arrive Francis

        # Il utilise une nouvelle session du navigateur
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visite home page. Il n'est pas identifié comme édith
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis commence une nouvelle liste
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Francis recoit son url unique
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Il n'y a toujours pas les informations d'edith
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn("make a fly", page_text)

        # satisfait, ils vont se coucher
