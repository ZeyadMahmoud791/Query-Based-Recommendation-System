import bs4
import nltk
import string

nltk.download("punkt", raise_on_error=True, quiet=True)
nltk.download("stopwords", raise_on_error=True, quiet=True)

stopwords = set(nltk.corpus.stopwords.words("english"))
detokenizer = nltk.TreebankWordDetokenizer()
punctuation_remover = str.maketrans("", "", string.punctuation)

def preprocess(text: str) -> str:
    text = bs4.BeautifulSoup(text, "html.parser").get_text()
    text = text.lower()
    text = text.translate(punctuation_remover)
    tokens = nltk.word_tokenize(text)
    tokens = [token for token in tokens if token not in stopwords]
    return detokenizer.detokenize(tokens)

if __name__ == "__main__":
    import datasets
    import tqdm
 
    with open("train.txt", "w") as file:
        dataset = datasets.load_dataset("booksouls/goodreads-book-descriptions", split="train")
        for row in tqdm.tqdm(dataset):
            description = preprocess(row["description"])
            file.write(description)
            file.write("\n")
