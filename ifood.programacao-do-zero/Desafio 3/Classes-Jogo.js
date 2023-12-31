
class HeroiAtributos {
    constructor(nome, idade, inimigo, tipo, ataque) {
        this.nome = nome;
        this.idade = idade;
        this.inimigo = inimigo;
        this.tipo = tipo;
        this.ataque = ataque;
    }

    comunicado() {
        console.log(`o ${this.tipo} ${this.nome}, aos seus ${this.idade} anos, atacou ${this.inimigo} usando ${this.ataque}!`);
    }
}

const ataqueMago = new HeroiAtributos("mago", "Circe", 20, "Kraken", "magia");
const ataqueGuerreiro = new HeroiAtributos("guerreiro", "Duque Valentino", 25, "Duque de Milão", "espada");
const ataqueMonge = new HeroiAtributos("monge", "Beatrix Kiddo", 26, "Bill", "artes marciais");
const ataqueNinja = new HeroiAtributos("ninja", "Hattori Hanzo", 18, "Toyotomi Hideyoshi", "shuriken");
const ataqueSamurai = new HeroiAtributos("samurai", "Miyamoto Musashi", "20", "Sasaki Kojiro", "Niten Ichi-ryu");

ataqueMago.comunicado();
ataqueGuerreiro.comunicado();
ataqueMonge.comunicado();
ataqueNinja.comunicado();
ataqueSamurai.comunicado();

