def find_it(seq):
    seq.sort()
    seq_clean = []
    
    for n in range(0,len(seq)):
        if seq[n] != seq[n-1]:
            seq_clean.append(seq[n])
    print(seq)
    print(seq_clean)
    return None

find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])