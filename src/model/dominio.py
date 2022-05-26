class Usuario:
    def __init__(self, nome: str):
        self.nome = nome


class Lance:
    def __init__(self, usuario, valor: float):
        self.usuario = usuario
        self.valor = valor


class Leilao:
    def __init__(self, descricao: str, valor_minimo: float):
        if valor_minimo <= 0:
            raise Exception('valor minimo do leilao deve ser positivo')
        self.descricao = descricao
        self.lances = []
        self.ativo = True
        self.valor_minimo = valor_minimo

    def realizaLance(self, lance: Lance):
        if self.ativo:
            self.processarLance(lance)
        else:
            raise Exception('leilao não esta ativo')

    def processarLance(self, lance: Lance):
        if lance.valor >= self.valor_minimo:
            for lances_ativos in self.lances:
                if lances_ativos.valor == lance.valor:
                    raise Exception('lance de mesmo valor já existe')
            self.lances.append(lance)
        else:
            raise Exception('lance menor que o valor mínimo')

    def quantidadeLances(self):
        return len(self.lances)

class Avaliador:
    def __init__(self):
        self.maior_lance = None

    def avaliarLeilao(self, leilao):
        if leilao.quantidadeLances() < 3:
            raise Exception('Não é possível avaliar um leilao sem pelo menos três lance')
        for lance in leilao.lances:
            if self.maior_lance is None:
                self.maior_lance = lance
            elif self.maior_lance.valor < lance.valor:
                self.maior_lance = lance
        leilao.ativo = False
