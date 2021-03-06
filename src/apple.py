import nltk
import re,sys
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
import pickle,random
from nltk.corpus import stopwords  
import fileinput	
#funtion to stem out the root words
def stemwords(wordtostem):
	stemmedwords = []
	words_list4 = word_tokenize(wordtostem)
	for words in words_list4:

		words_filtered = nltk.stem.porter.PorterStemmer().stem_word(words)

		stemmedwords.append(words_filtered)
	return stemmedwords

#function to convert sentences into 	er case
def lowr(item_type):
		sentim = []
		item = ''
		i =j= 0
		newwords = []
		for words in final_words:
			words_filtered,item = [e.lower() for e in words.split() if len(e) >= 4],item_type

			if (i<10):
				newwords += words_filtered
				
				i+=1
			else:
				tempfile = (newwords,item)
				sentim.append(tempfile)
				newwords = []

				i = 0
		return sentim

#functon to make a list of words in the file.
def get_words_in_senti(senti):
	all_words = []
	for (word, sentiment) in senti:
		all_words.extend(word)
	return all_words

#function to get the features of each word
def get_word_features(wordlist):
	wordlist = nltk.FreqDist(wordlist)
	word_features = wordlist.keys()
	return word_features


word_features = []
#function to find out the occurences of words when comparison between files are done
def extract_features(document):
	try:
		global i,word_features
		i = 0
		document_words = set(document)
		features = {}
		for word in word_features:
				if word in document_words:
   					features['contains(%s)' % word] = True
   					
		return features
	except ValueError:
		print "Oops! Not Available. Try again..."
		
#function to extract unique words from the list
def unique_list(l):
	ulist = []
	[ulist.append(x) for x in l if x not in ulist]
	return ulist
	    
#function to read the content of the given file
def read_words(words_file2):
    open_file2 = open(words_file2, 'r')
    words_list2 =[]
    contents2 = open_file2.readlines()
    for i in range(len(contents2)):
        words_list2.append(contents2[i].strip('\n'))
    open_file2.close()  
    tokenizer = RegexpTokenizer(r'\w+')
    words_list3 = tokenizer.tokenize(str(words_list2))
    punctuation = re.compile(r'[-.?!,":;()|0-9]')
    word_list5 = [punctuation.sub("", word) for word in words_list3]
    sentu = ' '.join(map(str, unique_list(word_list5)))
    return sentu  
    
#funtiion to remove duplicate entries
def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist
    
#function to classify the words by comparing the given files' contents
def classi(lst,sent):
	global word_features
	
	word_features = get_word_features(get_words_in_senti(lst))

	random.shuffle(lst)
	training_set = nltk.classify.apply_features(extract_features, lst)

	train_set, test_set = training_set[len(training_set)*3/4:], training_set[len(training_set)*1/2:len(training_set)]
	

	classifier1 = nltk.NaiveBayesClassifier.train(train_set)
	result = classifier1.classify(extract_features(sent.split()))
	print result
	print 'Accuracy: %f'%(nltk.classify.accuracy(classifier1, test_set))
		
listapple = []
print "Reading Apple Computer's File.."
listofwords = read_words('/home/nihalm/Check-Content/data/apple-computers.txt')
listword = stemwords(listofwords)
filtered_words = listword
final_words = list(set(filtered_words))
listapple += lowr('computer-company')

print "Reading Apple Fruit's File.."	
listofwords = read_words('/home/nihalm/Check-Content/data/apple-fruit.txt')
listword = stemwords(listofwords)
filtered_words = listword
final_words = list(set(filtered_words))
listapple += lowr('fruit')	
#print listapple
#txtfile = open('/home/nihalm/sample.txt','w')
#txtfile.write(str(listapple))
#txtfile.close()

wordl = []
print "Please Input File.."
while True:
    wordl = []
    wordl  = sys.stdin.readline()
    tokenizer = RegexpTokenizer(r'\w+')
    words_list3 = tokenizer.tokenize(str(wordl))
    punctuation = re.compile(r'[-.?!,":;()|0-9^\x00-\x7F]')
    word_list8 = [punctuation.sub("", word) for word in words_list3]
    wordll = ' '.join(map(str, word_list8))
    print "Stemming Words.."
    stemsent1 = stemwords(wordll)
    print "Making List.."
    final_words = list(set(stemsent1))
    stemsent2 = lowr(final_words)
    sent2 = ' '.join(map(str, final_words))
    print "Classifying.."
    classi(listapple,sent2)
			
		
	
#End
