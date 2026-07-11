# -*- coding: utf-8 -*-
"""
Rose Cosméticos - site simples em Flask (Python)
=================================================
Como rodar:
    1) pip install flask
    2) python app.py
    3) abrir no navegador: http://localhost:5000

O que editar:
    - Nome da loja, WhatsApp e Instagram: logo abaixo, em CONFIG.
    - Produtos e preços: no arquivo products.py
    - Fotos dos produtos: pasta static/img/ (veja o nome exato de cada
      arquivo dentro de products.py, campo "imagem")
"""

from flask import Flask, render_template, abort
from products import PRODUTOS, CATEGORIAS

app = Flask(__name__)

# ------------------- CONFIGURAÇÕES DA LOJA -------------------
CONFIG = {
    "nome_loja": "Rose Cosméticos",
    "slogan": "Delicadeza em cada detalhe",
    "whatsapp": "5567996007435",  # troque pelo número real, só números, com código do país (55) e DDD
    "instagram": "rosecosmeticos",  # sem o @
}
# ---------------------------------------------------------------


def preco_formatado(produto):
    if produto["preco"] is None:
        return "Consulte"
    return f"R$ {produto['preco']:.2f}".replace(".", ",")


def link_whatsapp(produto):
    mensagem = f"Olá! Tenho interesse no produto: {produto['nome']}"
    mensagem = mensagem.replace(" ", "%20")
    return f"https://wa.me/{CONFIG['whatsapp']}?text={mensagem}"


@app.route("/")
def index():
    return render_template(
        "index.html",
        config=CONFIG,
        categorias=CATEGORIAS,
        produtos=PRODUTOS,
        preco_formatado=preco_formatado,
        link_whatsapp=link_whatsapp,
    )


@app.route("/produto/<int:produto_id>")
def produto(produto_id):
    item = next((p for p in PRODUTOS if p["id"] == produto_id), None)
    if item is None:
        abort(404)
    return render_template(
        "produto.html",
        config=CONFIG,
        produto=item,
        preco_formatado=preco_formatado,
        link_whatsapp=link_whatsapp,
    )


if __name__ == "__main__":
    app.run(debug=True)
