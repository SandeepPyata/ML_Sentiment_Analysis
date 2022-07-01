# Youtube Link for SA without ML : https://youtube.com/playlist?list=PLhTjy8cBISEoOtB5_nwykvB9wfEDscuEo


from itertools import count
import pandas as pd
import string

from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer


df = pd.read_csv('./dataset/Amazon_Unlocked_Mobile.csv')
group = df['Reviews'].groupby(df['Product Name'])
df1 = pd.DataFrame(group)

# print(df1)

product_reviews = {}
for name,product in zip(df1[0],df1[1]):
    text = ""
    for r in product:
        text += str(r) + " "
    product_reviews[name] = text


'''     Detecting sentiment for sentence    '''
def sentiment_analyze(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    if(neg>pos):
        print("Negative sentiment :(\n")
    elif(pos>neg):
        print("Positive Sentiment :)\n")
    else:
        print("Neutral Sentiment :|\n")


count = 0
for name,text in product_reviews.items():
    print(name)
    count += 1

    # making lowercase
    lower_case = text.lower()

    # remove punctuations
    cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
        
    # detect sentiment for cleaned_text
    sentiment_analyze(cleaned_text)


    '''  Tokenization - sentence to words  '''
    # word_tokenize -> to extract the syllables from stream of words or sentences.
    # word_tokenize is better than split() in terms of time complexity & performance
    # parameters : text, language
    # Eg: Tokenize("Gametophyte") => [‘Ga’, ‘me’, ‘to’, ‘phy’, ‘te’]

    tokenized_words = word_tokenize(cleaned_text,"english")


    '''     A corpus is a collection of authentic text or audio organized into datasets. 
            Authentic here means text written or audio spoken by a native of the language or dialect. 
            A corpus can be made up of everything from newspapers, novels, recipes, radio broadcasts to television shows, movies, and tweets.
    '''

    # removing stop-words
    final_words = []
    stop_words = stopwords.words('english')
    for word in tokenized_words:
        if word not in stop_words:
            final_words.append(word)

    
    # # '''     Stemming    '''    
    # # from nltk.stem.snowball import SnowballStemmer
    
    # # #the stemmer requires a language parameter
    # # snow_stemmer = SnowballStemmer(language='english')
    
    # # #stem's of each word
    # # stem_words = []
    # # for w in final_words:
    # #     x = snow_stemmer.stem(w)
    # #     stem_words.append(x)
    
    # '''     Lemmatization   '''
    # from nltk.stem.wordnet import WordNetLemmatizer
    # # Reduce words to their root form
    # lemmed = [WordNetLemmatizer().lemmatize(w) for w in final_words]



    # # Algorithm for Emotion and Text Analysis

    # # detecting emotion words if present in emotion_dict(file)
    # # analysing emotion present in text file

    # emotion_list = []
    # with open('./emotions.txt','r') as file:
    #     for line in file:
    #         clear_dict = line.replace("\n","").replace(",","").replace("'","").strip()
    #         emotion,word = clear_dict.split(':')
    #         if emotion in final_words:
    #             emotion_list.append(word) 



    # # Counting emotions
    # from collections import Counter
    # w = Counter(emotion_list)


    # '''     Matplotlib is a low level graph plotting library in python that serves as a visualization utility.      '''
    # import matplotlib.pyplot as plt

    # '''     Method-1 : to show graph    '''
    # # x-axis labels are overlapped
    # # plt.bar(w.keys(),w.values())


    # '''     Method-2 : to show graph        '''
    # # x-axis labels are NOT overlapped
    # fig, ax1 = plt.subplots()
    # ax1.bar(w.keys(),w.values())
    # fig.autofmt_xdate()

    # plt.title(name, fontsize=10)

    # '''     save graph locally      '''
    # # plt.savefig("bar_graph_emotion_list.jpg")
    
    # plt.show()
    if count==6:
        break