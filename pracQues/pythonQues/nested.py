if __name__ == '__main__':
    small=1000
    name=[]
    score=[]
    n=int(input())
    for i in range(n):
        name[i].append(input())
        score[i].append(float(input()))
        if(score[i]<small):
            small=score
    print(small)
  #  for _ in range (len)
        
        