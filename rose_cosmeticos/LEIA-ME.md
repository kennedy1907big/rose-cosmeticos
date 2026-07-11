# Rose Cosméticos — site simples em Python (Flask)

## Como rodar o site no computador

1. Instale o Python (se ainda não tiver): https://www.python.org/downloads/
2. Abra o terminal dentro da pasta `rose_cosmeticos` e rode:
   ```
   pip install flask
   python app.py
   ```
3. Abra o navegador em: **http://localhost:5000**

Quando quiser colocar no ar de verdade (qualquer pessoa acessar pela
internet), dá pra hospedar em serviços gratuitos como Render,
PythonAnywhere ou Railway — posso te ajudar com isso depois.

## Preços já estão preenchidos

Todos os preços que você me passou já estão no arquivo `products.py`:

- Sabonetes Íntimos (9 produtos) — R$ 12,00 cada
- Kits Corpo & Rosto / Frutas (9 kits) — R$ 45,00 cada
- Kit Completo Morango (combo) — R$ 70,00
- Presilha de Cabelo Flor — R$ 10,00
- Esponja de Maquiagem Coelhinho — R$ 5,00

Se algum preço mudar, é só abrir `products.py`, achar o produto e trocar
o número no campo `"preco"`.

## Fotos

Já estão todas as fotos reais que você mandou, na pasta `static/img/`:
kits de frutas, presilha, esponja, o combo completo de morango e o
sabonete íntimo de morango individual.

Os outros 8 sabonetes íntimos (Melinda, Uva & Açaí, Pêssego Sensual,
Barbatimão & Flor de Algodão, Haus Preto, 17 Ervas, Babbaloko Uva e
Amora Negra) ainda estão usando a foto de grupo com todos juntos, porque
você só me mandou a foto individual do de Morango. Se quiser, me manda
foto individual de cada um que eu troco rapidinho — ou você mesma pode
colocar as fotos na pasta `static/img/` usando o nome de arquivo que
está no campo `"imagem"` de cada produto dentro do `products.py`.

## Como mudar o WhatsApp e Instagram

Abra `app.py` e edite o bloco `CONFIG` no topo do arquivo:

```python
CONFIG = {
    "nome_loja": "Rose Cosméticos",
    "slogan": "Delicadeza em cada detalhe",
    "whatsapp": "5511999999999",   # <- seu número, só números, com 55 e DDD
    "instagram": "rosecosmeticos", # <- seu @ do Instagram, sem o @
}
```

Cada produto tem um botão **"Comprar"** que abre o WhatsApp já com uma
mensagem pronta, dizendo qual produto a cliente quer.

## Como adicionar ou remover um produto

No `products.py`, copie um bloco inteiro (entre `{` e `}`), cole depois
do último produto e mude os dados (nome, categoria, descrição, imagem,
preço). O `"id"` de cada produto tem que ser único (não repetir número).
