from selenium.webdriver.common.by import By

from data.config import DRIVER_PATH
from selenium import webdriver
from utils.db.db import find_all_search, process_all_stuff


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
            self.driver.implicitly_wait(5)

            # accept cookies
            # self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

            items = len(self.driver.find_elements(By.CLASS_NAME, "z252w"))
            for item in range(items):
                stuff = self.driver.find_elements(By.CLASS_NAME, "yoqzg")
                for st in stuff:
                    st_title = st.find_element(By.CLASS_NAME, "product-name").text
                    st_href = st.find_element(By.CLASS_NAME, "bb1c_").get_attribute('href')
                    for search_model in search_models:
                        if st_title.find(search_model.title) >= 0:
                            await process_all_stuff(st_title, st_href, search_model.chatid, self.bot)
