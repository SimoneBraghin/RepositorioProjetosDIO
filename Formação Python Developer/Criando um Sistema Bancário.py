""" INSTRUÇÕES GERAIS:

    Fomos contratados por um grande banco para desenvolver o seu novo sistema. 
    Esse banco deseka modernizar suas operações e para isso escolheu a linguagem Python.
    Para a primeira versão do sistema devemos implementar apenas 3 operações:
    depósito, saque e extrato. """

""" OPERAÇÃO DEPÓSITO:

    Deve ser possível depositar valores positivos para a minha conta bancária.
    A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em 
    identificar qual é o número da agência e conta bancária.
    Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato. """

""" OPERAÇÃO DE SAQUE:

    O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500.00 por saque.
    Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar
    o dinheiro por falta de saldo.
    Todos os saques devem ser armazenados em uma variável e exibidos na operação extrato. """

""" OPERAÇÃO EXTRATO:
    
    Essa operação deve listar todos os depósitos e saques realizados na conta. 
    No fim da listagem deve ser exibido o saldo atual da conta.
    Os valores devem ser exibidos utilizando o formato R$ xxxxx.xx (Exemplo: 1500.45 = R$ 1500,45) """


saldo = 0
limite = 500.00
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Falta corrigir parte de retornos do fluxo de caixa do Débito para novo crédito.
# Como está: quando saldo + limite estão alterados, ao novo depósito o limite não retorna primeiro que o saldo... O copo 1 precisa encher antes do 2...
# Provavelmente o problema está na construção do bloco de opcao == 1 (depósito)


while True:
    try:
        print("\n >>>>>> Banco XP <<<<<< \n -- CAIXA ELETRÔNICO 24 HORAS --")
        opcao = int(input("\n----- MENU PRINCIPAL -----\n \n [1] Depositar \n [2] Sacar \n [3] Extrato \n [0] Sair\n\n Digite uma opção do Menu >> "))
        
        if opcao == 1:
            try:
                valor = float(input("\nInforme o valor do depósito: R$ "))
                
                if valor > 0:
                    saldo += valor
                    extrato += f"Depósito: R$ {valor:.2f} C\n"
                    while limite < 500:
                        limite += valor
                        if limite > 500:
                            limite = 500
                            break                        
                    print("\n>> Operação de Depósito concluída com sucesso! << \nRetornando ao Menu Principal... \n =================================")
                else:
                    print("Operação inválida! Informe valores positivos para depósito! \nRetornando ao Menu Principal")
            
            except ValueError:
                print("Operação falhou! O valor informado é inválido.\n =================================")

        elif opcao == 2:
            try:
                valor = float(input("\nInforme o valor do saque: R$ "))
                excedeu_saldo = valor > saldo
                excedeu_limite = valor > limite
                excedeu_saques = numero_saques >= LIMITE_SAQUES
                
                if excedeu_saldo:
                    print("\nVocê não tem saldo suficiente. \n")
                    limiteRequisitado = int(input("Deseja utilizar o Limite da sua conta?\n[1] Sim \n[0] Não \n>> "))
                    
                    if limiteRequisitado == 1:
                        valor = float(input("\nSaque do Cheque Especial | Confirme o valor do saque desejado: R$ "))
                        
                        if valor > 0 and valor <= (saldo + limite):
                            saldo -= valor
                            limite -= valor
                            extrato += f"Saque: R$ {valor:.2f} D\n"
                            numero_saques += 1
                            print("\n>> Operação de Saque concluída com sucesso! << \n\n Retire o dinheiro do compartimento \nRetornando ao Menu Principal... \n =================================")
                        
                        elif valor <= (saldo + limite):
                            saldo -= valor
                            while limite >= 0:
                                limite -= valor
                                if limite < 0:
                                    limite = 0
                                break
                            extrato += f"Saque: R$ {valor:.2f}\n"
                            numero_saques += 1
                            print("\n>> Operação de Saque concluída com sucesso! << \nRetornando ao Menu Principal... \n =================================")
                        else: 
                            print("\nLimite máximo de R$ 500.00 por saque. Retornando ao Menu Principal")
                    
                    elif limiteRequisitado == 0:
                        print("\nOperação cancelada.\nRetornando ao Menu Principal...")

                    else:
                        print("\nValor inválido. \nRetornando ao Menu Principal...")
                
                elif excedeu_saques:
                    print("Operação falhou! Número máximo de saques excedido.\n =================================")
                
                elif valor > 0:
                    saldo -= valor
                    extrato += f"Saque: R$ {valor:.2f} D\n"
                    numero_saques += 1
                    print("\n>> Operação de Saque concluída com sucesso! << \nRetornando ao Menu Principal... \n =================================")
            except ValueError:
                print("Operação falhou! O valor informado é inválido.\n =================================")

        elif opcao == 3:
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print(f"\nLimite | Cheque Especial: R$ {limite:.2f}")
            print(f"\nSaldo + Cheque Especial: R$ {saldo+limite:.2f}")
            print("==========================================")
            print("\nRetornando ao Menu Principal...\n")

        elif opcao == 0:
            print("\n========== O Banco XP agradece pela preferência! ========== \nSua sessão foi finalizada! \n \n** Banco XP ** \n** O impossível é só o começo! ** \n\n")
            break
        
        else: 
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            
    except ValueError:
        print("O valor informado é inválido. Selecione um número inteiro entre 1 a 4 ou aperte 0 para encerrar a operação.")