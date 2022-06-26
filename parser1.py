import requests
from selenium.webdriver.common.by import By

from config import DRIVER_PATH, URL
from selenium import webdriver
from db import find_all_search, process_all_stuff


class AllStuffParsing:
    def __init__(self, url, bot):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.minimize_window()
        self.url = url
        self.bot = bot

    def __del__(self):
        self.driver.close()

    async def parse(self):
        search_models = find_all_search()

        for page in range(1, 5):
            print(self.url.format(page))
            self.driver.get(self.url.format(page))
            self.driver.implicitly_wait(10)

            # self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

            items = len(self.driver.find_elements(By.CLASS_NAME, "z252w"))
            for item in range(items):
                cards = self.driver.find_elements(By.CLASS_NAME, "yoqzg")
                for card in cards:
                    card_title = card.find_element(By.CLASS_NAME, "product-name").text
                    card_href = card.find_element(By.CLASS_NAME, "bb1c_").get_attribute('href')
                    for search_model in search_models:
                        if card_title.find(search_model.title) >= 0:
                            await process_all_stuff(card_title, card_href, search_model.chatid, self.bot)
