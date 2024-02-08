'''
this is the main app
create a lock

lock queue for consumer

class level variables
    entry_lookup
    times

worker tasks:
    expire:
        could just expire items
        could also expire then notify garbage collector there is work to be done
    gc:
        expire it
    expire and gc are producer and consumer resp. in delete queue

    emit: 
        add item to priority queue
        update lookup so that we can expire it 
    read_k:
        read max K signal values
    emit and read_k tasks are producer and consumer resp in signal queue
'''
def emit()
