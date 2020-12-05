#checksum calculation

bin1=bin(int(input("Enter the first no:")))
bin2=bin(int(input("Enter the second no:")))
print("Entered data:",bin1,bin2)

def send():
    sum = bin(int(bin1,2) + int(bin2,2))

    if (len(bin1) == len(sum) or len(bin2) == len(sum)):
        print("No Carry Generated!")
        final=sum
    else:
        print("Carry Generated, Adding Bit")
        sum_2=sum.split('0b1')
        sum_pre_final=sum_2[1]
        final=bin(int(sum_pre_final,2)+int('1',2))
    
    xor_value=bin(15)
    checksum=bin(int(final,2)^int(xor_value,2))
    print("Checksum Value",checksum)

def recieve(d1,d2,checksum):
    bin1=d1
    bin2=d2
    sum = bin(int(bin1,2) + int(bin2,2))
    if (len(bin1) == len(sum) or len(bin2) == len(sum)):
        print("No carry")
        final=sum
    else:
        print("Carry Generated, Adding bit")
        sum_2=sum.split('0b1')
        sum_pre_final=sum_2[1]
        final=bin(int(sum_pre_final,2)+int('1',2))
    
    xor_value=bin(15)
    checksum_add=bin(int(final,2)+int(checksum,2))
    checksum_add=bin(int(checksum_add,2)^int(xor_value,2))
    if checksum_add=='0b0':
        print("Checksum verified, No errors!")
    else:
        print("Checksum Not verified! Message Corrupted!")

while True:
    print("\n\nCheck-sum 'CHECKSUM'")
    choice=int(input("1. Send \n2. Recieve \n3. Exit \nEnter Your choice:"))
    if choice==1:
        send()
    elif choice==2:
        val1=bin(int(input("Enter the first no:")))
        val2=bin(int(input("Enter the second no:")))
        checksum=bin(int(input("Enter the checksum value:")))
        recieve(val1,val2,checksum)
    elif choice==3:
        exit()
