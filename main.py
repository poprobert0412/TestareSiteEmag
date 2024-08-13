"""Fisierul principal unde scriem codul si clasa SiteEmag"""
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options#Problema cu default browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class SiteEmag(unittest.TestCase):
    cokkies = (By.XPATH, "//button[@class=\"btn btn-primary btn-block js-accept gtm_h76e8zjgoo\"]")
    search_box = (By.ID, "searchboxTrigger")
    iphone_15_pro_max = (By.XPATH, "//div[contains(@data-url, \"https://www.emag.ro/telefon-mobil-apple-iphone-15-pro-max\")]")
    iphone_256 = (By.XPATH, "//div[contains(text(), \"256\")]")
    iphone_512 = (By.XPATH, "//div[contains(text(), \"512\")]")
    iphone1TB = (By.XPATH, "//div[contains(text(), \"1 TB\")]")
    def setUp(self): #codul pentru inceputul testarii ca sa putem lua site ul pe care o sa facem urmatoarea testare
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")#Acest cod este pentru problema cu default browser
        self.chrome = webdriver.Chrome(options=chrome_options)#Acest cod este pentru problema cu default browser
        self.chrome.get("https://www.emag.ro")

    def tearDown(self):#Codul care o sa ruleze la sfarsitul testarii
        self.chrome.quit()

    def test_numar_iphone_15_pro_max(self):
 #Punem aceea steluta ca sa despachetam booleanul din cookies
        self.chrome.find_element(*self.search_box).send_keys("Iphone 15 pro max")
        self.chrome.find_element(*self.search_box).send_keys(Keys.ENTER)
        WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.iphone_15_pro_max))
        phones = self.chrome.find_elements(*self.iphone_15_pro_max)
        iphone_15_sum = len(phones)
        print(f"Am gasit {iphone_15_sum} de telefoane Iphone 15 pro max!")

    def test_iphone_GB(self):
        self.chrome.find_element(*self.search_box).send_keys("Iphone 15 pro max")
        self.chrome.find_element(*self.search_box).send_keys(Keys.ENTER)
        WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.iphone_15_pro_max))
        self.chrome.find_element(*self.iphone_15_pro_max).click()
        phone256 = self.chrome.find_element(*self.iphone_256)
        phone512 = self.chrome.find_element(*self.iphone_512)
        phone1TB = self.chrome.find_element(*self.iphone1TB)

        assert phone256, "Avem disponibil telefonul de 256 de gb!"
#NU MAI MERGE SITE UL DEOARECE ARE ANTI TESTARE
