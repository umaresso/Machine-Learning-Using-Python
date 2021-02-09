
from textblob import TextBlob
numberOfTweets = input("Enter Number of Tweets you want to Analyze ? \n")
size = int(numberOfTweets)
i=0
texts =[" "]*size
analysis = [" "]*size
#Getting Input From User
for i in range(0,size):
    val = input("\nEnter {}th Tweet \n".format(i+1))
    analyze = TextBlob(val)
    texts[i] = val
    analysis[i] = str(analyze.sentiment)

print("\nFollowing is the list of Tweets , the Analyzed Version\n")
for i in range(0,size):
    print("{}\t {}".format (texts[i],analysis[i] ) ) 

import csv

with open('Sentiment_analysis_File.csv', mode='w') as Sentiment__File:
   Sentiment__File = csv.writer(Sentiment__File, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
   Sentiment__File.writerow( ['Texts ','Sentiments'] )
   for i in range(0,size):
       Sentiment__File.writerow([ texts[i] ,analysis[i] ])

print("\nCSV File is Saved AS Follows \n")

with open('Sentiment_analysis_File.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
            print(row)
        

        


