from unittest import TestCase
from src.model.dominio import Usuario, Leilao, Lance, Avaliador


class TestLeilao(TestCase):
    def test_verifica_maior_lance(self):
        asaph = Usuario('Asaph')
        lance_asaph = Lance(asaph, 10.0)

        valtim = Usuario('Valterlim')
        lance_valtim = Lance(valtim, 10000.0)

        carlos = Usuario('Carlos')
        lance_carlos = Lance(carlos, 20.0)

        leilao = Leilao("BMW", 5)
        leilao.realizaLance(lance_asaph)
        leilao.realizaLance(lance_valtim)
        leilao.realizaLance(lance_carlos)

        irvayne = Avaliador()
        irvayne.avaliarLeilao(leilao)

        maior_lance_esperado = irvayne.maior_lance

        self.assertEqual(maior_lance_esperado, lance_valtim)

    def test_verifica_nome_do_maior_lance(self):
        asaph = Usuario('Asaph')
        lance_asaph = Lance(asaph, 10.0)

        valtim = Usuario('Valterlim')
        lance_valtim = Lance(valtim, 10000.0)

        carlos = Usuario('Carlos')
        lance_carlos = Lance(carlos, 20.0)

        leilao = Leilao("BMW", 10)

        leilao.realizaLance(lance_asaph)
        leilao.realizaLance(lance_valtim)
        leilao.realizaLance(lance_carlos)

        irvayne = Avaliador()
        irvayne.avaliarLeilao(leilao)

        nome_esperado = valtim.nome
        nome_obtido = irvayne.maior_lance.usuario.nome

        self.assertEqual(nome_esperado, nome_obtido)

    def test_verifica_lances_iguais(self):
        regla = Usuario('Regla')
        lance_regla = Lance(regla, 10)
        ryan = Usuario('Ryan')
        lance_ryan = Lance(ryan, 10)

        leilao_iphone = Leilao("iPhone", 10)
        deu_certo_lance_regla = leilao_iphone.realizaLance(lance_regla)

        with self.assertRaises(Exception):
            deu_certo_lance_ryan = leilao_iphone.realizaLance(lance_ryan)

        qtd_lances = leilao_iphone.quantidadeLances()

        self.assertEqual(1, qtd_lances)

    def test_verifica_lance_com_leilao_finalizado(self):
        lance_irvayne = Lance(Usuario("Irvayne"), 100)
        lance_gustavo = Lance(Usuario("Gustavo"), 200)
        lance_fabricio = Lance(Usuario("Fabricio"), 300)

        leilao = Leilao("iPhone", 100)

        leilao.realizaLance(lance_irvayne)
        leilao.realizaLance(lance_gustavo)
        leilao.realizaLance(lance_fabricio)

        avaliador = Avaliador()
        avaliador.avaliarLeilao(leilao)

        lance_matheus = Lance(Usuario("Matheus"), 200)
        with self.assertRaises(Exception):
            leilao.realizaLance(lance_matheus)
        avaliador.avaliarLeilao(leilao)

        ganhador = avaliador.maior_lance

        self.assertEqual(lance_fabricio, ganhador)

    def test_verifica_lance_menor_que_o_minimo(self):
        leilao = Leilao("iPhone", 200)
        lance_irvayne = Lance(Usuario("Irvayne"), 100)
        with self.assertRaises(Exception):
            leilao.realizaLance(lance_irvayne)

    def test_exception_divisao_por_zero(self):
        resultado = 0
        try:
            print("Iniciando a operação")
            resultado = 10/0
            print("Resultado: "+ str(resultado))
        except:
            print("Não é possível realizar divisão por zero")
        print(resultado)

    def test_verifica_avaliar_leilao_sem_lances(self):
        leilao = Leilao('Camisa', 20)
        avaliador = Avaliador()
        with self.assertRaises(Exception):
            avaliador.avaliarLeilao(leilao)

    def test_verifica_valor_minimo_naturais(self):
        with self.assertRaises(Exception):
            leilao = Leilao('Camisa', -100)
