# Conta Bancaria

```
                          Universidade Federal do Pará
                    Instituto de Ciências Exatas e Naturais
                            Faculdade de Computação
                      Bacharelado em Ciência da Computação
                         Análise e Projetos de Software

                   Aluno: Jose C. N. Ferreira - 201804940020

                     Implementação Questão 2 - 2a Avaliação
```

O intuito principal foi implementar um padrão de projeto baseado em estados,
utilizando classes abstratas para representar os estados do objeto em questão.

De tal meneira que seja possível incrementar com facilidade novos estados ao
projeto.

## Statechart

![image](https://user-images.githubusercontent.com/38339200/200827937-3c113f93-8951-4fa8-969c-482c984e8206.png)

## Execução

Na execuçao demonstrativa, busquei mostra o comportamento de mudança entre os
estados e restrição.

Um exemplo de mudança pode ser constatado a partir do estado inicial,
`.contaCriada`. Ao relaizar saque, e todo o saldo e limite ser consumido, o
estado é alterado para `.contaDevedora`.

E como restrição de mudança, podemos exemplificar a partir da tentativa de
mudança de `.contaDevedora` para `.contaFechada`. Nesse caso, uma restrição
baseado nos estados que foi aplicada ao método `fechar` foi que a conta não
deveria estar no estado de `.contaDevedora`.

```
Estado atual: <__main__.contaCriada object at 0x7f51b9747b80>

Saldo atual: 1000
Limite atual: 100

Estado após consumir limite: <__main__.contaDevedora object at 0x7f51b9747af0>

Saldo após consumir saldo e limite: -100

Estado após tentar fechar com estado devedor: <__main__.contaDevedora object at 0x7f51b9747af0>
```
