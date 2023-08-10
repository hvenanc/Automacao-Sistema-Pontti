import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from ambiente import get_variable

load_dotenv()
inicio = time.time()

# Planilha com produtos
df = pd.read_excel(get_variable("PLANILHA_INVENTARIO"))

driver = webdriver.Firefox()
driver.get(get_variable("LINK_PORTAL"))
assert "Gw" in driver.title
elem = driver.find_element(By.CSS_SELECTOR, "#user")
elem.clear()
elem.send_keys(get_variable("USUARIO"))
elem = driver.find_element(By.CSS_SELECTOR, "#pass")
elem.clear()
elem.send_keys(get_variable("SENHA"))
elem.send_keys(Keys.RETURN)
driver.get(get_variable("LINK_INVENTARIO"))

# Inserindo os produtos no inventario

for i, codigo in enumerate(df['Código']):
    quant = df.loc[i, 'Quantidade']

    elem = driver.find_element(By.CSS_SELECTOR, "#Produto")
    elem.clear()
    elem.send_keys(codigo)
    time.sleep(5)
    elem.send_keys(Keys.RETURN)
    elem = driver.find_element(By.CSS_SELECTOR, "#Qtd")
    elem.clear()
    elem.send_keys(str(quant))
    time.sleep(5)
    elem = driver.find_element(By.CSS_SELECTOR, ".azul > td:nth-child(6) > input:nth-child(1)").click()
    time.sleep(5)

# Salvando Inventário

time.sleep(5)
elem = driver.find_element(By.CSS_SELECTOR, "button.bt_cadastro:nth-child(6)").click()

print('Lançamento Concluído com Sucesso!')
fim = time.time()
print(fim - inicio)