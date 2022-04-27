import random

"""

Question 1

"""

class Card:
    def __init__(self,suit, rank ):
        self.rank = rank
        self.suit = suit
        points_dict = {'Two':2,
                      'Three':3,
                      'Four':4,
                      'Five':5,
                      'Six':6,
                      'Seven':7,
                      'Eight':8,
                      'Nine':9,
                       'Ten':10,
                      'Jack':10,
                      'Queen':10,
                      'King':10,
                      'Ace':11}
        self.points = points_dict[rank]
        
    def __repr__(self):
        return f'{self.rank} of {self.suit} - {self.points}pts'    
        
    def __str__(self):
        return f'{self.rank} of {self.suit} - {self.points}pts'
        
    

class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        ranks = ['Two', 'Three', 'Four',
                 'Five', 'Six', 'Seven',
                 'Eight', 'Nine', 'Ten',
                 'Jack', 'Queen', 'King',
                 'Ace']
        
        self.deck = [Card(s, r) for r in ranks for s in suits]
        
    def pop_cards(self):
        if len(self.deck) > 2:
            random.shuffle(self.deck)
            cards_out = self.deck[0:2]
            self.deck = self.deck[2::]
            return cards_out
        else:
            return []     
         
    
"""

Question 2

"""


class Client:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def get_client(self):
        return f'{self.first_name} {self.last_name} {self.age}'

class BankAccount:
    def __init__(self, first_name, last_name, age, balance=0):
        self.client = Client(first_name, last_name, age)
        self.balance = balance
        
    def deposit(self, Deposit):
        self.balance += Deposit
        
    def withdraw(self, Withdraw):
        if Withdraw <= self.balance:
            self.balance -= Withdraw
        else:
            return 'No funds available!'
            
    def transfer(self, amount, account_to):
        if amount <= self.balance:
            self.balance -= amount
            account_to.deposit(amount)
        else:
            return 'No funds available!'

"""

Question 1

"""

"""
class Card():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        #self.point=point
        self.cards=[]
    
    def __str__(self):
        return '{} {}'.format(self.suit, self.rank)
    
    def points(self):
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
        points=[2,3,4,5,6,7,8,9,10,10,10,10,11]
        for p in points:
            for s in suits:
                if s==self.suit:
                    for r in ranks:
                        if r==self.rank:
                            print(self.rank," of ",self.suit, " - ",p,"pts")
                            
"""  
"""
suits = {'Hearts', 'Diamonds', 'Spades', 'Clubs'}
ranks = {'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace'}
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
                      
            
        
class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
   
    def __str__(self):
        return self.rank + ' of ' + self.suit + ' - '+str(self.value)+'pts'
    
    
    def __str__(self):
        return self.rank+ self.suit, str(self.value)

    
    def points(self):
        return __str__()
        #print(str(self.rank) + ' of ' + str(self.suit) + ' - '+str(self.value)+'pts')
              
           

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        #self.point=point
        
    def __str__(self):
        return self.suit,self.rank
    
    def points(self):
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
        for s in suits:
            for r in ranks:
                return self.rank," of ", self.suit
                
        
    
   
    

class Deck(Card):
    def __init___(self,suit,rank,point):
        super.init(self,suit,rank,point)
        self.deck = [] 
 
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
        print (str(self.deck))
            
    
   
         
card = Card("Spades", "Four")
print(card.points)
#print(card)   

deck1 = Deck("Spades", "Four")

print(str(deck1))
#print(cards[1])


Question 2




class Client():
    
    pass

class BankAccount(Client):
    
    pass
                


Test your functions here
You must comment your tests when submiting your work
"""


# Question 1

"""
card = Card("Spades", "Four")
print(card.points)
print(card)
print("-"*25)

deck1 = Deck()
cards = deck1.pop_cards()
print(cards[0])
print(cards[1])
print("-"*25)

cards = deck1.pop_cards()
print(cards[0])
print(cards[1])
print("-"*25)

deck2 = Deck()
cards = deck2.pop_cards()
print(cards[0])
print(cards[1])
print("-"*25)
"""

# Question 2

"""
c1 = Client("John", "Doe", 30)    
print(c1.get_client())
print("-"*25)

ba1 = BankAccount('John', "Doe", 30, 100)    
print(ba1)       
print("-"*25) 

ba1.deposit(50)
ba1.withdraw(55)
ba1.withdraw(500)
print(ba1)
print("-"*25)

ba2 = BankAccount('Jane', "Doe", 30, 100)  
ba1.transfer(95, ba2)
print(ba1)
print(ba2)
"""