import os

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

print(r'''
    
                            :**+-:.                                                       
                           :********=:                                                    
                           .:+*********+=-:                                               
                            .+###***********+=-.                                          
                          .***########**********.                                         
                          ********########*****:                                          
                         +*************####: ..                                           
                        +******************-                                              
                       -*******************+                                              
                      :*******************#*.                                             
                      +******************#####+=-.                                        
                   .  =###**************###########+-                                     
                 .*****########********#=.:=*#########*+=:                                
                 +**********########**--      :=+*#########*=-:                           
                  .-=+***********###:             .:=*##########*+-.                      
                       :-+**********+:                .-=*###########*=:                  
                           :-=+******+                    .-+*###########+=:.             
                                :-=++                          :-+############+=:         
          .:::::::::::::::::::::::::::::::.                        :+*############*=-.    
      .:-=#################################=-:                         :=*############*:  
    .*#########################################-                           :-+*########*  
    +###########################################                               .:=*###*:  
     ...........................................                                    .     
    
''')
print('Welcome to the secret auction program.')
continue_bid = True
highest_bidder = {
    "name": "",
    "bid": 0.0
}
while continue_bid:
    name = input('What is your name? ')
    bid = float(input('What is your bid?: $'))
    if highest_bidder["bid"] < bid:
        highest_bidder['name'] = name
        highest_bidder['bid'] = bid
    continue_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n") == 'yes'
    clear()
print(f"The winner is {highest_bidder['name']} with a bid of ${highest_bidder['bid']:.2f}")