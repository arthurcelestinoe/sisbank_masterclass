menu = """
Por favor, digite o número correspondente a operação desejada e tecle [enter]:
                        [1] Deposito
                        [2] Saque
                        [3] Extrato
                        [4] Sair do Sistema
==> 
"""
saldo = 15000
extrato = """
"""
SAQUES_POR_DIA = 3
LIMITES_VALOR_SAQUE = 500
saques_efetuados = 0

print("Olá! Seja bem-vindo ao Banco MasterClass.")
while True:
    opcao = int(input(menu))
    if opcao == 1:
        valor = float(input("Por favor informe o valor do Depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print("Operação concluida com sucesso!!!!")
        else: 
            print("O valor digitado não é valído. Por Favor tente novamente.")
    elif opcao == 2:
        valor = float(input("Por Favor informe o valor do saque: "))
        if (saques_efetuados < SAQUES_POR_DIA) and (valor <= LIMITES_VALOR_SAQUE) and (valor <= saldo):
            saldo -= valor
            saques_efetuados += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
            print("Tudo certo! Seu saque foi concluído com sucesso!")
        else:
            print("Não foi possível realizar está operação, por favor verifique seus limites e seu saldo e tente novamente.")
    elif opcao == 3:
        print(f"{extrato}\nSeu saldo atual é de R$ {saldo:.2f}")
    elif opcao == 4:
        print("Obrigado por utilizar nossos sistemas!!")
        break
    else: 
        print("Opção inválida! Tente Novamente!")