# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    #tiek izveidots masīvs ar threads, kurš pagaidām ir aizpildīts ar nullēm. tas tiek izmantots, lai 
    # atrastu thread, kurš ātrāk beigs darbu
    threads = []
    for a in range(n):
        threads.append(0)
    #masīvs, lai saglabātu katra thread darba sākumu
    beginTime = []
    for b in range(m):
        beginTime.append(0)
    #masīvs, lai saglabātu katra thread indeksu
    threadIndex = []
    for c in range(m):
        threadIndex.append(0)
    
    k=0
    while k<m:
        #tiek paņemts pirmais threads elements un tiek salīdzināts ar citiem, lai atrastu thread ar mazāko laiku
        minTime = threads[0]
        index = 0
        l=1
        while l<n:
            if threads[l]<minTime:
                minTime = threads[l]
                index = l
            l+=1
        #beginTime masīvā tiek saglabāta threads vērtība, kura atbilst thread darba sākumam
        beginTime[k] = threads[index]
        #threadIndex masīvā tiek saglabāts thread indekss, kurš šobrīd veic darbu
        threadIndex[k] = index
        #attiecīgā thread laiks tiek palielināts par tik, cik ilgs ir pildāmais darbs
        threads[index] += data[k]
        k+=1
    #tiek aizpildīts output masīvs ar thread indeksiem un darbu izpildes laikiem attiecīgā secībā
    for i in range(m):
        output.append((threadIndex[i],beginTime[i]))
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []
    
    n, m = map(int, input().split())
    assert n>=1
    assert n<=105
    assert m>=1
    assert m<=105 
    data = list(map(int, input().split())) 
    assert len(data) == m
    for i in range(m):
        assert data[i]>=0
        assert data[i]<=109
    
    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i in range(len(result)):
        print(result[i][0],result[i][1])


if __name__ == "__main__":
    main()
