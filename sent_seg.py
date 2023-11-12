import re

Text = " Artificial Intelligence is a new technology in the field of computer science. “Artificial” means man-made that is not natural and “Intelligence” refers to the ability to think and make decisions."
w=0
s=0
print("The text is \n",Text)

print("\nSegmenting the above text into sentences\n")
sentence_endings = r"[.?!]"
sentences=re.split(sentence_endings, Text)
for sentence in sentences:
    s=s+1
    print(sentence)

print("Segmenting the above text into words ")
PATTERN = r"\w+"
words=re.findall(PATTERN, Text)
for word in words:
    w=w+1
    print(word)


print("No of sentences=",s)
print("No of words=",w)
