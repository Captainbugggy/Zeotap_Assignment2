from flask import Blueprint, request, jsonify, render_template
from app.services.model_factory import ModelFactory
main = Blueprint("main", __name__)

@main.route("/", methods=["GET"])
def home():
   return render_template("index.html")

@main.route("/process", methods=["POST"])
def process_request():
   data = request.form.get("user_prompt", "")
   if not data:
       return jsonify({"error": "User prompt is required"}), 400

   model_factory = ModelFactory()
   gemini_model = model_factory.get_model("gemini")
   response = gemini_model.generate_response(data)
   
   return jsonify({"response": response})