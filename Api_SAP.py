from flask import Flask, request, jsonify

app = Flask(__numero__)

# Base de números
base_numeros = ["5511998765432", "5511987654321", "5511976543210"]

@app.route('/validar-cidade', methods=['POST'])
def validar_cidade():
    dados = request.json
    numero = dados.get("numero")
    
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

if __numero__ == '__main__':
    port = int(os.environ.get("PORT", 11000))  
    app.run(debug=True, host='0.0.0.0', port=port)
