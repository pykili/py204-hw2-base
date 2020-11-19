my_text = "кошка мыла\nложку, собаку, и.. виноград"
my_text_striped = my_text.strip()
my_text_cleaned = my_text_striped.replace(',', '')
my_text_cleaned = my_text_cleaned.replace('.', '')
my_text_tokenized = my_text_cleaned.split()

my_orig_ixes_new_values = [-1] * len(my_text)
# your code here
