class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1

class AVLTree:
    def inserir(self, raiz, valor):
        # 1. Inserção normal de BST
        if not raiz:
            return No(valor)
        elif valor < raiz.valor:
            raiz.esquerda = self.inserir(raiz.esquerda, valor)
        else:
            raiz.direita = self.inserir(raiz.direita, valor)

        # 2. Atualiza a altura do nó ancestral
        raiz.altura = 1 + max(self.get_altura(raiz.esquerda),
                              self.get_altura(raiz.direita))

        # 3. Obtém o fator de balanceamento
        balanceamento = self.get_balanceamento(raiz)

        # 4. Se o nó estiver desbalanceado, tenta os 4 casos

        # Caso 1 - Rotação Simples à Direita (Left-Left)
        if balanceamento > 1 and valor < raiz.esquerda.valor:
            print(f"Rotação à Direita no nó {raiz.valor}")
            return self.rotacao_direita(raiz)

        # Caso 2 - Rotação Simples à Esquerda (Right-Right)
        if balanceamento < -1 and valor > raiz.direita.valor:
            print(f"Rotação à Esquerda no nó {raiz.valor}")
            return self.rotacao_esquerda(raiz)

        # Caso 3 - Rotação Dupla à Direita (Left-Right)
        if balanceamento > 1 and valor > raiz.esquerda.valor:
            print(f"Rotação Dupla (Esq-Dir) no nó {raiz.valor}")
            raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            return self.rotacao_direita(raiz)

        # Caso 4 - Rotação Dupla à Esquerda (Right-Left)
        if balanceamento < -1 and valor < raiz.direita.valor:
            print(f"Rotação Dupla (Dir-Esq) no nó {raiz.valor}")
            raiz.direita = self.rotacao_direita(raiz.direita)
            return self.rotacao_esquerda(raiz)

        return raiz

    def remover(self, raiz, valor):
        # 1. Remoção padrão de BST
        if not raiz:
            return raiz

        if valor < raiz.valor:
            raiz.esquerda = self.remover(raiz.esquerda, valor)
        elif valor > raiz.valor:
            raiz.direita = self.remover(raiz.direita, valor)
        else:
            # Nó com apenas um filho ou nenhum
            if raiz.esquerda is None:
                return raiz.direita
            elif raiz.direita is None:
                return raiz.esquerda

            # Nó com dois filhos: pega o menor da subárvore direita
            temp = self.get_min_value_node(raiz.direita)
            raiz.valor = temp.valor
            raiz.direita = self.remover(raiz.direita, temp.valor)

        if not raiz:
            return raiz

        # 2. Atualiza a altura
        raiz.altura = 1 + max(self.get_altura(raiz.esquerda),
                              self.get_altura(raiz.direita))

        # 3. Balanceia o nó
        balanceamento = self.get_balanceamento(raiz)

        # Casos de Rotação após remoção
        # Esquerda Pesada
        if balanceamento > 1 and self.get_balanceamento(raiz.esquerda) >= 0:
            return self.rotacao_direita(raiz)
        if balanceamento > 1 and self.get_balanceamento(raiz.esquerda) < 0:
            raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            return self.rotacao_direita(raiz)

        # Direita Pesada
        if balanceamento < -1 and self.get_balanceamento(raiz.direita) <= 0:
            return self.rotacao_esquerda(raiz)
        if balanceamento < -1 and self.get_balanceamento(raiz.direita) > 0:
            raiz.direita = self.rotacao_direita(raiz.direita)
            return self.rotacao_esquerda(raiz)

        return raiz

    # Operações Auxiliares
    def get_altura(self, no):
        if not no:
            return 0
        return no.altura

    def get_balanceamento(self, no):
        if not no:
            return 0
        return self.get_altura(no.esquerda) - self.get_altura(no.direita)

    def get_min_value_node(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    # Rotações
    def rotacao_esquerda(self, z):
        y = z.direita
        T2 = y.esquerda
        y.esquerda = z
        z.direita = T2
        z.altura = 1 + max(self.get_altura(z.esquerda), self.get_altura(z.direita))
        y.altura = 1 + max(self.get_altura(y.esquerda), self.get_altura(y.direita))
        return y

    def rotacao_direita(self, z):
        y = z.esquerda
        T3 = y.direita
        y.direita = z
        z.esquerda = T3
        z.altura = 1 + max(self.get_altura(z.esquerda), self.get_altura(z.direita))
        y.altura = 1 + max(self.get_altura(y.esquerda), self.get_altura(y.direita))
        return y

    def buscar(self, raiz, valor):
        if raiz is None or raiz.valor == valor:
            return raiz
        if valor < raiz.valor:
            return self.buscar(raiz.esquerda, valor)
        return self.buscar(raiz.direita, valor)

    # Visualização para o terminal
    def print_tree(self, currPtr, indent, last):
        if currPtr:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "   "
            else:
                sys.stdout.write("L----")
                indent += "|  "
            print(currPtr.valor)
            self.print_tree(currPtr.esquerda, indent, False)
            self.print_tree(currPtr.direita, indent, True)

# --- Bloco de Execução Principal (Para testar e gravar o vídeo) ---
import sys

if __name__ == "__main__":
    arvore = AVLTree()
    raiz = None

    print("\n--- INSERÇÃO (Forçando Rotações) ---")
    numeros = [10, 20, 30, 40, 50, 25]
    
    for num in numeros:
        print(f"\nInserindo: {num}")
        raiz = arvore.inserir(raiz, num)
        arvore.print_tree(raiz, "", True)

    print("\n--- BUSCA ---")
    valor_busca = 30
    resultado = arvore.buscar(raiz, valor_busca)
    if resultado:
        print(f"Valor {valor_busca} encontrado na árvore.")
    else:
        print(f"Valor {valor_busca} não encontrado.")

    print("\n--- REMOÇÃO ---")
    print("Removendo 40 (Nó folha/meio que causa rebalanceamento)")
    raiz = arvore.remover(raiz, 40)
    arvore.print_tree(raiz, "", True)