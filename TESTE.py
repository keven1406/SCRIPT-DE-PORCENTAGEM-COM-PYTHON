def porcentagem (numero):
    x = numero * 17 / 100
    return numero + x

linhas = int(input("Digite a quantidade de linhas da tabela: "))
contador = 1
while contador <= linhas:
    try:
        unidade = int(input("Digite a quantidade: "))
        valor = float(input("Digite o valor: "))
        valorItem = porcentagem(valor)
        valorUnidadeTotal = unidade * valorItem

        print(f"{contador} - Quantidade: {unidade} Valor Unitario: {valorItem}, Valor total: {valorUnidadeTotal}")
        contador += 1
    except KeyboardInterrupt:
        print("Aplicativo encerrado pelo Usuario")
        break
    except:
         print("digite um numero valido")
