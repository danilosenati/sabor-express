import os

# restaurantes = ["Boa Muqueca", "Nosso Prato", "Prato Vazio"] # LISTA DE RESTAURANTES

# CRIANDO UM LISTA DE DICIONARIO:
restaurantes = [{"Nome":"Boa Muqueca", "Categoria":"Baiana", "status_ativo": True},
                {"Nome": "Nosso Prato", "Categoria":"Gourmet","status_ativo": False},
                {"Nome": "Prato Vazio", "Categoria": "Vegano","status_ativo":True}
               ]

def nome_programa():
    print("""
       𝘴𝘢𝘣𝘰𝘳-𝘦𝘹𝘱𝘳𝘦𝘴𝘴
    """)
def exibir_opcoes():

    # Exibe as opções disponíveis no menu principal.

    print("1 - Cadastrar restaurante:")
    print("2 - Listar restaurante:")
    print("3 - Modificar estado do restaurante:")
    print("4 - Sair: ")

# FUNÇÃO EM PYTHON
def finalizar_app():

    # Exibe mensagem de finalização do aplicativo

   exibir_subtitulo("Finalizando o app")
   # exit()

def voltar_ao_menu_principal():

    ''' Solicita uma tecla para voltar ao menu principal '''

    input("Pressione enter para voltar ao menu principal: ")
    main()  # Chamando a função para que o programa seja novamente executado

def opcao_invalida():

    # Exibe mensagem de opção inválida e retorna ao menu principal

   print("Opção invalida!")
   voltar_ao_menu_principal()

def exibir_subtitulo(texto):

    # Exibe um subtitulo estilizado na tela

    os.system("cls") # comando que vai limpar o terminal
    linha = "+" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():

    # Essa função é responsável por cadastrar um novo restaurante

    exibir_subtitulo("Cadastro de novos restaurantes")

    nome_do_restaurante = input("Digite o nome do restaurante: ")
    categoria = input("Digite a categoria do restaurante")
    status = input("Digite True ou False para o status do restaurante: ")

    novo_restaurante = {
        "Nome": nome_do_restaurante,
        "Categoria": categoria,
        "status_ativo": status
    }

    restaurantes.append(novo_restaurante)

    print(f"O restaurante {nome_do_restaurante}, foi cadastrado com sucesso!\n")

    voltar_ao_menu_principal()

def listar_restaurantes():

    # Lista os restaurantes presentes na lista

    exibir_subtitulo("Listando os restaurantes:")

    print(f'{'Nome do restaurante'.ljust(21)} | {'Categoria'.ljust(20)} | Status')

    # PARA CADA RESTAURANTE NA LISTA RESTAURANTE:
    for restaurant in restaurantes:
        nome_restaurante = restaurant["Nome"]
        categoria_restaurante = restaurant["Categoria"]
        status_restaurante = "ativado" if restaurant["status_ativo"] else "desativado"
        print(f" * {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {status_restaurante}")

    voltar_ao_menu_principal()

def alternar_estado_restaurante():

    '''
    Altera o estado ativo/desativado de um restaurante

    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''

    exibir_subtitulo("Alterando estado do restaurante")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False

    for restaurant in restaurantes:
        if nome_do_restaurante == restaurant["Nome"]:
            restaurante_encontrado = True
            restaurant["status_ativo"] = not restaurant["status_ativo"]
            mensagem = f"O restaurante {nome_do_restaurante} foi ativado com sucesso" if restaurant["status_ativo"]  else f"O restaurante {nome_do_restaurante} foi desativado com sucesso."
            print(mensagem)

    if not restaurante_encontrado:
        print(f"O restaurante {nome_do_restaurante} não foi encontrado!")

    voltar_ao_menu_principal()

def escolher_opcao():

    # Solicita e executa a opção escolhida pelo usuário

   try:
        opcao = int (input("Escolha uma opção: "))

        if opcao == 1:
            cadastrar_novo_restaurante()
        elif opcao == 2:
                listar_restaurantes()
        elif opcao == 3:
                alternar_estado_restaurante()
        elif opcao == 4:
            finalizar_app()
        else:
            opcao_invalida() # chamando a função
   except:
       opcao_invalida()


def main():

    # função principal qye inicia o programa

    os.system("cls")
    nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()
