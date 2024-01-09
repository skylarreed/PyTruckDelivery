class ChainingHashTable:
    # Constructor with optional initial size parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_size=10):
        self.table = [[] for _ in range(initial_size)]

    # Inserts a new item into the hashtable.
    def insert(self, item):
        # get the bucket list where this item will go.
        bucket = hash(item) % len(self.table)
        bucket_list = self.table[bucket]

        # insert the item to the end of the bucket list.
        bucket_list.append(item)

    # Searches for an item with matching key in the hashtable.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list.
        if key in bucket_list:
            # find the item's index and return the item that is in the bucket list.
            item_index = bucket_list.index(key)
            return bucket_list[item_index]
        else:
            # the key is not found.
            return None

    # Removes an item with matching key from the hashtable.
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        if key in bucket_list:
            bucket_list.remove(key)

    # Returns a string representation of the hashtable.
    def __str__(self):
        return str(self.table)

    # Returns the number of slots in the table.
    def __len__(self):
        return len(self.table)

    # Returns an iterator for traversing the hashtable.
    def __iter__(self):
        return iter(self.table)

    # Returns an iterator for traversing the keys in the hashtable.
    def keys(self):
        for bucket_list in self.table:
            for key in bucket_list:
                yield key

    # Returns an iterator for traversing the values in the hashtable.
    def values(self):
        for bucket_list in self.table:
            for key in bucket_list:
                yield key