# helpful class for counting (you can do it another way of course)
from collections import Counter

# other classes you will need
from flair.data import Sentence
from flair.models import TextClassifier, SequenceTagger
from collections import Counter
# open review file
review_file = open("data/game_reviews.txt")

# read all reviews into an array
all_reviews = review_file.readlines()

# TODO: instantiate sentiment tagger and part-of-speech tagger
tagger = TextClassifier.load('sentiment-fast')

# TODO: predict sentiment and pos tags for all reviews
all_reviews_st=[Sentence(review) for review in all_reviews]
for reviewst in all_reviews_st:
    tagger.predict(reviewst)
good_reviews_st=[reviewst for reviewst in all_reviews_st if reviewst.get_labels()[0].value=='POSITIVE']
bad_reviews_st=[reviewst for reviewst in all_reviews_st if reviewst.get_labels()[0].value=='NEGATIVE']

# TODO: count most common nouns and adjectives for positive/negative reviews and print
taggers = SequenceTagger.load("upos-fast")
for goodreview in good_reviews_st:
    taggers.predict(goodreview)
for badreview in bad_reviews_st:
    taggers.predict(badreview)

pro_adj=[word.text for goodreview in good_reviews_st for word in goodreview if word.get_tag('pos').value =='ADJ' ]
neg_adj=[word.text for badreview in bad_reviews_st for word in badreview if word.get_tag('pos').value =='ADJ' ]

pro_noun=[word.text for goodreview in good_reviews_st for word in goodreview if word.get_tag('pos').value =='NOUN' ]
neg_noun=[word.text for badreview in bad_reviews_st for word in badreview if word.get_tag('pos').value =='NOUN' ]

pro_adj_count=Counter(pro_adj)
neg_adj_count=Counter(neg_adj)
pro_noun_count=Counter(pro_noun)
neg_noun_count=Counter(neg_noun)

a= [word for word, word_count in pro_adj_count.most_common(10)]
b= [word for word, word_count in neg_adj_count.most_common(10)]
c= [word for word, word_count in pro_noun_count.most_common(10)]
d= [word for word, word_count in neg_noun_count.most_common(10)]
print(a,b,c,d)

str1 = '   '.join(a)
str2 = '   '.join(b)
str3 = '   '.join(c)
str4 = '   '.join(d)
lines=[]
f=open("findings.txt",'r')  #
for line in f:
    lines.append(line)
f.close()

lines.insert(2,str1)
lines.insert(6,str2)  
lines.insert(10,str3)  
lines.insert(14,str4)      

s1=''.join(lines)
f=open("findings.txt",'w+') #重新写入文件
f.write(s1)
f.close()

