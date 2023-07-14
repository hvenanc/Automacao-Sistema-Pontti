import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from uteis import get_saturdays
from ambiente import get_variable

sabados = get_saturdays()
tipo_pag = ''

if len(sabados) == 5:
    tipo_pag = "BONUS SALARIO - 5 SEMANAS"
else:
    tipo_pag = "BONUS SALARIO 7/14/21/28"
    

df = pd.read_excel(get_variable("PLANILHA"))

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
    forne = df.loc[indice,"Fornecedor"]
    atividade = df.loc[indice,"Atividade"]
    valor = df.loc[indice,"Valor Original"]
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
    salario.send_keys(str(valor * len(sabados)))
    time.sleep(6)

    date1 = driver.find_element(By.CSS_SELECTOR, '#Data_Vencimento1')
    date1.clear()
    date1.send_keys(str(sabados[0]))
    time.sleep(5)

    salario1 = driver.find_element(By.CSS_SELECTOR,'#Valor_Original1')
    salario1.clear()
    salario1.send_keys(str(valor).replace('.',','))
    time.sleep(5)

    date2 = driver.find_element(By.CSS_SELECTOR, '#Data_Vencimento2')
    date2.clear()
    date2.send_keys(str(sabados[1]))
    time.sleep(5)

    salario2 = driver.find_element(By.CSS_SELECTOR,'#Valor_Original2')
    salario2.clear()
    salario2.send_keys(str(valor).replace('.',','))

    date3 = driver.find_element(By.CSS_SELECTOR, '#Data_Vencimento3')
    date3.clear()
    date3.send_keys(str(sabados[2]))
    time.sleep(5)

    salario3 = driver.find_element(By.CSS_SELECTOR,'#Valor_Original3')
    salario3.clear()
    salario3.send_keys(str(valor).replace('.',','))

    date4 = driver.find_element(By.CSS_SELECTOR, '#Data_Vencimento4')
    date4.clear()
    date4.send_keys(str(sabados[3]))
    time.sleep(5)

    salario4 = driver.find_element(By.CSS_SELECTOR,'#Valor_Original4')
    salario4.clear()
    salario4.send_keys(str(valor).replace('.',','))

    if len(sabados) == 5:

        date5 = driver.find_element(By.CSS_SELECTOR, '#Data_Vencimento5')
        date5.clear()
        date5.send_keys(str(sabados[4]))
        time.sleep(5)

        salario5 = driver.find_element(By.CSS_SELECTOR,'#Valor_Original5')
        salario5.clear()
        salario5.send_keys(str(valor).replace('.',','))

    time.sleep(7)
    salvar = driver.find_element(By.CSS_SELECTOR, "#btnSubmit").click()

print('Lançamento Concluído com Sucesso!')
