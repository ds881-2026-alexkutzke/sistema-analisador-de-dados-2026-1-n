class AnalisadorDados:
    def __init__(self):
        self.dados = []

    def carregar_dados(self, dados_brutos):
        self.dados = dados_brutos

    def limpar_dados(self):
        # Bug intencional: remove números negativos em vez de apenas nulos
        self.dados = [d for d in self.dados if d and d > 0]

    def processar(self):
        self.limpar_dados()
        soma = sum(self.dados)
        return soma
