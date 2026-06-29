#Menu
import json
import os

if os.path.exists('chamados.json'):
    with open('chamados.json', 'r') as arquivo:
        chamados = json.load(arquivo)
else:
    chamados = []
alternativa = 0
while alternativa != 5:
    print('-' * 60)
    print(' | Olá, você está no sistema de ajuda. Como posso ajudar? | ')
    print('-' * 60)
    print(' | 1 - Novo Chamado    | ')
    print(' | 2 - Listar Chamados | ')
    print(' | 3 - Buscar Chamado  | ')
    print(' | 4 - Alterar Status  | ')
    print(' | 5 - Sair            | ')
    print('-' * 60)
    alternativa1 = int(input(' | Para prosseguir informe qual é sua atual necessidade.  | R: '))
    alternativa = alternativa1
    print('-' * 60)
    if alternativa == 1:
        print(' | Você escolheu a opção [1] - Chamado | ')
        print(' | Insira os dados a seguir.           | ')
        print('-' * 60)
        nome = str(input(' Nome :'))
        setor = 0
        while setor != 1 and setor != 2 and setor != 3 and setor != 4 and setor != 5 and setor != 6 and setor != 7 and setor != 8:
            print(' Setores: ')
            print(' | 1 - Financeiro  | ')
            print(' | 2 - RH          | ')
            print(' | 3 - Comercial   | ')
            print(' | 4 - Marketing   | ')
            print(' | 5 - Atendimento | ')
            print(' | 6 - TI          | ')
            print(' | 7 - Logística   | ')
            print(' | 8 - Diretoria   | ')
            setor = int(input('  Setor: '))
            if setor == 1:
                print(' | Você escolheu o Setor: Financeiro | ')
                nome_setor = 'Financeiro'
            elif setor == 2:
                print(' | Você escolheu o Setor: RH | ')
                nome_setor = 'RH'
            elif setor == 3:
                print(' | Você escolheu o Setor: Comercial | ')
                nome_setor = 'Comercial'
            elif setor == 4:
                print(' | Você escolheu o Setor: Marketing | ')
                nome_setor = 'Marketing'
            elif setor == 5:
                print(' | Você escolheu o Setor: Atendimento | ')
                nome_setor = 'Atendimento'
            elif setor == 6:
                print(' | Você escolheu o Setor: TI | ')
                nome_setor = 'TI'
            elif setor == 7:
                print(' | Você escolheu o Setor: Logística | ')
                nome_setor = 'Logística'
            elif setor == 8:
                print(' | Você escolheu o Setor: Diretoria | ')
                nome_setor = 'Diretoria'
            else:
                print(' | A Escolha não existe! Escolha dentro das opções para prosseguir. | ')
        print(' Categorias: ')
        print(' | 1 - Hardware         | ')
        print(' | 2 - Windows          | ')
        print(' | 3 - Linux            | ')
        print(' | 4 - Microsoft Office | ')
        print(' | 5 - Rede / Internet  | ')
        print(' | 6 - Impressora       | ')
        print(' | 7 - E-mail / Outlook | ')
        print(' | 8 - Sistema Interno  | ')
        print(' | 9 - Senhas           | ')
        print(' | 10 - Outro           | ')
        categoria = 0
        while categoria != 1 and categoria != 2 and categoria != 3 and categoria != 4 and categoria != 5 and categoria != 6 and categoria != 7 and categoria != 8 and categoria != 9 and categoria != 10:
            categoria = int(input('  Categoria: '))
            if categoria == 1:
                print(' | Você escolheu o Categoria: Hardware | ')
                nome_categoria = 'Hardware'
                prioridade = 'Alta'
            elif categoria == 2:
                print(' | Você escolheu o Categoria: Windows | ')
                nome_categoria = 'Windows'
                prioridade = 'Média'
            elif categoria == 3:
                print(' | Você escolheu o Categoria: Linux | ')
                nome_categoria = 'Linux'
                prioridade = 'Alta'
            elif categoria == 4:
                print(' | Você escolheu o Categoria: Microsoft Office | ')
                nome_categoria = 'Microsoft Office'
                prioridade = 'Média'
            elif categoria == 5:
                print(' | Você escolheu o Categoria: Rede / Internet | ')
                nome_categoria = 'Rede / Internet'
                prioridade = 'Alta'
            elif categoria == 6:
                print(' | Você escolheu o Categoria: Impressora | ')
                nome_categoria = 'Impressora'
                prioridade = 'Baixa'
            elif categoria == 7:
                print(' | Você escolheu o Categoria: E-mail / Outlook | ')
                nome_categoria = 'E-mail / Outlook'
                prioridade = 'Média'
            elif categoria == 8:
                print(' | Você escolheu o Categoria: Sistema Interno | ')
                nome_categoria = 'Sistema Interno'
                prioridade = 'Média'
            elif categoria == 9:
                print(' | Você escolheu o Categoria: Senhas | ')
                nome_categoria = 'Senhas'
                prioridade = 'Baixa'
            elif categoria == 10:
                print(' | Você escolheu o Categoria: Outro | ')
                nome_categoria = 'Outro'
                prioridade = 'Baixa'
            else:
                print(' | A Escolha não existe! Escolha dentro das opções para prosseguir. | ')
        descricao = str(input(' Descrição: '))
        print('-' * 60)
        status = 'Aberto'
        chamado = {'nome':nome, 'setor':nome_setor, 'categoria':nome_categoria, 'descricao':descricao, 'prioridade':prioridade, 'status':status}
        chamados.append(chamado)
        with open('chamados.json', 'w') as arquivo:
            json.dump(chamados, arquivo, indent=4, ensure_ascii=False)
    elif alternativa == 2:
        print(' | Você escolheu a opção [2] - Listar Chamados | ')
        for chamado in chamados:
            print(' | ', chamado ['nome'])
    elif alternativa == 3:
        print(' | Você escolheu a opção [3] - Buscar Chamados           | ')
        print(' | Insira o dado a seguir para concluir a ação           | ')
        print('-' * 60)
        busca = str(input(' Nome :'))
        for chamado in chamados:
            if busca == chamado['nome']:
                print(' | Nome:', chamado['nome'])
                print(' | Setor:', chamado['setor'])
                print(' | Categoria:', chamado['categoria'])
                print(' | Descrição:', chamado['descricao'])
                print(' | Prioridade:', chamado['prioridade'])
                print(' | Status:', chamado['status'])
    elif alternativa == 4:
        print(' | Você escolheu a opção [4] - Alterar Status            | ')
        print(' | Insira o dado a seguir para concluir a ação           | ')
        print('-' * 60)
        busca = str(input(' Nome :'))
        for chamado in chamados:
            if busca == chamado['nome']:
                altera = 0
                while altera != 1 and altera != 2:
                    print('   Escolha um dos estados do chamado:   ')
                    print(' | [1] - Concluído    | ')
                    print(' | [2] - Em andamento | ')
                    altera = int(input(' R: '))
                    if altera == 1:
                        chamado['status'] = 'Concluído'
                        print('O novo status do chamado agora é "Concluído"')
                    elif altera == 2:
                        chamado['status'] = 'Em andamento'
                        print('O novo status do chamado agora é "Em andamento"')
                    else:
                        print(' | A Escolha não existe! Escolha dentro das opções para prosseguir. | ')
                with open('chamados.json', 'w') as arquivo:
                    json.dump(chamados, arquivo, indent=4, ensure_ascii=False)
    elif alternativa == 5:
        print('O programa será encerrado!')
    else:
        print('A Alternativa escolhida é inexistente! Caso deseje encerrar o programa, escolha a alternativa [5] ')