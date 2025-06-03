import pyautogui 
import time

# Passo 1: Entrar no sistema da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.PAUSE = 0.5

# Abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Abrir o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

# Passo 2: Fazer login
pyautogui.click(x=643, y=469)
pyautogui.write("cristianoronaldo@gmail.com")
pyautogui.press("tab")
pyautogui.write("siuuuu")
pyautogui.press("tab")
pyautogui.press("enter")

# Passo 3: Importar a base de dados
import pandas as pd

tabela = pd.read_csv(r"C:\Users\diogo\OneDrive\Documentos\JornadaPy\Aula 1\produtos.csv")
print(tabela)

# Passo 4: Cadastra 1 produto

for linha in tabela.index:
    pyautogui.click(x=673, y=325)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000)