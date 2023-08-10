import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv
from ambiente import get_variable

load_dotenv()
inicio = time.time()

df = pd.read_excel(get_variable("PLANILHA_IMPOSTO"))

driver = webdriver.Firefox()
driver.get(get_variable("LINK_PORTAL"))
assert "Gw" in driver.title
elem = driver.find_element(By.CSS_SELECTOR, "#user")
elem.clear()
elem.send_keys(get_variable("USUARIO"))
elem = driver.find_element(By.CSS_SELECTOR, "#pass")
elem.clear()
elem.send_keys(get_variable("SENHA"))
time.sleep(3)
elem.send_keys(Keys.RETURN)
time.sleep(10)
drop = driver.find_element(By.CSS_SELECTOR, ".dropdown > li:nth-child(2) > a:nth-child(1)").click()
produtos = driver.find_element(By.CSS_SELECTOR, ".dropdown > li:nth-child(2) > ul:nth-child(2) > li:nth-child(17) > a:nth-child(1)").click()
time.sleep(5)
driver.get("https://ponttierp.com/granderecife2/produto/list_produto.php?acao=entrar")
time.sleep(2)

for i, codigo in enumerate(df['Código']):
    produto = df.loc[i, 'Produto']
    cfop = df.loc[i, 'Cfop']
    icms = df.loc[i, 'ICMS Dentro']

    time.sleep(5)
    busca = driver.find_element(By.CSS_SELECTOR, ".ordenar_por > input:nth-child(3)")
    busca.clear()
    busca.send_keys(produto)
    busca.send_keys(Keys.RETURN)
    time.sleep(5)
    editar = driver.find_element(By.CSS_SELECTOR,"#lista > tbody:nth-child(3) > tr:nth-child(1) > td:nth-child(10) > a:nth-child(4) > img:nth-child(1)")
    editar.click()
    tipo_cfop = Select(driver.find_element(By.CSS_SELECTOR, "#CFOP\ Venda"))
    tipo_cfop.select_by_visible_text(cfop)
    icms_dentro = Select(driver.find_element(By.CSS_SELECTOR, "#Codigo_ST_Simples"))
    icms_dentro.select_by_visible_text(icms)
    icms_fora = Select(driver.find_element(By.CSS_SELECTOR, "#Codigo_ST_Simples2"))
    icms_fora.select_by_visible_text(icms)
    time.sleep(5)

    salvar = driver.find_element(By.CSS_SELECTOR, ".bt_cadastro").click()

print('Lançamento Concluído com Sucesso!')
fim = time.time()
print(fim - inicio)
