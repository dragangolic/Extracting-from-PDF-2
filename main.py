import re
from pdfminer.high_level import extract_pages, extract_text

# for page_layout in extract_pages("sample.pdf"):
#     for element in page_layout:
#         print(element)

text = extract_text("sample.pdf")
print(text)

# letters followed by comma and space
pattern = re.compile(r"[a-zA-Z]+,{1}\s{1}")
matches = pattern.findall(text)
print(matches)

# extract names
names = [n[:-2] for n in matches]
print(names)
