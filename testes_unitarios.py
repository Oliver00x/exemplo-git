import unittest
from exercicios import calcula_media, mensagem_saudacao, calcula_situacao


class TesteCalculaMedia(unittest.TestCase):

    def test_calcula_media_float(self):
        media = calcula_media([1, 2, 3])
        self.assertIsInstance(media, float,
                              f"[calcula_media devia retornar float, mas retornou {type(media)}")

    def test_calcula_media_unico_valor(self):
        notas = [1]
        media = calcula_media(notas)
        self.assertEqual(
            1, media, f"para as notas {notas}, a media calculada devia ser 1, mas retornou {media}")

    def test_calcula_media_nota_maxima(self):
        notas = [10, 10, 10]
        media = calcula_media(notas)
        self.assertEqual(
            10, media, f"para as notas {notas}, a media calculada devia ser 10, mas retornou {media}")

    def test_calcula_media_notas_variadas(self):
        notas = [3, 7, ]
        media = calcula_media(notas)
        self.assertEqual(
            5, media, f"para as notas {notas}, a media calculada devia ser 10, mas retornou {media}")

    def test_calcula_media_vazio(self):
        media = calcula_media([])
        self.assertEqual(
            0, media, f"para a lista vazia, a media calculada devia ser 10, mas retornou {media}")

    def test_calcula_media_none(self):
        media = calcula_media(None)
        self.assertEqual(
            0, media, f"para a lista vazia, a media calculada devia ser 10, mas retornou {media}")


class TesteSaudacao(unittest.TestCase):
    def test_matutino(self):
        msg = mensagem_saudacao("M")
        esperado = "Bom dia!"
        self.assertEqual(
            msg, esperado, f"para o periodo [M], a saudação deveria ser {esperado}, mas retornou {msg}")

    def test_vespertino(self):
        msg = mensagem_saudacao("V")
        esperado = "Boa tarde!"
        self.assertEqual(
            msg, esperado, f"para o periodo [V], a saudação deveria ser {esperado}, mas retornou {msg}")

    def test_noturno(self):
        msg = mensagem_saudacao("N")
        esperado = "Boa noite!"
        self.assertEqual(
            msg, esperado, f"para o periodo [V], a saudação deveria ser {esperado}, mas retornou {msg}")

    def test_periodo_inesperado(self):
        msg = mensagem_saudacao("X")
        esperado = "Olá!"
        self.assertEqual(
            msg, esperado, f"para um periodo inesperado, a saudação deveria ser {esperado}, mas retornou {msg}")


class TesteSituacao(unittest.TestCase):
    def test_aprovado(self):
        msg = calcula_situacao(7)
        esperado = "Aprovado"
        self.assertEqual(
            msg, esperado, f"para a media 7, a situação deveria ser {esperado}, mas retornou {msg}")

    def test_reprovado(self):
        msg = calcula_situacao(6)
        esperado = "Reprovado"
        self.assertEqual(
            msg, esperado, f"para a media 6, a situação deveria ser {esperado}, mas retornou {msg}")

    def test_aprovado_distincao(self):
        msg = calcula_situacao(10)
        esperado = "Aprovado com distinção"
        self.assertEqual(
            msg, esperado, f"para a media 10, a situação deveria ser {esperado}, mas retornou {msg}")


unittest.main()
