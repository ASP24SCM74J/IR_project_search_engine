import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def main():
    # Step 1: Load the Inverted Index
    with open('inverted_index.pkl', 'rb') as f:
        inverted_index = pickle.load(f)

    # Step 2: Inspect the Inverted Index
    print("Inverted Index:")
    for term, postings in inverted_index.items():
        print(f"Term: {term}")
        for doc_id, tfidf_score in postings:
            print(f"  Document ID: {doc_id}, TF-IDF Score: {tfidf_score}")

    # Step 3: Test Cosine Similarity
    # Generate sample query vectors and document vectors (replace with actual data if available)
    # Example query vector
    query_vector = np.random.rand(1, len(inverted_index))

    # Example document vectors
    document_vectors = np.random.rand(5, len(inverted_index))

    # Calculate cosine similarity scores
    cosine_similarities = cosine_similarity(query_vector, document_vectors)

    # Print the cosine similarity scores
    print("\nCosine Similarity Scores:")
    for i, similarity_score in enumerate(cosine_similarities[0]):
        print(f"Document {i+1}: {similarity_score}")

if __name__ == "__main__":
    main()
