from flask import Flask, request, jsonify

from difference_summary.gp2_summary import GPT2Summary
from similarity_score.gpt2_cosine_similarity import GPT2CosineSimilarity

gp2_summary = GPT2Summary()
gpt2_cosine_similarity = GPT2CosineSimilarity()
app = Flask(__name__)


# Define the API endpoint for generating a GPT-2 summary
@app.route("/generate_summary", methods=["POST"])
def generate_summary():
    # Get the input text from the request
    data = request.json
    text1 = data["text1"]
    text2 = data["text2"]

    # Generate a summary of the input texts using the GPT-2 model
    summary = gp2_summary.generate_gp2_summary(text1, text2)

    # Return the summary as a JSON response
    response = {"summary": summary}
    return jsonify(response)


# Define the API endpoint for text comparison
@app.route("/cosine_similarity", methods=["POST"])
def cosine_similarity():
    # Get the input texts from the request
    data = request.json
    text1 = data["text1"]
    text2 = data["text2"]

    # Calculate the cosine similarity between the input texts using the GPT-2 model
    similarity = gpt2_cosine_similarity.get_cosine_similarity(text1, text2)

    # Return the similarity score as a JSON response
    response = {"similarity": similarity}
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
