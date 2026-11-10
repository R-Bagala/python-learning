from concurrent.futures.thread import BrokenThreadPool
import json

def most_spoken_languages(filepath, number_of_languages):
    with open ("C:/Users/bagal/OneDrive/Personal projects/Python/countries_data.json", "r", encoding='utf-8') as language_text:
        #content = language_text.read()
        data = json.load(language_text)
        countries_dct = {item["name"]: item for item in data}
        languages_array = []
        #return countries_dct["Afghanistan"]["languages"] #this works follow this. Maybe do a for i in range loop of len(countries_dct)
        for outer_key in countries_dct:
            inner_dict = countries_dct[outer_key]
            if "languages" in inner_dict: 
                languages_array.append(inner_dict["languages"])
        languages_list = [i for j in languages_array for i in j]
        language_dct = {}
        for i in range(len(languages_list)):
            language_dct[languages_list[i]] = languages_list.count(languages_list[i])
        language_dct = dict(sorted(language_dct.items(), key = lambda item: item[1], reverse = True))
        languages = dict(list(language_dct.items())[0: number_of_languages])
        return languages
    

print(most_spoken_languages(filepath = "C:/Users/bagal/OneDrive/Personal projects/Python/countries_data.json", number_of_languages=10))