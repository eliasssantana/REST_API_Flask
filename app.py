from flask import Flask, jsonify,request
import json
app = Flask(__name__)

desenvolvedores = [{"ID": 0,"nome": "Elias", "habilidades":['Python', 'Flask']},{"ID": 1,"nome":"joãozinho","habilidades":['Python','Django']}]
# Devolve um desenvolvedor pelo ID, também deleta e altera um desenvolvedor
@app.route("/dev/<int:id>", methods= ["GET","PUT","DELETE"])
def desenvolvedor(id):
    try:
        if request.method == "GET":
            response = desenvolvedores[id]
            print(response)
        elif request.method == "PUT":
            dados = json.loads(request.data)
            desenvolvedores[id] = dados
            return jsonify(dados)
        elif request.method == "DELETE":
            desenvolvedores.pop(id)
            return jsonify({'status':'sucesso','mensagem':'registro excluído'})
    except IndexError:
        mensagem = f"Desenvolvedor de ID {id:2d} não encontrado"
        response = {'status':'erro','mensagem':mensagem}
    except Exception:
        mensagem = "Erro desconhecido. Por favor, procure o administrador da API."
        response = {'status':'erro','mensagem':mensagem}
    finally:
        return jsonify(response)
# Lista todos os desenvolvedores e permite registrar um novo
@app.route("/dev/", methods=["POST","GET"])
def lista_desenvolvedores():
    if request.method == "POST":
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['ID'] = posicao
        desenvolvedores.append(dados)
        return jsonify({'status':'sucesso','mensagem':'novo registro adicionado',"posição":posicao})

    elif request.method == "GET":
        return jsonify(desenvolvedores)
if __name__ == "__main__":
    app.run(debug=True)