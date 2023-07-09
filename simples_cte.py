from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get("https://app.simplescte.com.br/login")
assert "Simples" in driver.title
elem = driver.find_element(By.CSS_SELECTOR, "#\:r0\:")
elem.clear()
elem.send_keys("faturamentojvsantostransportes@gmail.com")
elem = driver.find_element(By.CSS_SELECTOR, "#\:r1\:")
elem.clear()
elem.send_keys("agr@2019")
driver.find_element(By.CSS_SELECTOR,"button.MuiButtonBase-root:nth-child(1)").click()