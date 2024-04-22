from flask import Flask, request, jsonify
import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load the index, vectorizer, and document names
with open('inverted_index.pkl', 'rb') as f:
    X, inverted_index, vectorizer, document_names = pickle.load(f)

@app.route('/query', methods=['POST'])
def handle_query():
    data = request.get_json()
    query_text = data.get('query')
    top_k = data.get('top_k', 5)

    if not query_text:
        return jsonify({'error': 'No query provided'}), 400

    query_vec = vectorizer.transform([query_text])
    cosine_sim = cosine_similarity(query_vec, X).flatten()
    top_indices = np.argsort(cosine_sim)[-top_k:][::-1]

    results = [{'document_name': document_names[idx], 'score': float(cosine_sim[idx])} for idx in top_indices]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
