
# PySearch: A Comprehensive Information Retrieval System in Python

**Author:** Abhinay Jajula  
**Student ID:** A20548474  
**Email:** ajajula@hawk.iit.edu  

## Abstract

The project endeavors to create a robust information retrieval system, leveraging Python libraries like Scrapy, Scikit-Learn, and Flask. It encompasses a web crawler for efficient web document retrieval, an indexer employing TF-IDF scores and cosine similarity for constructing an inverted index, and a query processor for handling user queries. Objectives include developing scalable crawling mechanisms, implementing efficient indexing techniques, and creating a responsive query processing system. Methodologically, the project employs Scrapy for web crawling, Scikit-Learn for TF-IDF computation and cosine similarity, and Flask for query processing. Outcomes include a fully functional information retrieval system, offering fast and accurate search results to users. Through this project, we seek to address the growing need for effective information retrieval systems in various domains such as research, education, and business intelligence. Moving forward, the next steps involve optimizing system performance, enhancing query processing capabilities, and exploring additional features such as query spelling correction and expansion to improve user experience and satisfaction.

## 1. Overview

### 1.1 Problem Statement

The project involves the development of an information retrieval system consisting of three main components: a web crawler, an indexer, and a query processor. The web crawler is responsible for fetching HTML documents from predefined URLs, the indexer constructs an inverted index from the downloaded documents, and the query processor handles user queries to retrieve relevant documents.

The system utilizes Python libraries such as Scrapy for web crawling, Scikit-Learn for indexing, and Flask for query processing. By integrating these components, the system enables users to search for information across multiple web documents efficiently.

### 1.2 Literature Survey

1. **"Information Retrieval Systems: Principles and Algorithms" by Baeza-Yates and Ribeiro-Neto**: This seminal work provides a comprehensive overview of information retrieval principles and algorithms. It covers fundamental concepts such as indexing, querying, and relevance ranking, making it an essential resource for understanding the theoretical foundations of information retrieval systems.

2. **"Web Crawling and Data Mining: Techniques and Applications" by Zhao and Yan**: This book explores the techniques and applications of web crawling and data mining for information retrieval purposes. It discusses various crawling strategies, data extraction methods, and data mining algorithms, offering insights into the practical aspects of building web-based information retrieval systems.

3. **"Text Mining: Concepts, Process, and Applications" by Feldman and Sanger**: Text mining plays a crucial role in information retrieval by extracting meaningful insights from unstructured text data. This book covers the concepts, processes, and applications of text mining, including techniques for document preprocessing, feature extraction, and text classification, which are essential for building effective information retrieval systems.

4. **"Machine Learning for Information Retrieval: Foundations and Applications" by Manning, Raghavan, and Schütze**: Machine learning techniques have revolutionized information retrieval by enabling the development of more intelligent and adaptive systems. This book provides a comprehensive overview of machine learning algorithms and their applications in information retrieval tasks such as document classification, relevance ranking, and query expansion, offering valuable insights into the state-of-the-art approaches in the field.

5. **"Natural Language Processing with Python" by Bird, Klein, and Loper**: Natural language processing (NLP) is essential for understanding and processing human language, which is crucial for effective information retrieval. This book introduces the basics of NLP using Python, covering topics such as tokenization, stemming, part-of-speech tagging, and named entity recognition, which are indispensable for processing textual data in information retrieval systems.

### 1.3 Methodology/Approach

1. **Web Crawling**: Utilize Scrapy, a Python framework, for efficient web crawling. Define seed URLs and set parameters for maximum pages and depth to retrieve relevant HTML documents.

2. **Indexing**: Employ Scikit-Learn library for indexing. Implement TF-IDF (Term Frequency-Inverse Document Frequency) scoring and cosine similarity to construct an inverted index from the downloaded documents.

3. **Query Processing**: Develop a Flask-based query processor to handle user queries in JSON format. Implement query validation and error-checking mechanisms to ensure accurate processing.

## 2. Design

### System Capabilities

- **Crawler** can initialize with a seed URL and parameters for depth and page limits. Optional features include auto-throttling and distributed crawling.

- **Indexer** supports various document processing techniques and the calculation of cosine similarity for document ranking.

- **Query Processor** validates and processes queries, returning top-k ranked results based on user input.

### Interactions

The interactions between components are as follows:

- The web crawler fetches HTML documents and stores them locally.

- The indexer reads the downloaded documents, constructs an inverted index, and saves it in pickle format.

- The query processor loads the inverted index, processes user queries, and retrieves relevant documents.

### Integration

The components are integrated as follows:

- The web crawler outputs HTML documents to a designated directory.
- The indexer reads HTML documents from the directory, constructs an inverted index, and saves it to a pickle file.
- The query processor loads the inverted index from the pickle file and listens for user queries via HTTP requests.

## 3. Architecture

### Software Components

1. **Web Crawler (Scrapy):** Responsible for fetching HTML documents from web pages.
2. **Indexer (Scikit-Learn):** Constructs an inverted index from downloaded documents.
3. **Query Processor (Flask):** Handles free-text queries and retrieves relevant documents.

### Interfaces

- The web crawler communicates with the indexer by writing downloaded documents to a designated directory.
- The indexer communicates with the query processor by providing the inverted index via file loading.
- The query processor communicates with users via HTTP requests and responses.

### Implementation

- **Web Crawler:** Implemented using Scrapy framework with Python.
- **Indexer:** Implemented using Scikit-Learn library for TF-IDF vectorization and cosine similarity calculation.
- **Query Processor:** Implemented using Flask framework for HTTP server and request handling.

## 4. Operation

### Software Commands

- **Web Crawler:** No user commands required; runs automatically upon execution.
- **Indexer:** Executes `indexing.py` script to build the inverted index.
- **Query Processor:** Executes `app.py` script to start the Flask server and handle queries.

### Inputs

- **Web Crawler:** Seed URLs, maximum pages, maximum depth.
- **Indexer:** HTML documents downloaded by the web crawler.
- **Query Processor:** User queries in JSON format.

### Installation

No specific installation steps required. Ensure Python 3.10+ and the required libraries (Scrapy, Scikit-Learn, Flask) are installed.
Environment setup:
<img width="1470" alt="Screenshot 2024-04-16 at 8 16 26 PM" src="https://github.com/ASP24SCM74J/IR_project_search_engine/assets/163171551/5a37809d-1800-4fdd-ab70-a28cbc50bac5">


## 5. Conclusion

The project successfully developed an information retrieval system capable of crawling web documents, constructing an inverted index, and handling user queries. The system demonstrates the integration of various Python libraries to create an efficient and scalable solution for information retrieval tasks.

## 6. Data Sources

The project utilizes web documents from various Wikipedia pages as data sources. The documents are downloaded and stored locally for indexing and querying purposes.
- **Website urls stored in urls.txt file:**
  

## 7. Test Cases

Test cases were conducted to validate the functionality of each component:

- **Web crawler:** Verified correct fetching and storage of HTML documents. Command: `scrapy crawl wiki`
  <img width="1470" alt="Screenshot 2024-04-16 at 8 24 26 PM" src="https://github.com/ASP24SCM74J/IR_project_search_engine/assets/163171551/582b24cd-b8ae-4ea0-ac14-9d6e2812d34a">

  
- **Indexer:** Ensured accurate construction of the inverted index and cosine similarity calculation.
  After running the command in root directory: `Python3 indexing.py`
- The resulting file is `inverted_index.pkl`.
- output of inverted_index.pkl file is:
 ![7A2A4D74-DAE6-45C9-86CE-AE2795D7D2CD_1_201_a](https://github.com/ASP24SCM74J/IR_project_search_engine/assets/163171551/f568e337-5852-4d42-92fd-d7eec0478917)

- **Query processor:** Tested query validation, error-checking, and retrieval of relevant documents using commands such as:
- In this step it will import `indexing.py file` and access the tokens, doc names, cosine similarity and runs the flask:
- Command: `python3 app.py or flask run`
- The above command will tell us where it is running:
![04F4A307-5925-4DD3-9072-D5F37841CB06_1_201_a](https://github.com/ASP24SCM74J/IR_project_search_engine/assets/163171551/29ed2e14-584b-409c-ba2d-02fdd78de751)



- After running the command `Python3 app.py` flask will run.
- Open the new terminal and pass the below commands:
- Query-1 command:
  ```bash
      curl -X POST http://127.0.0.1:5000/query \
      -H "Content-Type: application/json" \
      -d '{"query": "data privacy", "top_k": 5}'
  ```

- Query-2 command: 
   ```bash
       curl -X POST http://127.0.0.1:5000/query \
      -H "Content-Type: application/json" \
      -d '{"query": "application of information retrieval", "top_k": 5}'
  ```

- **Final Output:**
<img width="1000" alt="Screenshot 2024-04-16 at 6 03 02 PM" src="https://github.com/ASP24SCM74J/IR_project_search_engine/assets/163171551/7f8fb0e2-513e-41d6-afd1-e37f78beae03">

## 8. Source Code:
The source code for the project is available in the following files:
- **[Wiki_spider.py (Scrapy crawler)](https://github.com/ASP24SCM74J/IR_project_search_engine/blob/main/wikicrawler/wikicrawler/spiders/wiki_spider.py)**
- **[indexing.py (Indexer)](https://github.com/ASP24SCM74J/IR_project_search_engine/blob/main/wikicrawler/indexing.py)**
- **[app.py (Query processor)](https://github.com/ASP24SCM74J/IR_project_search_engine/blob/main/wikicrawler/app.py)**
- **[Pickle file](https://github.com/ASP24SCM74J/IR_project_search_engine/blob/main/wikicrawler/inverted_index.pkl)**
- **[Scrapped pages](https://github.com/ASP24SCM74J/IR_project_search_engine/blob/main/wikicrawler/inverted_index.pkl)**
- **[source for webscrapping html urls.txt file](https://github.com/ASP24SCM74J/IR_project_search_engine/blob/main/wikicrawler/urls.txt)**

## 9. Bibliography:
References to libraries, frameworks, and resources used in the project:
- Scrapy: https://scrapy.org/
- Scikit-Learn: https://scikit-learn.org/
- Flask: https://flask.palletsprojects.com/
- Cloudflare. (n.d.). What is a Web Crawler? Retrieved from https://www.cloudflare.com/learning/bots/what-is-a-web-crawler/
- Web Mining IS688. (2021, Spring). Cosine Similarity and TFIDF. Medium. Retrieved from https://medium.com/web-mining-is688-spring-2021/cosine-similarity-and-tfidf-c2a7079e13fa
- Ravi, J. (2013, October 27). TF-IDF and Cosine Similarity [Blog post]. Retrieved from https://janav.wordpress.com/2013/10/27/tf-idf-and-cosine-similarity/
- Stack Overflow. (n.d.). How vectorizer.fit_transform() work in sklearn? Retrieved from https://stackoverflow.com/questions/47898326/how-vectorizer-fit-transform-work-in-sklearn




