from flask import Flask, request, jsonify
import unidecode  # Biblioteca para remover acentos

app = Flask(__name__)

@app.route('/limpa_caracteres', methods=['POST'])
def limpa_caracteres():
    dados = request.json
    cidade = dados.get("cidade")
    estado = dados.get("estado")

    if not cidade or not estado:
        return jsonify({
            "status": "Erro",
            "mensagem": "Nenhum texto foi enviado."
        })

    # Remove acentos e transforma em minúsculas
    Cidade = unidecode.unidecode(Cidade).lower()
    Estado = unidecode.unidecode(Estado).lower()

    return jsonify({
        "status": "Sucesso",
        "CIdade_tratado": Cidade
        "Estado_tratado": Estado
    })

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 11000))
    app.run(debug=True, host='0.0.0.0', port=port)
