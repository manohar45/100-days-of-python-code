alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caeser(text,shift,direction):
    new_text=""
    for i in text:
        index=alphabet.index(i)
        if(direction=='encode'):
            new_index=(index+shift)%len(alphabet)
        elif(direction=='decode'):
            new_index=(index-shift)%len(alphabet)
        new_text=new_text+alphabet[new_index]
    print(f"The {direction} text is {new_text}")

flag=True
while flag:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(text,shift,direction)
    val=input("Type 'yes' to continue or 'no' to stop further !\n")
    if(val=='no'):
        flag=False

