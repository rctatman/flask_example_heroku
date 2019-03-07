from flashtext.keyword import KeywordProcessor
import pickle
import json

# funtion that takes in a text string & returns "NER" output
def get_keywords_api():
    # read in pickled word processor
    with open("word_processor.pkl", "rb") as file:
        keyword_processor = pickle.load(file)
    
    # get our keywords 
    def keywords_api(post): 
        keywords_found = keyword_processor.extract_keywords(post, span_info=True)
        
        output_data = json.dumps(keywords_found)
        
        return output_data
    
    return keywords_api
