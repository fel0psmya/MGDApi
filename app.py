from flask import Flask, jsonify
from main import get_all_games, get_game_by_id

app = Flask(__name__)

# Rota para obter todos os jogos
@app.route('/games', methods=['GET'])
def get_games():
    games = get_all_games()  # Função definida no main.py
    return jsonify(games), 200  # Retorna os jogos como JSON com status 200 OK

# Rota para obter um jogo específico por ID
@app.route('/games/<int:game_id>', methods=['GET'])
def get_game(game_id):
    game = get_game_by_id(game_id)  # Função definida no main.py
    if game:
        return jsonify(game), 200
    else:
        return jsonify({"error": "Jogo não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)