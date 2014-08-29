import sys
count = 0
def main():
    global count
    sent_file = open(sys.argv[1])
    for line in sent_file:
      count += 1
    print count

if __name__ == '__main__':
    main()
