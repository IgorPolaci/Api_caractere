from flask import Flask, request, jsonify
import unidecode  # Biblioteca para remover acentos

app = Flask(__name__)

@app.route('/limpa_caracteres', methods=['POST'])
def limpa_caracteres():
    dados = request.json
    texto = dados.get("texto")

    if not texto:
        return jsonify({
            "status": "Erro",
            "mensagem": "Nenhum texto foi enviado."
        })

    # Remove acentos e transforma em minúsculas
    texto_tratado = unidecode.unidecode(texto).lower()

    return jsonify({
        "status": "Sucesso",
        "texto_tratado": texto_tratado
    })

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 11000))
    app.run(debug=True, host='0.0.0.0', port=port)
