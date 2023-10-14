# //logar responsavel
# 1 - Acessar https://escolatotal.educacao.sp.gov.br/
# 2 - Inserir RG
# 3 - Inserir Senha 
# 4 - Apertar Botão "acessar"
# //Puxar aluno
# 5 - Clicar botão "aluno presente"
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