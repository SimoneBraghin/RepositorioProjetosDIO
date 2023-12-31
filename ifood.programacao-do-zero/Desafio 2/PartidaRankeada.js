//Vamos tentar em JavaScript =] realizar o cálculo de partidas rankeadas! 

// Instruções do Felipão:
`
Instruções para entrega
# 2️⃣ Calculadora de partidas Rankeadas

**O Que deve ser utilizado**

- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões
- Funções

## Objetivo:

Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)

Se vitórias for menor do que 10 = Ferro
Se vitórias for entre 11 e 20 = Bronze
Se vitórias for entre 21 e 50 = Prata
Se vitórias for entre 51 e 80 = Ouro
Se vitórias for entre 81 e 90 = Diamante
Se vitórias for entre 91 e 100= Lendário
Se vitórias for maior ou igual a 101 = Imortal

## Saída

Ao final deve se exibir uma mensagem:
"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**" 
`

let vitorias = 50;
let derrotas = 10;

const resultado = ScoreCalc(vitorias, derrotas);
const saldoVitorias = resultado[0];
const nivel = resultado[1];

function ScoreCalc(vitorias, derrotas) {
    let saldoVitorias = vitorias - derrotas;
    let nivel = '';

    if (vitorias <10) {
        nivel = 'Ferro';
    } else if (vitorias >= 10 && vitorias <= 20){
        nivel = 'Bronze';
    }else if (vitorias > 20 && vitorias <= 50){
        nivel = 'Prata';
    }else if (vitorias > 50 && vitorias <= 80){
        nivel = 'Ouro';
    }else if (vitorias > 80 && vitorias <= 90){
        nivel = 'Diamante';
    }else if (vitorias > 90 && vitorias <= 100){
        nivel = 'Lendário';
    }else if (vitorias > 100){
        nivel = 'Imortal';
    }
    return [saldoVitorias, nivel]
    }

console.log(`O Herói tem de saldo de ${saldoVitorias} e está no nível ${nivel}`);



