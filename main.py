# python3


class Query:
    def __init__(self, query):
        self.type=query[0] 
        self.number=int(query[1])
        if self.type=='add':
            self.name=query[2]

class HashFunction:
    
    def __init__(self,bucket_count):
        self.bucket_count=bucket_count
        self.buckets=[[] for _ in range(bucket_count)]

    def _hash_func(self,s):
        ans=0
        for c in s:
            ans=(ans*128+ord(c))%self.bucket_count
        return ans

    def add(self, query):
        hashed=self._hash_func(str(query.number))
        bucket=self.buckets[hashed]

        for contact in bucket:
            if contact.number==query.number:
                contact.name=query.name
                return

        bucket.append(query)
        

    def find(self,number):
        hashed=self._hash_func(str(number))
        bucket=self.buckets[hashed]

        for contact in bucket:
            if contact.number==number:
                return contact.name
        return "not found"
    
    def delete(self,number):
        hashed=self._hash_func(str(number))
        bucket=self.buckets[hashed]

        for i in range(len(bucket)):
            if bucket[i].number==number:
                bucket.pop(i)
                break


def read_queries():
    n=int(input())
    return [Query(input().split()) for i in range(n)]
def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    # Keep list of all existing (i.e. not deleted yet) contacts.
    result=[]
    contacts=HashFunction(100000)
    for query in queries:
        if query.type=='add':
            contacts.add(query)
        elif query.type=='del':
            contacts.delete(query.number)

        #if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            #for contact in contacts:
                #if contact.number == cur_query.number:
                    #contact.name = cur_query.name
                    #break
            #else: # otherwise, just add it
                #contacts.append(cur_query)
        else:
            response=contacts.find(query.number)
            result.append(response)
    return result

if __name__=='__main__':
    write_responses(process_queries(read_queries()))
