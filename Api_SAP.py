from flask import Flask, request, jsonify
from rapidfuzz import process

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
    curso_input = dados.get("curso")
    
if not curso_input:
        return jsonify({
            "status": "Erro",
            "mensagem": "Nenhum curso foi enviado."
        })
    
    melhor_curso, score, _ = process.extractOne(curso_input, base_cursos.keys())
    
    if score > 80:  # Define um limite para considerar uma correspondência válida
        return jsonify({
            "status": "Encontrado",
            "mensagem": "Curso identificado.",
            "curso": melhor_curso,
            "link": base_cursos[melhor_curso]
        })
    else:
        return jsonify({
            "status": "Nao_encontrado",
            "mensagem": "Curso não identificado na base."
        })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 11000))  
    app.run(debug=True, host='0.0.0.0', port=port)
