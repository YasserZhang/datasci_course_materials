import sys
import json

tweets = []
words_list = []

def tweet():
    tweet_file = open(sys.argv[1])
    tweet_file = tweet_file.readlines()
    for line in tweet_file:
        t = json.loads(line)
        if "text" in t.keys():
            tweets.append(t["text"])
def seperate():
    for line in tweets:
        #lst = line.split(" ")
        for word in line.split(" "):
            word= word.strip()
            words_list.append(word)
def main():
    tweet()
    seperate()
    for word in set(words_list):
        print word + " " + str((words_list.count(word) + 0.0)/len(words_list))

if __name__ == '__main__':
    main()
