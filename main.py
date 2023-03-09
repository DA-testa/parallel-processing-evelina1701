# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    threads = []
    for k in range(n):
        threads.append(0)
    
    k=0
    l=1
    while k<m:
        minTime = threads[0]
        index = 0
        while l<n:
            if threads[l]<minTime:
                minTime = threads[l]
                index = l
            l+=1
        k+=1

    begin = treads[index]
    threads[index] += data[i]
    output.append((index,begin))

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
    letter = input()
   
    if "I" in letter:
        n = int(input())
        assert n>=1
        assert n<=105
        m = int(input())
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
    for i in range(result):
        print(result[i],"\n")


if __name__ == "__main__":
    main()
