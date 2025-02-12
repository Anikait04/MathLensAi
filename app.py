from flask import Flask, request, jsonify
from llm_response import get_ai_response
from extraction import save_user_image
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/chat", methods=["POST"])
def chat():
    """API endpoint to get chat response from the model."""
    data = request.form
    messages = data.get("messages", "[]")
    if not messages:
        return jsonify({"error": "Messages list is required"}), 400
    
    image = request.files.get("image")
    if not image:
        return jsonify({"error": "Image file is required"}), 400
    
    try:
        image_path = save_user_image(image)
        response = get_ai_response(image_path)
        return jsonify({"response": response})
    except Exception as e:a
        return jsonify({"error": str(e)}), 500
 
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=5000)