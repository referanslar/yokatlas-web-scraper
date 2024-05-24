import re, json

class Common:
    def transform(self, key):
        def turkish_to_english(s):
            turkish_chars = "şŞıİçÇöÖüÜğĞ"
            english_chars = "sSiIcCoOuUgG"
            translation_table = str.maketrans(turkish_chars, english_chars)
            
            return s.translate(translation_table)
        
        def clean_key(key):
            key = turkish_to_english(key)
            key = key.lower()
            key = re.sub(r'\W+', '', key)

            return key

        return clean_key(key)

    def pretty(self, data):
        print(json.dumps(data, indent=4, ensure_ascii=False))
