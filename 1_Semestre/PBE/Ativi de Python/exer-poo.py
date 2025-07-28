class ItemBiblioteca:
    def __init__(self, titulo, ano_publicacao, disponivel):
        if ano_publicacao <= 0:
            raise ValueError("O ano de publicação tem que ser maior que 0")
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.disponivel = disponivel

    def emprestar(self):
        if not self.disponivel:
            raise Exception("O item já está emprestado.")
        self.disponivel = False

    def devolver(self):
        if self.disponivel:
            raise Exception("O item já está disponível.")
        self.disponivel = True

    def obter_info(self):
        status = "Sim" if self.disponivel else "Não"
        return f"Título: {self.titulo}\nAno: {self.ano_publicacao}\nDisponível: {status}"


class ColecaoLivros(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, disponivel, colecao):
        super().__init__(titulo, ano_publicacao, disponivel)
        self.colecao = colecao

    def obter_info(self):
        return f"{super().obter_info()}\nColeção: {self.colecao}"


class Revista(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, disponivel, n_edicao):
        super().__init__(titulo, ano_publicacao, disponivel)
        self.n_edicao = n_edicao

    def atualizar_edicao(self, nova_edicao):
        if nova_edicao <= 0:
            raise ValueError("Número da edição inválido.")
        self.n_edicao = nova_edicao

    def restringir_emprestimo(self):
        return self.ano_publicacao > 2000

    def obter_info(self):
        return f"{super().obter_info()}\nEdição: {self.n_edicao}"


class Biblioteca:
    def __init__(self):
        self.itens = {}

    def adicionar_item(self, item: ItemBiblioteca):
        if item.titulo in self.itens:
            raise Exception("Item já existe.")
        self.itens[item.titulo] = item

    def remover_item(self, titulo):
        if titulo not in self.itens:
            raise Exception("Item não encontrado.")
        del self.itens[titulo]

    def listar_itens_disponiveis(self):
        return [titulo for titulo, item in self.itens.items() if item.disponivel]

    def contar_itens_emprestados(self):
        return len([item for item in self.itens.values() if not item.disponivel])


class RelatorioBiblioteca:
    def __init__(self, biblioteca: Biblioteca):
        self.biblioteca = biblioteca

    def gerar_relatorio_completo(self):
        relatorio = ""
        for item in self.biblioteca.itens.values():
            relatorio += item.obter_info() + "\n---\n"
        return relatorio

    def gerar_relatorio_disponibilidade(self):
        disponiveis = [item for item in self.biblioteca.itens.values() if item.disponivel]
        total = len(self.biblioteca.itens)
        return f"Itens disponíveis: {len(disponiveis)} de {total}"

    def gerar_relatorio_emprestimos(self):
        emprestados = self.biblioteca.contar_itens_emprestados()
        total = len(self.biblioteca.itens)
        percentual = (emprestados / total * 100) if total > 0 else 0
        return f"Itens emprestados: {emprestados} ({percentual:.1f}%)"


# TESTE
biblio = Biblioteca()
item1 = ItemBiblioteca("O Hobbit", 1937, True)
item2 = Revista("Superinteressante", 2023, True, 400)
item3 = ColecaoLivros("Harry Potter", 1997, False, "Saga HP")

biblio.adicionar_item(item1)
biblio.adicionar_item(item2)
biblio.adicionar_item(item3)

relatorio = RelatorioBiblioteca(biblio)
print(relatorio.gerar_relatorio_completo())
print(relatorio.gerar_relatorio_disponibilidade())
print(relatorio.gerar_relatorio_emprestimos())
