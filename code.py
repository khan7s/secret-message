#backword of english alphabets like:- hello world is coded as svool dliow

msg = input().lower()

eng = [chr(i).lower() for i in range(65,91)]    
d = {' ':' '}      
for i in range(0,len(eng)):
    d[eng[i]] = eng[-(i+1)]
   
output = ''
for w in msg:
    output +=d[w]
print(output)
