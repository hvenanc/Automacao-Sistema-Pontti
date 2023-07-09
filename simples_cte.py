from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from ambiente import get_variable

driver = webdriver.Firefox()
driver.get("https://app.simplescte.com.br/login")
assert "Simples" in driver.title
elem = driver.find_element(By.CSS_SELECTOR, "#\:r0\:")
elem.clear(get_variable('USUARIO_SCTE'))
elem.send_keys()
elem = driver.find_element(By.CSS_SELECTOR, "#\:r1\:")
elem.clear()
elem.send_keys(get_variable('SENHA_SCTE'))
driver.find_element(By.CSS_SELECTOR,"button.MuiButtonBase-root:nth-child(1)").click()