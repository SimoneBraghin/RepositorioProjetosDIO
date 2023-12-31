#Desafio Felipão

# ****INSTRUÇÕES****
"""
# 1️⃣ Desafio Classificador de nível de Herói

**O Que deve ser utilizado**

- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões

## Objetivo

Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, 
depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

Se XP for menor do que 1.000 = Ferro
Se XP for entre 1.001 e 2.000 = Bronze
Se XP for entre 2.001 e 5.000 = Prata
Se XP for entre 6.001 e 7.000 = Ouro
Se XP for entre 7.001 e 8.000 = Platina
Se XP for entre 8.001 e 9.000 = Ascendente
Se XP for entre 9.001 e 10.000= Imortal
Se XP for maior ou igual a 10.001 = Radiante

## Saída

Ao final deve se exibir uma mensagem:
"O Herói de nome **{nome}** está no nível de **{nivel}**"
"""

nomeHeroi = "Dona Aranha"
idadeHeroi = 15
XP = 0
vilao = "Chuva forte"


while XP < 10001:
    if XP < 1000:
        nivel = "Ferro"
    elif 1001 <= XP <= 2000:
        nivel = "Bronze"
    elif 2001 <= XP <= 5000:
        nivel = "Prata"
    elif 6001 <= XP <= 7000:
        nivel = "Ouro"
    elif 7001 <= XP <= 8000:
        nivel = "Platina"
    elif 8001 <= XP <= 9000:
        nivel = "Ascendente"
    elif 9001 <= XP <= 10000:
        nivel = "Imortal"
    else:
        nivel = "Radiante"
    
    print(f"O Herói de nome {nomeHeroi} está no nível de {nivel}")
    XP += 1000


    
print(f"{nomeHeroi} viu luzes de Unicórnios e ganhou XP! Agora XP é {XP} e seu nível é {nivel}!")
print(f"Parabéns {nomeHeroi}! Após {idadeHeroi} anos lutando contra {vilao}, você finalmente subiu ao Panteão dos Deuses imortais!")


opcao = input("Escolha uma opção:\n1. Finalizar\n2. Reiniciar")

opcao = int(opcao)

if opcao == 1:
    print(f"Você escolheu a Opção 1. Quando quiser, suba você uma parede íngreme com {vilao} na sua cabeça!")
elif opcao == 2:
    print(f"Você escolheu a Opção 2. Vamos reiniciar seu jogo! A {vilao} derrubou {nomeHeroi}. Agora {nomeHeroi} vai subir tudo de novo, #Coitade!")
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")

print("Ps. toda violência deste jogo é justificada como boas doses de humor! rs")
