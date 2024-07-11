from modelos.avaliacao import Avaliacao;

class Restaurante:
    restaurantes = [];

    def __init__(self, nome, categoria):
        self._nome = nome.title();
        self._categoria = categoria.title();
        self._estado = False;
        self._avaliacao = [];
        Restaurante.restaurantes.append(self);

    def __str__(self):
        return f'{self.nome} | {self.categoria}';

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Estado'}');
        print(f'-' * 100);
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.estado}');

    @property
    def estado(self):
        return 'Ativo ☑' if self._estado else 'Desativado ☒';

    def alternar_estado(self):
        self._estado = not self._estado;

    def receber_avaliacao(self, cliente, nota):
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota);
            self._avaliacao.append(avaliacao);

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Sem avaliações';

        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao);
        qtd_notas = len(self._avaliacao);
        media = round(soma_notas / qtd_notas, 1);
        
        return media;