from flask import Flask, jsonify,request
import json
app = Flask(__name__)

desenvolvedores = [{"nome": "Elias", "habilidades":['Python', 'Flask']},{"nome":"joãozinho","habilidades":['Python','Django']}]
@app.route("/dev/<int:id>", methods= ["GET","PUT","DELETE"])
def desenvolvedor(id):
    if request.method == "GET":
        desenvolvedor = desenvolvedores[id]
        print(desenvolvedor)
        return jsonify(desenvolvedor)
    elif request.method == "PUT":
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == "DELETE":
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso','mensagem':'registro excluído'})
if __name__ == "__main__":
    app.run(debug=True)