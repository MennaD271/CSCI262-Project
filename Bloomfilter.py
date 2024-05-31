import hashlib

class Bloomfilter:
    def __init__(self):
        self.size = 1000
        self.num_of_hashes = 15
        
    def hash(self, password: str):
        hashes = []
        password = password.encode()
        for i in range(self.num_of_hashes):
            g = hashlib.md5()
            h = hashlib.sha256()
            g.update(password)
            h.update(password)
             
            hash = (int(g.hexdigest(), base=16) + i * int(h.hexdigest(), base=16)) % self.size
            hashes.append(hash)
        return hashes
    
    def train_filter(self,file):
        file = open('rockyou.txt', 'r')
        passwords = file.readlines()  
    
    def test(self,newpassword):
        return True
    
#Testing
a = Bloomfilter()
b = input("Enter string: ")
print(a.hash(b))