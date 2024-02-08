'''
9 8 1 2 3 4 5 3 7
- -             -
may use two heaps

read_heap and rem_heap as follows
on emit: push into read_heap, if read_heap over cap, then pop from it

insert already costs lg n...what if we could update an aux heap

if something expires

this is the main app

parameters: sigmin, sigmax, K, TTL

class level variables
    signal: [signal: int, is_deleted: bool]
    signals: Priority queue of signal
    time: the time we receive a signal
    times : FIFO queue of times
    signal_lookup : dictionary taking a (time,count) to a unique signal 

worker tasks:
           --------               -------------------------        <-- x
    read_heap of size k            rem_heap of size   n-k             signal
          PQ                            PQ
    emit (signal producer): O(lg k) 
        generate random signal
        push into read heap. if read_heap over cap, pop off it into rem_heap
        come back to this later: update lookup so that we can expire it 
    read (signal reader): O(k):
        just report the values in read_heap
    expire: O (1)
        periodically check both PQs, and expire items based on TTL
    gc (signal consumer):
        heapify
        at the same rate we expire, 
    expire and gc are producer and consumer resp. in delete queue
'''