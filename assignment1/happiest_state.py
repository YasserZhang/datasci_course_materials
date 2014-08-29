import sys
import json
states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}
#execfile("cities_states.py")
scores = {}
eng_twt = []
loc_twt = []
state_twt = {}
results = {}
def sentiment():
    sent_file = open(sys.argv[1])
    for line in sent_file:
        term, score = line.split("\t") # The file is tab-delimited
        scores[term] = int(score)

def eng_tweet():
    tweet_file = open(sys.argv[2])
    tweet_file = tweet_file.readlines()
    #t = json.loads(tweet_file[30])
    #print t.keys()
    #print t["user"].keys()
    for line in tweet_file:
        t = json.loads(line)
        if "lang" in t.keys() and t["lang"] == "en":
            eng_twt.append(t)
    #print len(eng_twt)

def tweet_in_us():
    for twt in eng_twt:
        #location.append(twt["user"]["location"])
        a = twt["user"]["location"]
        for b in a.split(","):
            b = b.strip()
            if b in states.keys() or b in states.values():
                loc_twt.append(twt)
                break
def tweet_by_state():
    for twt in loc_twt:
        a = twt["user"]["location"].split(",")
        b=[]
        for word in a:
            b.append(word.strip())
        for abb, state in states.items():
            if abb in b or state in b:
                if abb not in state_twt.keys():
                    state_twt[abb] = [twt]
                else:
                    state_twt[abb].append(twt)
            else:
                pass

def tweet_score():
    for state, tweet in state_twt.items():
        c = 0
        tweets = []
        for twt in tweet:
            if "text" in twt.keys():
                tweets.append(twt["text"])
        for txt in tweets:
            lst = txt.split(" ")
            for word in lst:
                word = word.encode('utf-8').lower()
                if word in scores.keys():
                    c += scores[word]
        results[state] = (c + 0.0)/len(tweets)

    #print location[0:100]

    '''
    for line in tweet_file:
        t = json.loads(line)
    '''        

'''
        if "location" in t.keys():
            location.append(t["location"])
    print len(location)
'''


def main():
    sentiment()
    eng_tweet()
    tweet_in_us()
    tweet_by_state()
    tweet_score()
    for state, score in results.items():
        if score == max(results.values()):
            print state
        

if __name__ == "__main__":
    main()
'''        
english tweets ---> tweets with location ---> assign tweets to different groups by states ---> rating happiness of each group
finally build a dictionary whose keys are state names and values are lists of tweets
'''
