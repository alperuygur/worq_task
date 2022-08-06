import os
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

"""
class linktest(LiveServerTestCase):

    def testpage(self):
        driver = webdriver.Chrome()

        driver.get('https://www.trendyol.com/atari/retro-mini-620-mario-oyunlu-av-retro-mini-oyun-konsolu-scart-basliksiz-p-36587919')
        time.sleep(3)
        assert "Atari" in driver.title
"""

class formtest(LiveServerTestCase):

    def testform(self):
        try:
            try:
                op = webdriver.ChromeOptions()
                op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
                driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)
            except:
                driver = webdriver.Chrome(ChromeDriverManager().install())
            
            start_url = "https://www.trendyol.com/atari/retro-mini-620-mario-oyunlu-av-retro-mini-oyun-konsolu-scart-basliksiz-p-36587919"
            driver.get(start_url)
            
            name = driver.find_element(By.CLASS_NAME, 'pr-new-br')
            get_brand_text = name.find_elements(By.CSS_SELECTOR, ".pr-new-br [href]")
            for text_b in get_brand_text:
                brand = text_b.text
            price_selling = driver.find_element(By.CLASS_NAME, 'prc-dsc')
            category_get = driver.find_elements(By.ID, 'marketing-product-detail-breadcrumb')
            category = []
            for cat in category_get:
                category.append(cat.text)
            category = [j.replace('\n', '/') for j in category]
            print(name.text ," - ", brand ," - ", price_selling.text ," - ", category)
            
            link_merchant_info = driver.find_element(By.CLASS_NAME, 'seller-container')
            link_merchant_info.click()
            time.sleep(1)
            driver.find_element(By.LINK_TEXT, 'SATICI PROFİLİ').click()
            seller =  driver.find_element(By.CLASS_NAME, 'seller-store__name')
            seller_score =  driver.find_element(By.CLASS_NAME, 'seller-store__score')
            seller_city = driver.find_element(By.XPATH, '//*[@id="seller-store"]/div/div[2]/div[1]/div[2]/div/span[2]')
            print(seller.text ," - ", seller_score.text ," - ", seller_city.text)
            
            driver.execute_script("window.history.go(-2)")
            time.sleep(3)
            then_click = driver.find_element(By.CLASS_NAME, 'omc-mr-btn')
            driver.execute_script("arguments[0].click();", then_click)
            rows = len(driver.find_elements(By.CLASS_NAME, 'pr-mc-w'))
            count=1 
            
            while count <= rows:
                
                then_click = driver.find_element(By.CLASS_NAME, 'omc-mr-btn')
                driver.execute_script("arguments[0].click();", then_click)
                data = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'omc-cntr'))
                )
                merchants = '//*[@id="product-detail-app"]/div/div[3]/div[2]/div['
                merchants += str(count)
                merchants += ']/div[1]/div[1]/div/div[1]/a'
                then_click = data.find_element(By.XPATH, merchants)
                driver.execute_script("arguments[0].click();", then_click)
                time.sleep(3)
                then_click = driver.find_element(By.LINK_TEXT, 'SATICI PROFİLİ')
                driver.execute_script("arguments[0].click();", then_click)
                other_merchant =  driver.find_element(By.CLASS_NAME, 'seller-store__name')
                other_merchant_score =  driver.find_element(By.CLASS_NAME, 'seller-store__score')
                other_merchant_city = driver.find_element(By.XPATH, '//*[@id="seller-store"]/div/div[2]/div[1]/div[2]/div/span[2]')
                print(other_merchant.text ," - ", other_merchant_score.text ," - ", other_merchant_city.text)
                driver.execute_script("window.history.go(-2)")
                time.sleep(3)
                count += 1

        finally:
            driver.quit()
