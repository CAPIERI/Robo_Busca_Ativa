from selenium import webdriver
import os

def is_edge_installed():
    edge_path = os.path.join(os.environ['ProgramFiles(x86)'], 'Microsoft', 'Edge', 'Application', 'msedge.exe')
    return os.path.isfile(edge_path)

def open_browser():
    if is_edge_installed():
        driver = webdriver.Edge()
    elif is_chrome_installed():
        driver = webdriver.Chrome()
    else:
        raise Exception("Nenhum navegador compatível encontrado")
    return driver

driver = open_browser()
