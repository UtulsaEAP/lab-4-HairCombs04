"""
Name: Bradyn Combs
Lab Time: 2/22/24 2:00 PM
"""

def feet_to_steps(user_feet):
   #write your code here
   steps_walked = user_feet // 2.5
   return round(steps_walked)

if __name__ == '__main__':
    #take input feet steps here
    #store it into the function
    
    #print your steps here
    input_feet = float(input())
    steps_walked = feet_to_steps(input_feet)
    print(steps_walked)