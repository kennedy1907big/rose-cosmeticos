# -*- coding: utf-8 -*-
"""
CATALOGO DE PRODUTOS - Rose Cosmeticos
========================================
Para EDITAR PRECOS: procure o campo "preco" de cada produto abaixo e troque
o valor (use ponto para os centavos, ex: 24.90). Se o preco ainda nao foi
definido, deixe como None e o site vai mostrar "Consulte".

Para EDITAR/ADICIONAR PRODUTOS: copie um bloco inteiro (entre chaves { }),
cole logo abaixo e mude os dados.

Para as FOTOS: coloque o arquivo de imagem dentro da pasta static/img/
com o mesmo nome que esta no campo "imagem" de cada produto. Se a imagem
nao existir, o site mostra automaticamente um espaco reservado (placeholder).
"""

CATEGORIAS = [
    "Sabonetes Íntimos",
    "Kits Corpo & Rosto",
    "Combos",
    "Acessórios",
]

PRODUTOS = [
    # ---------------- SABONETES ÍNTIMOS (R$ 12,00 cada) ----------------
    {"id": 1, "nome": "Sabonete Íntimo Melinda", "categoria": "Sabonetes Íntimos",
     "descricao": "Spray íntimo perfumado, experiência única. 200ml / 6.7 fl.oz.",
     "imagem": "sabonetes-linha.jpg", "preco": 12.00},
    {"id": 2, "nome": "Sabonete Íntimo Uva & Açaí", "categoria": "Sabonetes Íntimos",
     "descricao": "Extratos de Barbatimão, Aroeira e Malva. pH equilibrado. 200ml.",
     "imagem": "sabonetes-linha.jpg", "preco": 12.00},
    {"id": 3, "nome": "Sabonete Íntimo Pêssego Sensual", "categoria": "Sabonetes Íntimos",
     "descricao": "Extratos de Malva. pH equilibrado. 200ml.",
     "imagem": "sabonetes-linha.jpg", "preco": 12.00},
    {"id": 4, "nome": "Sabonete Íntimo Morango", "categoria": "Sabonetes Íntimos",
     "descricao": "Extratos de Barbatimão, Aroeira e Malva. pH equilibrado. 200ml.",
     "imagem": "sabonete-morango.jpg", "preco": 12.00},
    {"id": 5, "nome": "Sabonete Íntimo Barbatimão & Flor de Algodão", "categoria": "Sabonetes Íntimos",
     "descricao": "Extratos de Barbatimão, Aroeira e Malva. pH equilibrado. 200ml.",
     "imagem": "sabonetes-linha.jpg", "preco": 12.00},
    {"id": 6, "nome": "Sabonete Íntimo Haus Preto", "categoria": "Sabonetes Íntimos",
     "descricao": "Extratos de Barbatimão, Aroeira e Malva. 200ml.",
     "imagem": "sabonetes-linha.jpg", "preco": 12.00},
    {"id": 7, "nome": "Sabonete Íntimo 17 Ervas", "categoria": "Sabonetes Íntimos",
     "descricao": "Extrato de 17 Ervas, com camomila. Limpeza diária e delicada. 200ml.",
     "imagem": "sabonetes-linha.jpg", "preco": 12.00},
    {"id": 8, "nome": "Sabonete Íntimo Babbaloko Uva", "categoria": "Sabonetes Íntimos",
     "descricao": "Contém ácido lático. 200ml.",
     "imagem": "sabonetes-linha.jpg", "preco": 12.00},
    {"id": 9, "nome": "Sabonete Íntimo Amora Negra", "categoria": "Sabonetes Íntimos",
     "descricao": "Extrato de Amora. pH equilibrado. 200ml.",
     "imagem": "sabonetes-linha.jpg", "preco": 12.00},

    # ---------------- KITS CORPO & ROSTO / FRUTAS (R$ 45,00 cada) ----------------
    {"id": 10, "nome": "Kit Maracujá", "categoria": "Kits Corpo & Rosto",
     "descricao": "Sabonete líquido + Hidratante (200ml cada) + Esfoliante corporal (300g). Aroma de frutas, para corpo e rosto.",
     "imagem": "kit-maracuja.jpg", "preco": 45.00},
    {"id": 11, "nome": "Kit Morango", "categoria": "Kits Corpo & Rosto",
     "descricao": "Sabonete líquido + Hidratante (200ml cada) + Esfoliante corporal (300g). Deixa a pele macia e perfumada.",
     "imagem": "kit-morango.jpg", "preco": 45.00},
    {"id": 12, "nome": "Kit Pitaya (Dragon Fruit)", "categoria": "Kits Corpo & Rosto",
     "descricao": "Sabonete líquido + Hidratante (200ml cada) + Esfoliante corporal (300g). Antirressecamento.",
     "imagem": "kit-pitaya.jpg", "preco": 45.00},
    {"id": 13, "nome": "Kit Ameixa Negra (Black Plum)", "categoria": "Kits Corpo & Rosto",
     "descricao": "Sabonete líquido + Hidratante (200ml cada) + Esfoliante corporal (300g). Uso diário, todos os tipos de pele.",
     "imagem": "kit-ameixa-negra.jpg", "preco": 45.00},
    {"id": 14, "nome": "Kit Abacaxi (Pineapple)", "categoria": "Kits Corpo & Rosto",
     "descricao": "Sabonete líquido + Hidratante (200ml cada) + Esfoliante corporal (300g). Antirressecamento.",
     "imagem": "kit-abacaxi.jpg", "preco": 45.00},
    {"id": 15, "nome": "Kit Tangerina", "categoria": "Kits Corpo & Rosto",
     "descricao": "Sabonete líquido + Hidratante (200ml cada) + Esfoliante corporal (300g). Antirressecamento.",
     "imagem": "kit-tangerina.jpg", "preco": 45.00},
    {"id": 16, "nome": "Kit Pêssego Doce (Sweet Peach)", "categoria": "Kits Corpo & Rosto",
     "descricao": "Sabonete líquido + Hidratante (200ml cada) + Esfoliante corporal (300g). Antirressecamento.",
     "imagem": "kit-pessego-doce.jpg", "preco": 45.00},
    {"id": 17, "nome": "Kit Maçã Verde (Green Apple)", "categoria": "Kits Corpo & Rosto",
     "descricao": "Sabonete líquido + Hidratante (200ml cada) + Esfoliante corporal (300g). Antirressecamento.",
     "imagem": "kit-maca-verde.jpg", "preco": 45.00},
    {"id": 18, "nome": "Kit Tutti Frutti", "categoria": "Kits Corpo & Rosto",
     "descricao": "Sabonete líquido + Hidratante (200ml cada) + Esfoliante corporal (300g). Antirressecamento.",
     "imagem": "kit-tutti-frutti.jpg", "preco": 45.00},

    # ---------------- COMBOS ----------------
    {"id": 21, "nome": "Kit Completo Morango", "categoria": "Combos",
     "descricao": "Sabonete Íntimo Morango + Sabonete Líquido + Hidratante + Esfoliante Corporal (aroma de morango) + Presilha de Flor + Esponja de Maquiagem Coelhinho.",
     "imagem": "kit-completo-morango.jpg", "preco": 70.00},

    # ---------------- ACESSÓRIOS ----------------
    {"id": 19, "nome": "Presilha de Cabelo Flor", "categoria": "Acessórios",
     "descricao": "Presilha em formato de flor tropical, disponível em várias cores.",
     "imagem": "presilha-flor.jpg", "preco": 10.00},
    {"id": 20, "nome": "Esponja de Maquiagem Coelhinho", "categoria": "Acessórios",
     "descricao": "Esponja para maquiagem em formato de coelhinho, material de alta qualidade.",
     "imagem": "esponja-coelhinho.jpg", "preco": 5.00},
]
