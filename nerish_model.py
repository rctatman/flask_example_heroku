from flashtext.keyword import KeywordProcessor
import pickle

# funtion that takes in a text string & returns "NER" output
def get_keywords(post):
    # read in pickled word processor
    with open("word_processor.pkl", "rb") as file:
        keyword_processor = pickle.load(file)
    
    keywords_found = keyword_processor.extract_keywords(post, span_info=True)
    return keywords_found
