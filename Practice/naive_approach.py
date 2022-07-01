from itertools import count
import pandas as pd

df = pd.read_csv('./dataset/Amazon_Unlocked_Mobile.csv')

group = df['Reviews'].groupby(df['Product Name'])

df1 = pd.DataFrame(group)

product_reviews = {}
for name,product in zip(df1[0],df1[1]):
    text = ""

    for r in product:
        text += str(r) + " "

    product_reviews[name] = text


'''         Used for taking input text for analysis in other text file      '''
# text = open('./read.txt',encoding='utf-8').read()



# stop-words removing : pronouns, extra words
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
            "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
            "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
            "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
            "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
            "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
            "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
            "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
            "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
            "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]



''' 👇  Code to detect emotion of each product review 👇 '''

count = 0
for name,text in product_reviews.items():
    print(name)
    count += 1

    # making lowercase
    import string
    lower_case = text.lower()

    # remove punctuations
    cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))

    # tokenization - sentence to words
    tokenized_words = cleaned_text.split()


    # removing stop-words
    final_words = []
    for word in tokenized_words:
        if word not in stop_words:
            final_words.append(word)


    # Algorithm for Emotion and Text Analysis

    # detecting emotion words if present in emotion_dict(file)
    # analysing emotion present in text file

    emotion_list = []
    with open('./emotions.txt','r') as file:
        for line in file:
            clear_dict = line.replace("\n","").replace(",","").replace("'","").strip()
            emotion,word = clear_dict.split(':')
            if emotion in final_words:
                emotion_list.append(word) 



    # Counting emotions
    from collections import Counter
    w = Counter(emotion_list)


    '''     Matplotlib is a low level graph plotting library in python that serves as a visualization utility.      '''
    import matplotlib.pyplot as plt

    '''     Method-1 : to show graph    '''
    # x-axis labels are overlapped
    # plt.bar(w.keys(),w.values())


    '''     Method-2 : to show graph        '''
    # x-axis labels are NOT overlapped
    fig, ax1 = plt.subplots()
    ax1.bar(w.keys(),w.values())
    fig.autofmt_xdate()

    plt.title(name, fontsize=10)

    '''     save graph locally      '''
    # plt.savefig("bar_graph_emotion_list.jpg")
    plt.show()
    if count==3:
        break

