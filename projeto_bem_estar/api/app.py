from flask import Flask, request, jsonify, render_template
import services

app = Flask(__name__)

# Rota raiz para o Render não retornar 404
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/analyze-checkin', methods=['POST'])
def analyze_checkin():
    data = request.get_json()
    required_fields = ['humor', 'foco', 'pausas', 'horas_trabalhadas']
    if not data or not all(field in data for field in required_fields):
        return jsonify({"error": "Dados incompletos. Campos necessários: humor, foco, pausas, horas_trabalhadas"}), 400

    humor = data.get('humor')
    foco = data.get('foco')
    pausas = data.get('pausas')
    horas_trabalhadas = data.get('horas_trabalhadas')

    indice_bem_estar = services.calcular_indice_bem_estar(humor, foco, pausas)
    risco_burnout = services.calcular_risco_burnout(horas_trabalhadas, pausas)
    feedback_ia = services.gerar_feedback_ia(indice_bem_estar, risco_burnout, humor)

    response = {
        "indice_bem_estar": indice_bem_estar,
        "risco_burnout": risco_burnout,
        "feedback_ia": feedback_ia,
        "dados_recebidos": data
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)