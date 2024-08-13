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

    def setUp(self): #codul pentru inceputul testarii ca sa putem lua site ul pe care o sa facem urmatoarea testare
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")#Acest cod este pentru problema cu default browser
        self.chrome = webdriver.Chrome(options=chrome_options)#Acest cod este pentru problema cu default browser
        self.chrome.get("https://www.emag.ro")

    def tearDown(self):#Codul care o sa ruleze la sfarsitul testarii
        self.chrome.quit()