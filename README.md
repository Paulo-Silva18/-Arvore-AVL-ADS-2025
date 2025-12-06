# Implementação de Árvore AVL em Python

Este projeto consiste na implementação completa de uma Árvore AVL (Adelson-Velsky e Landis) utilizando a linguagem Python, sem o uso de bibliotecas externas para estruturas de dados. O objetivo é demonstrar o funcionamento do balanceamento automático em árvores binárias de busca.

## 📋 Funcionalidades

O algoritmo suporta as seguintes operações:
1.  **Inserção:** Adiciona nós mantendo a propriedade de busca binária e verifica o balanceamento.
2.  **Remoção:** Remove nós (folhas, com 1 filho ou 2 filhos) e rebalanceia a árvore se necessário.
3.  **Busca:** Localiza um valor na estrutura.
4.  **Balanceamento Automático:** Utiliza cálculo de altura e fator de balanceamento para aplicar rotações.

## 🔄 Tipos de Rotações Implementadas

Para manter o fator de balanceamento entre -1 e 1, o código aplica:
* **Rotação Simples à Direita (LL):** Quando o desbalanceamento ocorre na subárvore esquerda da esquerda.
* **Rotação Simples à Esquerda (RR):** Quando o desbalanceamento ocorre na subárvore direita da direita.
* **Rotação Dupla (LR e RL):** Combinações de rotações para casos onde o "joelho" da árvore está desbalanceado (zigue-zague).

## 🚀 Como Executar

### Pré-requisitos
* Python 3.x instalado.

### Passo a passo
1.  Clone este repositório:
    ```bash
    git clone [https://github.com/SEU_USUARIO/NOME_DO_REPO.git](https://github.com/SEU_USUARIO/NOME_DO_REPO.git)
    ```
2.  Navegue até a pasta:
    ```bash
    cd NOME_DO_REPO
    ```
3.  Execute o arquivo principal:
    ```bash
    python main.py
    ```

## 🎥 Demonstração

O funcionamento da árvore, incluindo as rotações ocorrendo em tempo real, pode ser visualizado no vídeo abaixo:
[LINK DO SEU VÍDEO NO YOUTUBE AQUI]
