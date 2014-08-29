import sys
import json

entities = []
hashtag_list = []
results = {}

def tweet():
    tweet_file = open(sys.argv[1])
    tweet_file = tweet_file.readlines()
    for line in tweet_file:
        t = json.loads(line)
        if "entities" and "lang" in t.keys() and t["lang"] == "en":
            entities.append(t["entities"])

def listing():
    for line in entities:
        #lst = line.split(" ")
        hashtags = line["hashtags"]
        if hashtags != []:
            hashtag_list.append(hashtags[0]["text"].encode('utf-8'))

def main():
    tweet()
    listing()
    for word in set(hashtag_list):
       results[word] = hashtag_list.count(word)
    lst = sorted(results.items(), key = lambda x:x[1],reverse=True)[0:10]
    for line in lst:
        print line[0],line[1]
    
'''
    for word in set(words_list):
        print word + " " + str((words_list.count(word) + 0.0)/len(words_list))
'''
if __name__ == '__main__':
    main()
