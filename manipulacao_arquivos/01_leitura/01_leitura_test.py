import unittest # Aqui chamamos a biblioteca padrão do python com seu módulo de testes
import os # esse módulo 'os" que importamos é referente manipulação de arquivos
from leitura import ler_arquivo # aqui importamos a função ler_arquivo do nosso script leitura.py =D

class TestLeituraArquivo(unittest.TestCase): # Aqui delcaramos a classe de testes que carrega o Testcase. O que significa? cada método que for escrito com test_ na frente será tratado automaticamente como um teste unitário pelo TestCase

    def setUp(self): # esse é um método de preparo que eu não conhecia, mas parece que em testes que precisa manipular arquivos é uma boa prática usá-lo
        self.arquivo_teste = "arquivo_test.txt" # Aqui definimos o nome do nosso arquivo de testes e usamos o self pra instanciá-lo e poder usar em outros métodos.
        with open(self.arquivo_teste, "w") as f: # Abre o arquivo en modo de escrita "w" 
            f.write("Conteúdo de teste") # escreve a string "conteúdo de teste" dentro do arquivo. 

    def tearDown(self): # esse carinha é chamado a cada teste para limpar o ambientem (deletar os arquivos criados nos testes) É importante, pq se não fosse ele, a cada vez q rodarmos esse teste unitário, vai criar um novo arquivo e acumular dentro da pasta
        if os.path.exists(self.arquivo_teste): # Verificação se o arquivo de fato existe antes de tentar removê-lo.
            os.remove(self.arquivo_teste) # Aqui ele remove esse arquivo de teste gerado deixando nossa pasta limpa \o

    def test_leitura_sucesso(self): # teste para verificar o funcionamento do código de leitura.
        conteudo = ler_arquivo(self.arquivo_teste) # chama a função ler_arquivo com o arquivo criado pelo setUp
        self.assertEqual(conteudo, "Conteúdo de teste") # faz a comparação pelo assert e retorna o valor esperado. Caso for diferente retorna F

    def test_arquivo_inexistente(self): # teste para caso de arquivo que não existe!
        conteudo = ler_arquivo("não_existe.txt") # Chama o ler_arquivo com um nome que não existe !
        self.assertEqual(conteudo, "Erro: Arquivo inexistente!") # Assert verifica aqui se a função retornou a string de erro. 

if __name__ == "__main__": # O bloco que possibilita a gente rodar o teste diretamente no terminal
    unittest.main() # executa o unittest chamando um por um até finalizar. 
