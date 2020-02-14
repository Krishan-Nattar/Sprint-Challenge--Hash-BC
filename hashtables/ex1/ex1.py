#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    for i in range(length):\
        # Difference is the value we need to equal the weight limit
        difference = limit - weights[i]

        # Check if a key with the value of difference exists in the hash table
        # If it does, then we have 2 matching items, so we sort them and return them in a tuple
        if hash_table_retrieve(ht, difference) is not None:

            if hash_table_retrieve(ht, difference) > i:
                return (hash_table_retrieve(ht, difference), i)
            else:
                return (i, hash_table_retrieve(ht, difference))

        # Store the weight as a key, store the index as a value
        hash_table_insert(ht, weights[i], i)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
