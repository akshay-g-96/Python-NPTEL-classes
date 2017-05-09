def tennis():
    data=[]
    while( True ):
        data=input()
        columns=data.split(":")
        score=columns.split(",",2,)
        name[0][0]=columns[1]
        name[0][1]=1
        for i in range (0,len(name)):
            if columns[1] != name[i][0]:
                name[i+1][0]=columns[1]
                name[i+1][1]=1
            else:
                name[i][1]=name[i][1]+1
    for i in range (0,name):
        print(name[i][0],name[i][1])      
            
        
     #   try:
      #      for i in range (0,6):
                
            
        
   
    
