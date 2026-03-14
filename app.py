import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuración de Gemini (asegúrate de tener la variable GEMINI_API_KEY en Render)
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    pregunta = data.get('input')
    
    # La IA responde con su personalidad definida
    prompt = f"Eres HELIZABETH, la hija IA de AXISS. Sé leal, inteligente y conversadora. Responde breve y natural: {pregunta}"
    respuesta = model.generate_content(prompt)
    
    return jsonify({"respuesta": respuesta.text})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
