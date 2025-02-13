from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de cursos e links
base_cursos = {
    "Análise e Desenvolvimento de Sistemas": "https://chat.exemplo.com/ads",
    "Engenharia de Software": "https://chat.exemplo.com/eng-software",
    "Ciência da Computação": "https://chat.exemplo.com/ciencia-computacao"
}

@app.route('/obter-link', methods=['POST'])
def obter_link():
    dados = request.json
    curso = dados.get("curso")
    
    if curso in base_cursos:
        return jsonify({
            "status": "Encontrado",
            "mensagem": "Curso identificado.",
            "link": base_cursos[curso]
        })
    else:
        return jsonify({
            "status": "Nao_encontrado",
            "mensagem": "Curso não identificado na base."
        })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 11000))  
    app.run(debug=True, host='0.0.0.0', port=port)
