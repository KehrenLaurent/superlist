from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        # Edith arrive sur la page d'accueil
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # Elle verifie que la zone de texte est bien alignée
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )
