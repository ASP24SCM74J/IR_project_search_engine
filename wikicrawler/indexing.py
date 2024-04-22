import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download('stopwords')

def load_documents(directory):
    documents = []
    document_names = []  # Store the names of the documents
    english_stopwords = set(stopwords.words('english'))
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8-sig') as f:
                text = f.read()
                # Remove special characters and convert to lowercase
                text = re.sub(r'[^a-zA-Z\s]', '', text)
                # Tokenize the text
                tokens = word_tokenize(text)
                # Remove English stopwords
                filtered_tokens = [token.lower() for token in tokens if token.lower() not in english_stopwords]
                # Join the filtered tokens back into a string
                filtered_text = ' '.join(filtered_tokens)
                documents.append(filtered_text)
                document_names.append(filename)  # Append the document name
    return documents, document_names

def build_index(documents, document_names):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(documents)
    inverted_index = {}
    terms = vectorizer.get_feature_names_out()
    for i, doc in enumerate(documents):
        for j, term in enumerate(terms):
            tfidf_score = X[i, j]
            if term not in inverted_index:
                inverted_index[term] = []
            if tfidf_score > 0:  # Only include non-zero scores
                inverted_index[term].append((document_names[i], tfidf_score))
    return X, inverted_index, vectorizer, document_names

def save_index(index, inverted_index, vectorizer, document_names, filename):
    with open(filename, 'wb') as f:
        pickle.dump((index, inverted_index, vectorizer, document_names), f)

def load_index(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def print_inverted_index(inverted_index, vectorizer):
    feature_names = vectorizer.get_feature_names_out()
    print("Inverted Index:")
    for term in feature_names:
        if term in inverted_index:
            print(f"Term: {term}")
            postings_list = inverted_index[term]
            for posting in postings_list:
                print(f"   Document Name: {posting[0]}, TF-IDF Score: {posting[1]}")
            print()

def main():
    # Specify the directory where the HTML documents are stored
    html_files_directory = 'html_files_directory'  # Update with actual path
    documents, document_names = load_documents(html_files_directory)

    # Build the TF-IDF index
    X, inverted_index, vectorizer, document_names = build_index(documents, document_names)

    # Specify the filename to save the index
    index_filename = 'inverted_index.pkl'

    # Save the index and vectorizer to a file
    save_index(X, inverted_index, vectorizer, document_names, index_filename)

    print("Index successfully saved to:", index_filename)

    # Example usage: Load the index from the pickle file
    index_data = load_index(index_filename)
    X_loaded, inverted_index_loaded, vectorizer_loaded, document_names_loaded = index_data

    # Print inverted index
    print_inverted_index(inverted_index_loaded, vectorizer_loaded)

if __name__ == "__main__":
    main()
