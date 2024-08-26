# Query-Based-Recommendation-System

Overview:


This project focuses on comparing three versions of FastText models—CBOW, Skip-gram, and a pre-trained model from Facebook—trained on the Goodreads dataset. The aim is to evaluate the performance of these models in a query based book recommendation task.

Models Used:


CBOW (Continuous Bag of Words): A version of FastText where the model predicts the target word from the surrounding context words.
Skip-gram: A version of FastText that predicts the surrounding context words from a given target word.
Pre-trained Facebook Model: A FastText model pre-trained by Facebook on a large-scale corpus. (https://huggingface.co/facebook/fasttext-en-vectors)

Dataset:


Goodreads Dataset
The Goodreads dataset consists of book reviews and metadata collected from the Goodreads platform. It provides a rich source of textual data, making it ideal for training and evaluating word embeddings and text classification models.

Source: https://datarepo.eng.ucsd.edu/mcauley_group/gdrive/goodreads/goodreads_books.json.gz


After Preprocessing: https://huggingface.co/datasets/booksouls/goodreads-book-descriptions
