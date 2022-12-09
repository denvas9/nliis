def eq_rating(files: list, search: str):
    # слова в запросе
    search_list = [word.strip() for word in set(search.lower().split())]
    
    for file in files:
        matched_words = [word for word in file['words'] if word in search_list]
        
        eq_rate = len(matched_words)
        #for word in file.words_from_query:
        #    eq_rate += file.words_weight_coef[word]
            #print(word, file.words_weight_coef[word])
        file['words_from_query'] = matched_words
        file['eq_rate'] = eq_rate
        

def get_rated_files(files, search):
    eq_rating(files, search)
    #print(files)
    return sorted(files, key=lambda file: file['eq_rate'], reverse=True)
