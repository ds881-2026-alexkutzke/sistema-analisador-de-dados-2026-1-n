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

    def processar(self):
        self.converter_textos()
        self.ordenar_dados()
        total = sum(self._dados_internos)
        logging.info(f"Processamento concluído. Total: {total}")
        return total
