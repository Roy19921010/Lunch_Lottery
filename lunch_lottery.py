import requests
import re
import random
import matplotlib.pyplot as plt
r = requests.get('https://www.strawpoll.me/17209027/r')
#print(r.text)
search_pattern=re.compile('<p class="option-text"><span>(.*)</span> <span class="option-count" data-count=(.*)>(.*)</span></p>')
places_votes = re.findall(search_pattern, r.text)
#print(places_votes)
total_votes=0
#print(len(places_votes))
for i in range(len(places_votes)):
    total_votes=total_votes+int(places_votes[i][2])
probs=[float(places_votes[i][2])/total_votes for i in range(len(places_votes))]
ran_num=random.random()
portion=[]
temp=0
for i in range(len(probs)):
    temp=temp+float(probs[i])
    portion.append(temp)
portion=[0]+portion

def less_than_50_result():
	print('*'*40)
	print('Based on the {} votes we get this time'.format(total_votes))
	print('*'*40)
	for i in range(len(probs)):
	    print('Probability for going to {} is {}'.format(places_votes[i][0],probs[i]))
	#print(probs)
	print('*'*40)
	print('Ultimate solution to Lunch places')
	print('*'*40)
	print(r"Let's have lunch in {} this time!!!".format(result))
def more_than_50_result():
	print('*'*40)
	print('Based on the {} votes we get this time'.format(total_votes))
	print('*'*40)
	for i in range(len(probs)):
	    print('Probability for going to {} is {}'.format(places_votes[i][0],probs[i]))
	print('*'*40)
	print("Since the vote for {} is more than 50%, let's follow majority then".format(result))
	print('*'*40)
	print('*'*40)
	print('*Ultimate solution to Lunch places*')
	print('*'*40)
	print(r"Let's have lunch in {} this time!!!".format(result))
#print(probs)
for i in range(len(portion)):
    if probs[i]>0.5:
        result=places_votes[i][0]
        more_than_50_result()
        break
    elif ran_num>portion[i] and ran_num<portion[i+1]:
       result=places_votes[i][0]
       less_than_50_result()
       break
    else:
        continue


