import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from ambiente import get_variable

inicio = time.time()
    

df = pd.read_excel(get_variable("PLANILHA_DESPESAS_FIXAS"))

driver = webdriver.Edge()
driver.get(get_variable("EMPRESA"))
assert "Gw" in driver.title
elem = driver.find_element(By.CSS_SELECTOR, "#user")
elem.clear()
elem.send_keys(get_variable("USUARIO"))
elem = driver.find_element(By.CSS_SELECTOR, "#pass")
elem.clear()
elem.send_keys(get_variable("SENHA"))
elem.send_keys(Keys.RETURN)
time.sleep(10)
contas = driver.find_element(By.CSS_SELECTOR, "#pagar > a:nth-child(1) > img:nth-child(1)").click()

for indice,descricao in enumerate(df['Descrição']):
    time.sleep(10)
    descr = df.loc[indice,"Descrição"]
    forne = df.loc[indice,"Fornecedor"]
    atividade = df.loc[indice,"Atividade"]
    data = df.loc[indice,"Data"]
    valor = df.loc[indice,"Valor"]
    tipo_pag = df.loc[indice,"Tipo"]
    time.sleep(10)

    #Link do Contas a Pagar 
    driver.get(get_variable("MODULO"))
    time.sleep(5)
    desc = driver.find_element(By.CSS_SELECTOR, "#Descricao")
    desc.clear()
    desc.send_keys(descricao)
    time.sleep(3)

    forn = driver.find_element(By.CSS_SELECTOR, '#Fornecedor')
    forn.clear()
    forn.send_keys(forne)
    time.sleep(5)
    forn.send_keys(Keys.RETURN)

    tipo = Select(driver.find_element(By.CSS_SELECTOR,'#Atividade'))
    tipo.select_by_visible_text(atividade)
    check_box = driver.find_element(By.CSS_SELECTOR, '#Boleto_Recebido')
    check_box.click()
    check_box = driver.find_element(By.CSS_SELECTOR, '#EF')
    check_box.click()

    tipo = Select(driver.find_element(By.CSS_SELECTOR,'#Tipo_Pagamento'))
    tipo.select_by_visible_text(tipo_pag)
    time.sleep(6)

    salario = driver.find_element(By.CSS_SELECTOR,'#Valor_Original')
    salario.clear()
    salario.send_keys(valor)
    time.sleep(6)

    date1 = driver.find_element(By.CSS_SELECTOR, '#Data_Vencimento1')
    date1.clear()
    date1.send_keys(str(data) + "/08/2023")
    time.sleep(5)

    salario1 = driver.find_element(By.CSS_SELECTOR,'#Valor_Original1')
    salario1.clear()
    salario1.send_keys(valor)
    time.sleep(5)

    time.sleep(7)
    salvar = driver.find_element(By.CSS_SELECTOR, "#btnSubmit").click()

print('Lançamento Concluído com Sucesso!')
fim = time.time()
print(fim - inicio)
