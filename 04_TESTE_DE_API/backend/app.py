from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db_config = {
    "host": "localhost",
    "user": "seu_usuario",
    "password": "sua_senha",
    "database": "teste_de_banco_de_dados"
}

@app.route('/buscar', methods=['GET'])
def buscar_operadoras():
    termo = request.args.get('termo', '')

    conexao = mysql.connector.connect(**db_config)
    cursor = conexao.cursor(dictionary=True)

    query = """
        SELECT * FROM operadoras
        WHERE razao_social LIKE %s OR cnpj LIKE %s OR registro_ans LIKE %s
    """
    cursor.execute(query, (f"%{termo}%", f"%{termo}%", f"%{termo}%"))
    
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()

    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
