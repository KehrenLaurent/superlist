from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Teste de connexion sur la page d'accueil
        self.browser.get('http://localhost:8000')

        # verifier la mention to-do dans le title de la page
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test')

        # Inviter à entrer des elements dans la todo

        # elle tape "Buy peacock feathers" dans le text box

        # quand on tappe sur enter, la page s'actualise, maintenant la page affiche
        # "1: Buy peacock feathers" est un element de la To Do list

        # Le text box invite pour saisir un nouvel element
        # Elle entre "Use peacock feathers to make a fly"

        # La page se met à jour, elle affiche les deux elements

        # Elle se demande si le site se souvient des ces elements sur un url specifique

        # elle visite son url, elle affiche ces elements


if __name__ == "__main__":
    unittest.main(warnings='ignore')
