from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class FunctionalTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
            super().setUpClass()
            cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Teste de connexion sur la page d'accueil
        self.browser.get(self.server_url)

        # verifier la mention to-do dans le title de la page
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn('To-Do', header_text)

        # Inviter à entrer des elements dans la todo
        inputbox = self.browser.find_element_by_id("id_new_item")
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
        inputbox = self.browser.find_element_by_id('id_new_item')
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
        inputbox = self.browser.find_element_by_id('id_new_item')
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


class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        # Edith arrive sur la page d'accueil
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # Elle verifie que la zone de texte est bien alignée
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )


class ItemValidationTest(FunctionalTest):

    @skip
    def test_cannot_add_empty_list_items(self):
            # Edith goes to the home page and accidently tries to submit
            # an empty list item. She hits Enter on the empty input box

            # The homae page refreshes, and there is an error message saying
            # that list items cannot be blank

            # She tries again with the same test for the item, which now works

            # Perversely, she now decides to submit a second blank list item

            # She receives a similar warning on the list page

            # And she can correct it by filling some text in
        self.fail("Write me !")
