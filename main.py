# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    tiek izveidots masīvs ar threads, kurš pagaidām ir aizpildīts ar nullēm
    threads = []
    for k in range(n):
        threads.append(0)
    
    k=0
    while k<m:
        #tiek paņemts pirmais threads elements un tiek salīdzināts ar citiem, lai atrastu thread ar mazāko vērtību
        minTime = threads[0]
        index = 0
        l=1
        while l<n:
            if threads[l]<minTime:
                minTime = threads[l]
                index = l
            l+=1

        begin = threads[index]
        threads[index] += data[k]
        output.append((index,begin))
        k+=1
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
    #letter = input()
   
    #if "I" in letter:
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
