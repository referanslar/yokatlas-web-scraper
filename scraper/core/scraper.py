from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import requests, time

class Scraper:

    def soupWithoutSelenium(self, url):
        res = requests.get(url)
        return BeautifulSoup(res.content, "html.parser")

    def soup(self, url):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)

        WebDriverWait(driver, 10).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

        return BeautifulSoup(driver.page_source, "html.parser")
