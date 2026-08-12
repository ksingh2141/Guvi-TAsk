import time
from pages.population_page import PopulationPage


class TestPopulation:

    def test_live_population_counter(self, setup):

        driver = setup

        driver.get(
            "https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live"
        )

        population_page = PopulationPage(driver)

        print("\nPress CTRL+C to stop...\n")

        try:

            while True:

                count = population_page.get_population_count()

                print(f"Current World Population : {count}")

                time.sleep(1)

        except KeyboardInterrupt:

            print("\n\nPopulation monitoring stopped by user.")