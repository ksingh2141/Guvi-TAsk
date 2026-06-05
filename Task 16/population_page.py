from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PopulationPage:

    # XPATH ONLY
    POPULATION_COUNT = (
        By.XPATH,
        "//div[contains (@class, 'counter-ticker is-size-2-mobile')]"
    )

    def __init__(self, driver):
        self.driver = driver

    def get_population_count(self):

        population = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                self.POPULATION_COUNT
            )
        )

        return population.text.strip()