from unittest import TestCase
from prova01.q01 import Pais, NotEditable


class TesteQuestao01(TestCase):
    def test_A_objeto_Pais_recebe_nome_e_dimensão_no_construtor(self):
        from prova01.q01 import Pais
        
        pais = Pais("A", 2321, 23)
        self.assertEqual(pais.name, "A")
        self.assertEqual(pais.dimension, 23)

    def test_A_erro_ao_tentar_editar_o_código_do_pais(self):
        pais = Pais("Brasil", 2891829, 25898989)
        with self.assertRaises(NotEditable):
            pais.code = 232

    def test_C_verificar_se_dois_paises_sao_iguais(self):
        brasil = Pais("Brasil", 433233, 2019029102.039)
        eua = Pais("EUA", 9382938, 1298918.9823)

        self.assertEqual(eua, eua)
        self.assertNotEqual(brasil, eua)

    def test_D_adicionar_fronteira(self):
        uruguai = Pais("URUGUAI", 2123132, 5989898.3)
        brasil = Pais("BRASIL", 2132132, 34.2)
        brasil.add_fronteira(uruguai)
        brasil.add_fronteira(uruguai)
        self.assertTrue(brasil.e_limitrofe(uruguai))
        self.assertTrue(uruguai.e_limitrofe(brasil))

    def test_retorna_vizinhos_comuns(self):
        uruguai = Pais("URUGUAI", 2123132, 5989898.3)
        brasil = Pais("BRASIL", 2132132, 34.2)
        argenina = Pais("ARGENINA", 9382938, 1298918.9823)
        eua = Pais("EUA", 98298, 21322.2121)

        uruguai.add_fronteira(brasil, argenina)
        brasil.add_fronteira(argenina)

        brasil.vizinhos_comuns(argenina)

        self.assertEqual({brasil}, uruguai.vizinhos_comuns(argenina))
        self.assertEqual({argenina}, uruguai.vizinhos_comuns(brasil))
        self.assertEqual(set(), brasil.vizinhos_comuns(eua))

    def test_retorna_todos_os_paises(self):
        uruguai = Pais("URUGUAI", 2123132, 5989898.3)
        uruguai.clear()
        uruguai = Pais("URUGUAI", 2123132, 5989898.3)
        brasil = Pais("BRASIL", 2132132, 34.2)
        argenina = Pais("ARGENINA", 9382938, 1298918.9823)
        eua = Pais("EUA", 98298, 21322.2121)


        self.assertEqual(argenina, eua.todos_paises()[0])
        self.assertEqual(uruguai, eua.todos_paises()[-1])


    
