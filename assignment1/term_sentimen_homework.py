import sys
import json

scores = {}
tweets = []
tweets_words = []
words = {}
def sentiment():
    sent_file = open(sys.argv[1])
    for line in sent_file:
        term, score = line.split("\t") # The file is tab-delimited
        scores[term] = int(score)

def tweet():
    tweet_file = open(sys.argv[2])
    tweet_file = tweet_file.readlines()
    for line in tweet_file:
	t = json.loads(line)
	if "text" in t.keys():
	    tweets.append(t["text"])

def evaluation():
    for lst in tweets:
        lst1= []
        score = 0
        for word in lst.split(" "):
            word = word.encode("utf-8").lower()
            tweets_words.append(word)
            lst1.append(word)
        for word in lst1:
            if word in scores.keys():
                score += scores[word]
            else:
                pass
        for word in lst1:
            if word not in scores.keys():
                if word in words.keys():
                    words[word] += score
                else:
                    words[word] = score
            else:
                pass
  
def main():
    sentiment()
    tweet()
    evaluation()
    for word in words.keys():
        print word, (words[word] + 0.0)/tweets_words.count(word)

'''
def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)
'''
if __name__ == '__main__':
    main()


