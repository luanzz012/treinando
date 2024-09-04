import os
lista = []
id_contador = 0
def pedir_produtos():
    global id_contador
    id_contador +=1
    while True:
        try:
            nome = input("Digite o NOME do produto: ").strip().upper()
            valor = float(input("Digite o VALOR do produto: "))
            qtd = int(input("Digite a QUANTIDADE do produto: "))
            break
        except ValueError:
            print("Você digitou alguma coisa ERRADA, adicione o produto novamente!\n")
            
    produto = {
    'id': id_contador ,
    'nome': nome,
    'valor': valor,
    'quantidade': qtd
}
    lista.append(produto)
    return  produto
    

def confirmar_correto():
    
    print(f'O NOME do produto está correto ?: {produto['nome']}')
    print("Digite (s) ou (n)")
    confirmaçao_nome =  input()
    os.system('cls') # limpar terminal

    print(f'O VALOR do produto está correto ?: {produto['valor']}')
    print("Digite (s) ou (n)")
    confirmaçao_valor =  input()
    os.system('cls')

    print(f'A QUANTIDADE do produto está correto ?: {produto['quantidade']}')
    print("Digite (s) ou (n)")
    confirmaçao_qtd =  input('\n')
    os.system('cls')
    
    if confirmaçao_nome.lower() =="s" and confirmaçao_valor == "s" and confirmaçao_qtd=="s":
        print("Produto confirmado com sucesso!\n")
        
    else:
        print('produto nao cadastrado!, digite novamente o produto\n')
        lista.remove(produto)  # Removendo o produto incorreto
        pedir_produtos()  # Pedindo novamente o produto

def remover_produto():
    if lista: # verifica se a lista nao esta vazia   
        print('produtos cadastrados: ') 

        for produto in lista: #itera sobre a lista e exibe todos os produtos 
            print(f"ID: {produto['id']} Nome: {produto['nome']}")
        escolha = int(input("Digite o ID do produto que deseja excluir: ")) 

         # Tenta encontrar o produto na lista com base no ID fornecido
        produto_remover = next((p for p in lista if p['id'] == escolha), None)

        if produto_remover:  # Se encontrar o produto
            lista.remove(produto_remover)  # Remove o produto da lista
            print(f"Produto {produto_remover['nome']} removido com sucesso.\n")

        else:  # Se o produto com o ID fornecido não for encontrado
            print("ID não encontrado.\n")

    else:  # Se a lista estiver vazia
        print("Nenhum produto cadastrado para remover.\n")


produto = pedir_produtos()   
confirmar_correto()

 
while True:
    try:
        print('Caso deseja adicinar outro produto digite (1)')
        print('Caso deseja remover um produto digite (2)')
        print('Caso deseja ver os cadastros digite (3)')
        print('Caso deseje sair, digite (0)')
        opcao = int(input())

        if opcao == 1:
            pedir_produtos()
            confirmar_correto()
            
            print(lista)
        elif opcao == 2:
            remover_produto()
            
        elif opcao ==3:
            print("Produtos cadastrados:")
            for produto in lista:
                print(f"ID: {produto['id']} - Nome: {produto['nome']} - Valor: {produto['valor']} - Quantidade: {produto['quantidade']}\n")

        elif opcao == 0:
            print("Saindo...")
            exit()
        else:
            print("Opção inválida. Tente novamente.")
            break
    except ValueError:
        print("voce digitou errado")
        




