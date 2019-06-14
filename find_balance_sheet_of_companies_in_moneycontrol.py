
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
list_1=['2M','21C','I11','MI42','PI36','C98']
i = 0
#while i < len(list_1):
query = "balance sheet moneycontrol"
for j in search(query, tld="co.in", num=4, stop=1, pause=2): 
        print(j) 
    
