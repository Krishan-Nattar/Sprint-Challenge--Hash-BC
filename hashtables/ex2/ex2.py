#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length -1)
    count = 0


    """
    YOUR CODE HERE
    """

    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
        while True:
            # If the current ticket item has a source of "NONE", then we set it to the first index, because it is the start of the flight
            if tickets[i].source == "NONE" and route[0] == None:
                route[count] = tickets[i].destination
                count += 1

            # If we have already placed the first ticket, check to see if matchin routes exist in our hash table
            if i > 0 and count <= i and count > 0:
                # See if there is a matching source key to the last destination in the route
                destination = hash_table_retrieve(hashtable, route[count-1])

                # If there is a matching source key with a destination that is NOT the last flight, add that destination
                if destination != "NONE" and destination != None:
                    route[count] = destination
                    count += 1
                # If we can't find a matching key or we're on the last flight, break out of the loop
                else:
                    break
            else:
                # If we still haven't placed the first flight or we have placed ALL the flights, break the while loop
                break
    
    # Set very last array item to "NONE" to match test cases

    return route


            




    return route
