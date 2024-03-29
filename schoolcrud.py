"""
Natalia Marçon Botteon
Superior de Tecnologia em Análise e Desenvolvimento de Sistemas
"""
import os
import json


def exibir_menu_principal():
    """
    Exibe o menu principal do programa.

    :return: None
    """
    print('''
----- MENU PRINCIPAL -----

1 - Gerenciar estudantes.
2 - Gerenciar professores.
3 - Gerenciar disciplinas.
4 - Gerenciar turmas.
5 - Gerenciar matrículas.
9 - Sair.
    ''')
    escolha = int(input("Informe a opção desejada: "))

    if escolha == 1:
        exibir_menu_secundario("ESTUDANTES")

    elif escolha == 2:
        exibir_menu_secundario("PROFESSORES")

    elif escolha == 3:
        exibir_menu_secundario("DISCIPLINAS")

    elif escolha == 4:
        exibir_menu_secundario("TURMAS")

    elif escolha == 5:
        exibir_menu_secundario("MATRÍCULAS")

    elif escolha == 9:
        print("Até mais!")

    else:
        print("Opção inválida! Tente novamente")
        exibir_menu_principal()

    return


def exibir_menu_secundario(tabela):
    """
    Exibe o menu secundário de gerenciamento de uma tabela específica.

    :param tabela: Nome da tabela a ser gerenciada.
    :return: None
    """
    print(f'''
***** GERENCIAR {tabela} *****

1 - Incluir.
2 - Listar.
3 - Atualizar.
4 - Excluir.
5 - Voltar ao menu principal.
            ''')

    escolha = int(input("Informe a opção desejada: "))

    if escolha == 1:
        incluir(tabela)

    elif escolha == 2:
        listar(tabela)

    elif escolha == 3:
        atualizar(tabela)

    elif escolha == 4:
        excluir(tabela)

    elif escolha == 5:
        exibir_menu_principal()

    else:
        print("Opção inválida! Tente novamente")
        exibir_menu_secundario(tabela)

    return


def pedir_dados_estudantes():
    """
    Solicita os dados de um estudante para inclusão.

    :return: Dicionário com os dados do estudante.
    """
    while True:
        try:
            codigo = int(input("Digite o código do estudante: "))
            nome = str(input("Digite o nome completo do estudante: "))
            cpf = str(input("Digite o CPF do estudante: "))
            estudante = {"Código": codigo, "Nome": nome, "CPF": cpf}
            break
        except ValueError:
            print("Erro: Entrada inválida. Confira os dados e tente novamente!")
    return estudante


def pedir_dados_professores():
    """
    Solicita os dados de um professor para inclusão.

    :return: Dicionário com os dados do professor.
    """
    while True:
        try:
            codigo = int(input("Digite o código do professor: "))
            nome = str(input("Digite o nome do professor: "))
            cpf = str(input("Digite o CPF do professor: "))
            professor = {"Código": codigo, "Nome": nome, "CPF": cpf}
            break
        except ValueError:
            print("Erro: Entrada inválida. Confira os dados e tente novamente!")
    return professor


def pedir_dados_disciplinas():
    """
    Solicita os dados de uma disciplina para inclusão.

    :return: Dicionário com os dados da disciplina.
    """
    while True:
        try:
            codigo = int(input("Digite o código da disciplina: "))
            nome = str(input("Digite o nome da disciplina: "))
            disciplina = {"Código": codigo, "Nome": nome}
            sem_dados = False
            break
        except ValueError:
            print("Erro: Entrada inválida. Confira os dados e tente novamente!")
    return disciplina


def pedir_dados_turmas():
    """
    Solicita os dados de uma turma para inclusão.

    :return: Dicionário com os dados da turma.
    """
    while True:
        try:
            codigo = int(input("Digite o código da turma: "))
            codigo_prof = int(input("Digite o código do professor: "))
            codigo_disciplina = int(input("Digite o código da disciplina: "))
            turma = {"Código": codigo, "Professor": codigo_prof, "Disciplina": codigo_disciplina}
            break
        except ValueError:
            print("Erro: Entrada inválida. Confira os dados e tente novamente!")
    return turma


def pedir_dados_matriculas():
    """
    Solicita os dados de uma matrícula para inclusão.

    :return: Dicionário com os dados da matrícula.
    """
    while True:
        try:
            codigo = int(input("Digite o número da turma: "))
            codigo_estudante = str(input("Digite o código do estudante: "))
            matricula = {"Número da matrícula": codigo, "Estudante": codigo_estudante}
            break
        except ValueError:
            print("Erro: Entrada inválida. Confira os dados e tente novamente!")
    return matricula


def salvar():
    with open("tabelas.json", "w", encoding="utf-8") as arquivo:
        json.dump(tabelas, arquivo, ensure_ascii=False)


def recuperar():
    dados = {"ESTUDANTES": [], "PROFESSORES": [], "DISCIPLINAS": [], "TURMAS": [], "MATRÍCULAS": []}
    if os.path.isfile("tabelas.json"):
        with open("tabelas.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    return dados


def incluir(tabela):
    """
    Realiza a inclusão de um registro na tabela especificada.

    :param tabela: Nome da tabela onde será feita a inclusão.
    :return: None
    """
    if tabela == "ESTUDANTES":
        dados_incluir = pedir_dados_estudantes()

    elif tabela == "PROFESSORES":
        dados_incluir = pedir_dados_professores()

    elif tabela == "DISCIPLINAS":
        dados_incluir = pedir_dados_disciplinas()

    elif tabela == "TURMAS":
        dados_incluir = pedir_dados_turmas()

    elif tabela == "MATRÍCULAS":
        dados_incluir = pedir_dados_matriculas()

    tabelas[tabela].append(dados_incluir)
    salvar()
    print(f"{tabela} cadastrado com sucesso!")
    exibir_menu_secundario(tabela)
    return


def listar(tabela):
    """
    Lista os registros da tabela especificada.

    :param tabela: Nome da tabela a ser listada.
    :return: None
    """
    dados_tabela = tabelas[tabela]
    ordem = 0
    for i in dados_tabela:
        ordem += 1
        print(f"{ordem} - {i}")

    exibir_menu_secundario(tabela)
    return


def atualizar(tabela):
    """
    Atualiza um registro na tabela especificada.

    :param tabela: Nome da tabela onde será feita a atualização.
    :return: None
    """
    dados_tabela = tabelas[tabela]
    ordem = 0
    for i in dados_tabela:
        ordem += 1
        print(f"{ordem} - {i}")

    ordem_atualizar = int(input("Digite o número do registro que deseja atualizar: "))

    if tabela == "ESTUDANTES":
        dados_atualizar = pedir_dados_estudantes()

    elif tabela == "PROFESSORES":
        dados_atualizar = pedir_dados_professores()

    elif tabela == "DISCIPLINAS":
        dados_atualizar = pedir_dados_disciplinas()

    elif tabela == "TURMAS":
        dados_atualizar = pedir_dados_turmas()

    elif tabela == "MATRÍCULAS":
        dados_atualizar = pedir_dados_matriculas()

    tabelas[tabela][ordem_atualizar - 1] = dados_atualizar
    salvar()
    print("Dado atualizado com sucesso!")

    exibir_menu_secundario(tabela)
    return


def excluir(tabela):
    """
    Exclui um registro na tabela especificada.

    :param tabela: Nome da tabela onde será feita a exclusão.
    :return: None
    """
    dados_tabela = tabelas[tabela]
    ordem = 0
    for i in dados_tabela:
        ordem += 1
        print(f"{ordem} - {i}")

    ordem_excluir = int(input("Digite o número do registro que deseja excluir: "))
    tabelas[tabela].pop(ordem_excluir - 1)
    salvar()
    print("Dado excluído com sucesso!")
    exibir_menu_secundario(tabela)
    return


tabelas = recuperar()
exibir_menu_principal()