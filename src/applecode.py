# Enter your code here. Read input from STDIN. Print output to STDOUT
import operator
import re

fruit_lookup = {}
company_lookup = {}

N = int(raw_input())
with open('apple-fruit.txt','r') as fruit:
    for line in fruit:
        for word in re.split('\W+', line.upper()):
            if word not in fruit_lookup:
                fruit_lookup[word] = 1
            else:
                fruit_lookup[word] += 1

with open('apple-computers.txt','r') as company:
    for line in company:
        for word in re.split('\W+', line.upper()):
            if word not in company_lookup:
                company_lookup[word] = 1
            else:
                company_lookup[word] += 1

sorted_fruit = sorted(fruit_lookup.iteritems(), key=operator.itemgetter(1))    

#remove frequent and common words    
for word in sorted_fruit[:200]:
    if word in company_lookup:
        del company_lookup[word]
        del fruit_lookup[word]

for i in range(N):
    line = raw_input()
    #use simple heuristic as a first check otherwise do word based scoring
    if 'apple' in line or 'apples' in line or 'APPLES' in line.upper():
        print 'fruit'
        continue

    line = re.split('\W+', line.upper())
    fruit_score = 0
    company_score = 0

    for word in line:
        if word in fruit_lookup:
            fruit_score += 1
        if word in company_lookup:
            company_score += 1

    if company_score > fruit_score:
        print 'computer-company'
    else:
        print 'fruit' 

