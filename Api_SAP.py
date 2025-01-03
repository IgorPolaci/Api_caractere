from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de números
base_numeros = ["5511998765432", "5511987654321", "5511976543210"]

@app.route('/validar-numero', methods=['POST'])
def validar_numero():
    dados = request.json
    numero = dados.get("numero_telefone")
    
    if numero in base_numeros:
        return jsonify({
            "status": "Encontrado",
            "mensagem": "Número identificado para atendimento diferenciado."
        })
    else:
        return jsonify({
            "status": "Nao_encontrado",
            "mensagem": "Número não identificado na base."
        })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  
    app.run(debug=True, host='0.0.0.0', port=port)
