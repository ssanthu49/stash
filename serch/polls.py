polls=['abc','def','ghi','jkl','mno','pqr','stu','vwx','yz1','abc','def','ghi','abc','def','ghi','abc','def']

candidates=[]

votes=[]

for person in polls:
    if person not in candidates:
        candidates.append(person)
        votes.append(1)
    else :
        candidate_index=candidates.index(person)
        votes[candidate_index]+=1
max_vote=0
max_candidates=[]
for i in range(len(votes)):
    if votes[i]>max_vote:
        max_vote=votes[i]
        candidate=candidates[i]
        max_candidates=[]
        max_candidates.append(candidate)
    elif votes[i]==max_vote:
        candidate=candidates[i]
        max_candidates.append(candidate)
print('The higest vote goes to: ')
print(*max_candidates, sep='\n')
print('Each person has'+str(max_vote)+'Votes.')
    