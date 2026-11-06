import unittest
import threading
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from app import app


class TestSeleniumStudentManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Start Flask in a background thread
        cls.server_thread = threading.Thread(
            target=lambda: app.run(port=5001, use_reloader=False)
        )
        cls.server_thread.daemon = True
        cls.server_thread.start()
        time.sleep(1.5)  # let Flask boot

        options = Options()
        options.add_argument("--headless=new")  # remove for visible browser
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.implicitly_wait(3)
        cls.base_url = "http://127.0.0.1:5001"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def _submit(self, text):
        self.driver.get(self.base_url)
        field = self.driver.find_element(By.ID, "grades")
        field.clear()
        field.send_keys(text)
        self.driver.find_element(By.ID, "calculate-btn").click()

    def test_moyenne_12_15_18(self):
        self._submit("12,15,18")
        self.assertIn("15", self.driver.find_element(By.ID, "average").text)

    def test_moyenne_10_10_10(self):
        self._submit("10,10,10")
        self.assertIn("10", self.driver.find_element(By.ID, "average").text)

    def test_mention_echec(self):
        self._submit("8,8,8")
        self.assertIn("Échec", self.driver.find_element(By.ID, "mention").text)

    def test_mention_excellent(self):
        self._submit("18,18,18")
        self.assertIn("Excellent", self.driver.find_element(By.ID, "mention").text)

    def test_note_superieure_20(self):
        self._submit("12,25,18")
        self.assertTrue(
            self.driver.find_elements(By.ID, "error"),
            "Un message d'erreur était attendu",
        )

    def test_champ_vide(self):
        self._submit("")
        self.assertTrue(
            self.driver.find_elements(By.ID, "error"),
            "Un message d'erreur était attendu",
        )


if __name__ == "__main__":
    unittest.main()