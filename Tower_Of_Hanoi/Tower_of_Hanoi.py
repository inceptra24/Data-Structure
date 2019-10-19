# ToH using Recursive method
def TowerofHanoi(n , pl1, pl2, plmiddle): 
    if n == 1: 
        print "Move disk 1 from rod",pl1,"to rod",pl2 
        return
    TowerofHanoi(n-1, pl1, plmiddle, pl2) 
    print "Move disk",n,"from rod",pl1,"to rod",pl2 
    TowerofHanoi(n-1, plmiddle, pl2, pl1) 
          
# Main
n = 4
TowerofHanoi(n, \'A\', \'C\', \'B\') 
