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
            "mensagem": "Os campos 'cidade' e 'estado' são obrigatórios."
        })

    # Remove acentos, transforma em minúsculas e substitui espaços por traços
    cidade_tratada = unidecode.unidecode(cidade).lower().replace(" ", "-")
    estado_tratado = unidecode.unidecode(estado).lower()

    return jsonify({
        "status": "Sucesso",
        "cidade_tratada": cidade_tratada,
        "estado_tratado": estado_tratado
    })

@app.route('/', methods=['GET'])
def ping():
    return jsonify({"status": "ok", "mensagem": "API ativa"}), 200

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 11000))
    app.run(debug=True, host='0.0.0.0', port=port)
