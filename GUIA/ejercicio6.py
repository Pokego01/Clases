S=0
M=0
H=0
while H!=23:
    print(H,M,S)
    H=H+int(M/59)
    if M==59:
        M=0
    while M!=59:
        print(H,M,S)
        M=M+int(S/59)
        if S==59:
            S=0
        while S!=59:
            print(H,M,S+1)
            S=S+1
