from modelos.restaurante import Restaurante;

restaurante_praça = Restaurante('Praça', 'Gourmet');
restaurante_pizza = Restaurante('Pizza Express', 'Italiana');
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana');

restaurante_mexicano.alternar_estado();
restaurante_mexicano.receber_avaliacao('Max', 4);
restaurante_mexicano.receber_avaliacao('Max', 5);
restaurante_mexicano.receber_avaliacao('Max', 2);


def main():
    Restaurante.listar_restaurantes();

if __name__ == '__main__':
    main();