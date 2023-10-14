from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os

# Verificar navegadores disponíveis
navegadores = {
    "Microsoft Edge": EdgeChromiumDriverManager,
    "Google Chrome": ChromeDriverManager,
    "Mozilla Firefox": GeckoDriverManager,
}

# Verificar quais navegadores estão instalados
navegador_disponivel = None
driver_manager_disponivel = None

for navegador, driver_manager in navegadores.items():
    driver_path = driver_manager().install()
    if os.path.isfile(driver_path):
        navegador_disponivel = navegador
        driver_manager_disponivel = driver_manager
        break

# Verificar se algum navegador foi encontrado
if navegador_disponivel:
    print(f"Navegador disponível: {navegador_disponivel}")

    # Configurar o driver para o navegador disponível
    if driver_manager_disponivel == EdgeChromiumDriverManager:
        driver = webdriver.Edge(driver_path)
    elif driver_manager_disponivel == ChromeDriverManager:
        driver = webdriver.Chrome(driver_path)
    elif driver_manager_disponivel == GeckoDriverManager:
        driver = webdriver.Firefox(driver_path)

    # Navegar até a página de login
    driver.get('https://escolatotal.educacao.sp.gov.br/')

    # Esperar até que os elementos estejam disponíveis
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'name')))
    wait.until(EC.presence_of_element_located((By.ID, 'senha')))
    wait.until(EC.presence_of_element_located((By.ID, 'botaoEntrar')))

    # Inserir RG e Senha
    rg_responsavel = "rg228522936sp"
    senha_responsavel = "HUGO2021"
    driver.find_element_by_id('name').send_keys(rg_responsavel)
    driver.find_element_by_id('senha').send_keys(senha_responsavel)

    # Clicar no botão "acessar"
    driver.find_element_by_id('botaoEntrar').click()
else:
    print("Nenhum navegador suportado foi encontrado. Por favor, instale algum navegador, como o Chrome ou Edge.")


# 6 - Clicar botão "turma"
# 7 - Clicar Caixa de texto "de"
# 8 - Inserir Região da escola, exemplo "sul1"
# 9 - Clicar Caixa de texto "municipio"
# 10 - Inserir Municipio, exemplo "São Paulo"
# 11 - Clicar Caixa de texto "tipo escola"
# 12 - Inserir Tipo escola, exemplo "pei"
# 13 - Clicar Caixa de texto "pei"
# 14 - Inserir (boolean) Pei, exemplo sim/não
# 15 - Clicar Caixa de texto "escola"
# 16 - Inserir Escola, exemplo "Hugo Lacorte Vitale"
# 17 - Clicar "data matricula"
# 18 - Clicar "..."
# 19 - Clicar "exportar dados"
# 20 - Clicar "exportar"
# 21 - Abrir data.xlsx
# // (Usuario seleciona) presença atual turma
# 22 - Se "%Presença atual turma" <=80
# 23 - Guardar RA
# 24 - Guardar Aluno
# // (Usuario seleciona) presença semana atual
# 22 - Se "%Presença semana atual"
# 23 - Guardar RA
# 24 - Guardar Aluno
# // (Usuario seleciona) presença semana anterior
# 22 - Se "%Presenca semana anterior"
# 23 - Guardar RA
# 24 - Guardar Aluno
# // Puxar numero alunos
# 25 - Acessar ""
# 26 - (CONTINUAR)
# //salvar informações dos alunos faltantes
# 27 - Encontrar "ra_aluno"
# 28 - Guardar "sala_aluno"
# 29 - Guardar "telefona_aluno"
# // Fazer tabela com informações de alunos faltantes em Presença Atual turma (PAT)
# 30 - Criar arquivo xlxs
# 31 - Inserir formatação padrão (titulo das colunas, como, Sala, Ra, Nome, Presença Atual, Telefone)
# 32 - Inserir "sala_aluno" (coluna 1, linha x)
# 33 - Inserir "ra_aluno" (coluna 2, linha x)
# 34 - Inserir "nome_aluno" (coluna 3, linha x)
# 35 - Inserir "presenca_pat_aluno" (coluna 4, linha x)
# 36 - Inserir "telefone" (coluna 5, linha x)
# 37 - Nomear arquivo "escola_registrada [ ] PAT_(data).pdf"
# 38 - Salvar arquivo "escola_registrada [ ] PAT (data).pdf"
# // Fazer tabela %Presença Semana Atual (PSA)
# 30 - Criar arquivo xlxs
# 31 - Inserir formatação padrão (titulo das colunas, como, Sala, Ra, Nome, Presença Semana Atual, Telefone)
# 32 - Inserir "sala_aluno" (coluna 1, linha x)
# 33 - Inserir "ra_aluno" (coluna 2, linha x)
# 34 - Inserir "nome_aluno" (coluna 3, linha x)
# 35 - Inserir "presenca_psa_aluno" (coluna 4, linha x)
# 36 - Inserir "telefone" (coluna 5, linha x)
# 37 - Nomear arquivo "escola_registrada [ ] PSA_(data).pdf"
# 38 - Salvar arquivo "escola_registrada [ ] PSA (data).pdf"
# // Fazer tabela %Presença Semana Anterior (PSAT)
# 30 - Criar arquivo xlxs
# 31 - Inserir formatação padrão (titulo das colunas, como, Sala, Ra, Nome, Presença Semana Atual, Telefone)
# 32 - Inserir "sala_aluno" (coluna 1, linha x)
# 33 - Inserir "ra_aluno" (coluna 2, linha x)
# 34 - Inserir "nome_aluno" (coluna 3, linha x)
# 35 - Inserir "presenca_psa_aluno" (coluna 4, linha x)
# 36 - Inserir "telefone" (coluna 5, linha x)
# 37 - Nomear arquivo "escola_registrada [ ] PSAT_(data).pdf"
# 38 - Salvar arquivo "escola_registrada [ ] PSAT (data).pdf"

# //*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[8]/transform/div/div[3]/div/div/visual-modern/div/div/div[2]/div
# //*[@id="slicer-dropdown-popup-fee091e3-a7ed-c54b-1fed-d5d45102c62c"]/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div
# //*[@id="slicer-dropdown-popup-fee091e3-a7ed-c54b-1fed-d5d45102c62c"]/div[1]/div/div[2]/div/div[1]/div/div/div[7]/div
# /html/body/div[18]/div[1]/div/div[2]/div/div[1]/div/div/div[8]/div
# /html/body/div[18]/div[1]/div/div[2]/div/div[1]/div/div/div[4]/div
# /html/body/div[18]/div[1]/div/div[2]/div/div[1]/div/div/div[1]/div
# //*[@id="slicer-dropdown-popup-fee091e3-a7ed-c54b-1fed-d5d45102c62c"]/div[1]/div/div[2]/div/div[1]/div/div
# //*[@id="slicer-dropdown-popup-fee091e3-a7ed-c54b-1fed-d5d45102c62c"]/div[1]/div/div[2]/div/div[1]/div/div
# <div class="visibleGroup" role="none" style="transform: translate(0px, 0px);"><div class="row" role="none"><div class="slicerItemContainer" tabindex="0" role="option" aria-checked="true" aria-setsize="-1" aria-posinset="1" data-row-index="1" data-row-id="0:1" style="margin-left: 0px; padding-top: 4px; padding-bottom: 4px;"><div class="slicerCheckbox selected" aria-hidden="true"><span class="glyphicon checkbox checkboxOutlineContrast" style="font-size: 16px;"></span></div><span class="slicerText" title="1ª SERIE A INTEGRAL ANUAL - 38663828" style="color: rgb(37, 36, 35); border-style: solid; border-color: rgb(96, 94, 92); border-width: 0px; font-size: 16px; font-family: &quot;Segoe UI&quot;, wf_segoe-ui_normal, helvetica, arial, sans-serif; line-height: 21px; font-weight: normal; font-style: normal; text-decoration: none;">1ª SERIE A INTEGRAL ANUAL - 38663828</span></div></div><div class="row" role="none"><div class="slicerItemContainer" role="option" aria-checked="false" aria-setsize="-1" aria-posinset="2" data-row-index="2" data-row-id="0:2" style="margin-left: 0px; padding-top: 4px; padding-bottom: 4px;"><div class="slicerCheckbox" aria-hidden="true"><span class="glyphicon checkbox checkboxOutlineContrast" style="font-size: 16px;"></span></div><span class="slicerText" title="1ª SERIE B INTEGRAL ANUAL - 38663978" style="color: rgb(37, 36, 35); border-style: solid; border-color: rgb(96, 94, 92); border-width: 0px; font-size: 16px; font-family: &quot;Segoe UI&quot;, wf_segoe-ui_normal, helvetica, arial, sans-serif; line-height: 21px; font-weight: normal; font-style: normal; text-decoration: none;">1ª SERIE B INTEGRAL ANUAL - 38663978</span></div></div><div class="row" role="none"><div class="slicerItemContainer" role="option" aria-checked="false" aria-setsize="-1" aria-posinset="3" data-row-index="3" data-row-id="0:3" style="margin-left: 0px; padding-top: 4px; padding-bottom: 4px;"><div class="slicerCheckbox" aria-hidden="true"><span class="glyphicon checkbox checkboxOutlineContrast" style="font-size: 16px;"></span></div><span class="slicerText" title="1ª SERIE C INTEGRAL ANUAL - 38664011" style="color: rgb(37, 36, 35); border-style: solid; border-color: rgb(96, 94, 92); border-width: 0px; font-size: 16px; font-family: &quot;Segoe UI&quot;, wf_segoe-ui_normal, helvetica, arial, sans-serif; line-height: 21px; font-weight: normal; font-style: normal; text-decoration: none;">1ª SERIE C INTEGRAL ANUAL - 38664011</span></div></div><div class="row" role="none"><div class="slicerItemContainer" role="option" aria-checked="false" aria-setsize="-1" aria-posinset="4" data-row-index="4" data-row-id="0:4" style="margin-left: 0px; padding-top: 4px; padding-bottom: 4px;"><div class="slicerCheckbox" aria-hidden="true"><span class="glyphicon checkbox checkboxOutlineContrast" style="font-size: 16px;"></span></div><span class="slicerText" title="2ª SERIE A INTEGRAL ANUAL - 38561967" style="color: rgb(37, 36, 35); border-style: solid; border-color: rgb(96, 94, 92); border-width: 0px; font-size: 16px; font-family: &quot;Segoe UI&quot;, wf_segoe-ui_normal, helvetica, arial, sans-serif; line-height: 21px; font-weight: normal; font-style: normal; text-decoration: none;">2ª SERIE A INTEGRAL ANUAL - 38561967</span></div></div><div class="row" role="none"><div class="slicerItemContainer" role="option" aria-checked="false" aria-setsize="-1" aria-posinset="5" data-row-index="5" data-row-id="0:5" style="margin-left: 0px; padding-top: 4px; padding-bottom: 4px;"><div class="slicerCheckbox" aria-hidden="true"><span class="glyphicon checkbox checkboxOutlineContrast" style="font-size: 16px;"></span></div><span class="slicerText" title="2ª SERIE B INTEGRAL ANUAL - 38562031" style="color: rgb(37, 36, 35); border-style: solid; border-color: rgb(96, 94, 92); border-width: 0px; font-size: 16px; font-family: &quot;Segoe UI&quot;, wf_segoe-ui_normal, helvetica, arial, sans-serif; line-height: 21px; font-weight: normal; font-style: normal; text-decoration: none;">2ª SERIE B INTEGRAL ANUAL - 38562031</span></div></div><div class="row" role="none"><div class="slicerItemContainer" role="option" aria-checked="false" aria-setsize="-1" aria-posinset="6" data-row-index="6" data-row-id="0:6" style="margin-left: 0px; padding-top: 4px; padding-bottom: 4px;"><div class="slicerCheckbox" aria-hidden="true"><span class="glyphicon checkbox checkboxOutlineContrast" style="font-size: 16px;"></span></div><span class="slicerText" title="2ª SERIE C INTEGRAL ANUAL - 38562095" style="color: rgb(37, 36, 35); border-style: solid; border-color: rgb(96, 94, 92); border-width: 0px; font-size: 16px; font-family: &quot;Segoe UI&quot;, wf_segoe-ui_normal, helvetica, arial, sans-serif; line-height: 21px; font-weight: normal; font-style: normal; text-decoration: none;">2ª SERIE C INTEGRAL ANUAL - 38562095</span></div></div><div class="row" role="none"><div class="slicerItemContainer" role="option" aria-checked="false" aria-setsize="-1" aria-posinset="7" data-row-index="7" data-row-id="0:7" style="margin-left: 0px; padding-top: 4px; padding-bottom: 4px;"><div class="slicerCheckbox" aria-hidden="true"><span class="glyphicon checkbox checkboxOutlineContrast" style="font-size: 16px;"></span></div><span class="slicerText" title="3ª SERIE A INTEGRAL ANUAL - 38473618" style="color: rgb(37, 36, 35); border-style: solid; border-color: rgb(96, 94, 92); border-width: 0px; font-size: 16px; font-family: &quot;Segoe UI&quot;, wf_segoe-ui_normal, helvetica, arial, sans-serif; line-height: 21px; font-weight: normal; font-style: normal; text-decoration: none;">3ª SERIE A INTEGRAL ANUAL - 38473618</span></div></div><div class="row" role="none"><div class="slicerItemContainer" role="option" aria-checked="false" aria-setsize="-1" aria-posinset="8" data-row-index="8" data-row-id="0:8" style="margin-left: 0px; padding-top: 4px; padding-bottom: 4px;"><div class="slicerCheckbox" aria-hidden="true"><span class="glyphicon checkbox checkboxOutlineContrast" style="font-size: 16px;"></span></div><span class="slicerText" title="3ª SERIE B INTEGRAL ANUAL - 38473681" style="color: rgb(37, 36, 35); border-style: solid; border-color: rgb(96, 94, 92); border-width: 0px; font-size: 16px; font-family: &quot;Segoe UI&quot;, wf_segoe-ui_normal, helvetica, arial, sans-serif; line-height: 21px; font-weight: normal; font-style: normal; text-decoration: none;">3ª SERIE B INTEGRAL ANUAL - 38473681</span></div></div></div>