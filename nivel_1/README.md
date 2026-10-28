# Sistema de vendas com descontos

Feito em python, ele calcula descontos nas compras e mostra um resumo de tudo no fim do dia.

## Como funciona?

- Informe o valor da compra feita e sua idade
- Se você tiver 65 anos ou mais, você ganha 20% de desconto.
- Compras com valor superior a R$ 100,00, após o desconto por idade, recebem mais 10% de desconto.
- O sistema mostra o valor final de cada compra.
- Ao digitar 0, o programa encerra e mostra um resumo diário.

## Alguns exemplos para comparação

| Preço | Idade | Valor final |
|---:|---:|---:|
| R$ 50,00 | 30 | R$ 50,00 |
| R$ 100,00 | 30 | R$ 100,00 |
| R$ 101,00 | 30 | R$ 90,90 |
| R$ 200,00 | 30 | R$ 180,00 |
| R$ 200,00 | 64 | R$ 180,00 |
| R$ 200,00 | 65 | R$ 144,00 |
| R$ 125,00 | 65 | R$ 100,00 |
| R$ 1000,00 | 80 | R$ 720,00 |

## Como executar

É necessário ter o Python instalado. Depois, basta abrir o terminal na pasta do arquivo e executar:

```bash
python pdv.py
```