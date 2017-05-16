class HashMap(object):
    def __init__(self):
        self.size=6
        self.map =[None]*self.size

    def get_hash(self,key):
        hash=0
        for ch in str(key):
            hash+=ord(ch)
        return hash%self.size

    def add(self,key,value):
        hash_k = self.get_hash(key)
        self_val = [key,value]

        if self.map[hash_k] is None:
            self.map[hash_k]= list([self_val])
        else:
            for pair in self.map[hash_k]:
           #     print 'pair',pair
                if pair[0]==key:
                    pair[1]=value
            #        print pair[1]
                    return True
            self.map[hash_k].append(self_val)

    def print1(self):
        for i in self.map:
            if i is not None:
                print str(i)

    def get1(self,key):
        key_hash =self.get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]

        return None
    

h = HashMap()
h.add('Bob', '567-8888')
h.add('Ming', '293-6753')
h.add('Ming', '333-8233')
h.add('Ankit', '293-8625')
h.add('Aditya', '852-6551')
h.add('Alicia', '632-4123')
h.add('Mike', '567-2188')
h.add('Aditya', '777-8888')
h.print1()
print('Ming: ' + h.get1('Ming'))