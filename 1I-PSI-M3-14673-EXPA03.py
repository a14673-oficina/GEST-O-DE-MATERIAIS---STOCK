#Função para adicionar o material
def adicionar_material(stock):
    nome = input("Nome do material: ")
    if nome in stock:
        print("O material já existe no stock!")
    else:
        try:
            quantidade = int(input(f"Quantidade inicial de {nome}: "))
            if quantidade < 0:
                print("Erro: A quantidade não pode ser negativa.")
            else:
                stock[nome] = quantidade
                print(f"{nome} adicionado com sucesso!")
        except ValueError:
            print("Erro: A quantidade deve ser um número inteiro.")

#Função para consultar o stock
def consultar_stock(stock):
    nome = input("Nome do material para consulta: ")
    if nome in stock:
        print(f"O stock atual de {nome} é: {stock[nome]}")
    else:
        print(f"{nome} não encontrado no stock.")

#Função para atualizar o stock
def atualizar_stock(stock):
    nome = input("Nome do material a atualizar: ")
    if nome in stock:
        operacao = input("Deseja adicionar (A) ou remover (R)? ").upper()
        try:
            quantidade = int(input("Quantidade: "))
            if quantidade < 0:
                print("Erro: A quantidade não pode ser negativa.")
                return
            if operacao == "A":
                stock[nome] += quantidade
                print(f"{quantidade} unidade(s) adicionada(s) ao stock de {nome}.")
            elif operacao == "R":
                if quantidade <= stock[nome]:
                    stock[nome] -= quantidade
                    print(f"{quantidade} unidade(s) removida(s) do stock de {nome}.")
                else:
                    print("Quantidade insuficiente em stock!")
            else:
                print("Operação inválida!")
        except ValueError:
            print("Erro: A quantidade deve ser um número inteiro.")
    else:
        print(f"{nome} não encontrado no stock.")

#Função para exibir o stock
def exibir_stock(stock):
    print("\nEstado Geral do Stock:")
    print(f"{'Material':<15}{'Quantidade':<10}")
    print("-" * 25)
    for material, quantidade in stock.items():
        print(f"{material:<15}{quantidade:<10}")
        
#Função para fazer print
def stosk_file():
    f = open("s.txt", "r")
    print(f.read())
    
#Função que executa a intreface do menu
def main():
    stock = {}
    while True:
        print("\nGestão de Stock")
        print("1. Adicionar Material")
        print("2. Consultar Stock")
        print("3. Atualizar Stock")
        print("4. Exibir Stock Geral")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_material(stock)
        elif opcao == "2":
            consultar_stock(stock)
        elif opcao == "3":
            atualizar_stock(stock)
        elif opcao == "4":
            exibir_stock(stock)
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
