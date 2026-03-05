import logging

logging.basicConfig(level=logging.INFO)

class AnalisadorDados:
    def __init__(self, ignorar_erros=False):
        self._dados_internos = []
        self.ignorar_erros = ignorar_erros
        logging.info("Analisador inicializado.")

    def carregar_dados(self, array_dados):
        if not isinstance(array_dados, list):
            raise ValueError("Os dados devem ser uma lista")
        self._dados_internos = array_dados
        logging.info(f"{len(array_dados)} registros carregados.")

    def ordenar_dados(self):
        self._dados_internos.sort()

    def converter_textos(self):
        temp = []
        for d in self._dados_internos:
            try:
                temp.append(float(d))
            except (ValueError, TypeError):
                if not self.ignorar_erros:
                    raise
        self._dados_internos = temp

    def limpar_dados(self):
        # Bug intencional: remove números negativos em vez de apenas nulos
        self.dados = [d for d in self.dados if d and d > 0]

    def processar(self):
        self.limpar_dados()
        soma = sum(self.dados)
        return soma

    def exibir_relatorio(self):
        resultado = self.processar()
        print(f"--- Relatório de Processamento -
        print(f"Total calculado: {resultado}")
