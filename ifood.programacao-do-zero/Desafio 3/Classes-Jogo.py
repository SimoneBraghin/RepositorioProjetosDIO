"""
    Instruções para entrega
# 3️⃣ Escrevendo as classes de um Jogo

**O Que deve ser utilizado**

- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões
- Funções
- Classes e Objetos

## Objetivo:

Crie uma classe generica que represente um herói de uma aventura e que possua as seguintes propriedades:

- nome
- idade
- tipo (ex: guerreiro, mago, monge, ninja )

além disso, deve ter um método chamado atacar que deve atender os seguientes requisitos:

- exibir a mensagem: "o {tipo} atacou usando {ataque}")
- aonde o {tipo} deve ser concatenando o tipo que está na propriedade da classe
- e no {ataque} deve seguir uma descrição diferente conforme o tipo, seguindo a tabela abaixo:

se mago -> no ataque exibir (usou magia)
se guerreiro -> no ataque exibir (usou espada)
se monge -> no ataque exibir (usou artes marciais)
se ninja -> no ataque exibir (usou shuriken)

## Saída

Ao final deve se exibir uma mensagem:

- "o {tipo} atacou usando {ataque}"
  ex: mago atacou usando magia
  guerreiro atacou usando espada
"""

class heroiAtributos:
    def __init__(self, nome, idade, inimigo, tipo, ataque):
        self.nome = nome
        self.idade = idade
        self.inimigo = inimigo
        self.tipo = tipo
        self.ataque = ataque

    def comunicado(self):
        print(f"o {self.tipo} {self.nome}, aos seus {self.idade} anos, atacou {self.inimigo} usando {self.ataque}!")

ataqueMago = heroiAtributos("mago", "Circe", 20, "Kraken", "magia")
ataqueGuerreiro = heroiAtributos("guerreiro", "Duque Valentino", 25, "Duque de Milão", "espada")
ataqueMonge = heroiAtributos("monge", "Beatrix Kiddo", 26, "Bill", "artes marciais")
ataqueNinja = heroiAtributos("ninja", "Hattori Hanzo", 18, "Toyotomi Hideyoshi", "shuriken")
ataqueSamurai = heroiAtributos("samurai", "Miyamoto Musashi", "20", "Sasaki Kojiro", "Niten Ichi-ryu")

ataqueMago.comunicado()
ataqueGuerreiro.comunicado()
ataqueMonge.comunicado()
ataqueNinja.comunicado()
ataqueSamurai.comunicado()