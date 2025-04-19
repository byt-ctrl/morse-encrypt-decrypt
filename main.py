# MORSE CODE ENCRYPTION AND DECRYPTION WITH GUI

import tkinter as tk  # for GUI
from tkinter import messagebox # for displaying message-box

#   Morse code dictionary
#   this dictionary maps alphanumeric and some punctuation chracters to morse code
morse_code_dict={
    'A':'.-',        'B':'-...',      'C':'-.-.',        'D':'-..',    'E':'.',
    'F':'..-.',      'G':'--.',       'H':'....',        'I':'..',     'J':'.---',
    'K':'-.-',       'L':'.-..',      'M':'--',          'N':'-.',     'O':'---',
    'P':'.--.',      'Q':'--.-',      'R':'.-.',         'S':'...',    'T':'-',
    'U':'..-',       'V':'...-',      'W':'.--',         'X':'-..-',   'Y':'-.--',
    'Z':'--..',

    '0':'-----',     '1':'.----',     '2':'..---',       '3':'...--',  '4':'....-',
    '5':'.....',     '6':'-....',     '7':'--...',       '8':'---..',  '9':'----.',

    '.':'.-.-.-',    ',':'--..--',    '?':'..--..',      "'":'.----.', '!':'-.-.--',
    '/':'-..-.',     '(':'-.--.',     ')':'-.--.-',      '&':'.-...',  ':':'---...',
    ';':'-.-.-.',    '=':'-...-',     '+':'.-.-.',       '-':'-....-', '_':'..--.-',
    '"':'.-..-.',    '$':'...-..-', '@':'.--.-.',      ' ':'/'
}

# reserving dictionary for decoding morse code back to chr
reverse_morse_code_dict={v:k for k,v in morse_code_dict.items()}

# for encrption a plain message into morse code 
def encrypt(message) :
    encrypted=''
    for char in message :
        upper_char=char.upper()  #convert to uppercase since morse dict has uppercase letters

        if upper_char in morse_code_dict :
            encrypted+=morse_code_dict[upper_char]+' '
        else: 
            encrypted+=f'[{char}] '  # preserve unknown/special characters by wrapping 
    return encrypted.strip()

# decrypt a morse messgage back to plain text
def decrypt(message) :
    words=message.strip().split(' / ')  # split morse by word using slashes
    decoded=[]
    for word in words :
        letters=word.strip().split()
        decoded_word=''
        for token in letters :
            if token.startswith('[') and token.endswith(']') :
                #  if wrapped , it's a preserved secial chr
                decoded_word+=token[1:-1]
            else :
                decoded_word+=reverse_morse_code_dict.get(token,'<?>')  # unknown morse code
        decoded.append(decoded_word)
    return ' '.join(decoded)


""" setting up the GUI """
def create_gui() :
    def encode_text() :
        msg = input_text.get("1.0",tk.END).strip()
        if not msg :
            messagebox.showwarning("Input Error","Please enter text to encode.")
            return
        result=encrypt(msg)
        output_text.delete("1.0",tk.END)
        output_text.insert(tk.END,result)

    def decode_text() :
        msg=input_text.get("1.0",tk.END).strip()
        if not msg :
            messagebox.showwarning("Input Error","Please enter Morse code to decode.")
            return
        result=decrypt(msg)
        output_text.delete("1.0",tk.END)
        output_text.insert(tk.END,result)

    def clear_text() :
        input_text.delete("1.0",tk.END)
        output_text.delete("1.0",tk.END)

    root=tk.Tk()
    root.title(" Morse Code Encryptor/Decoder ")
    root.geometry("600x450")
    root.config(bg="lightgray")

    # input label + text
    tk.Label(root,text="Enter Text or Morse Code :",font=("Arial",15),bg="lightgray").pack(pady=6)
    global input_text
    input_text=tk.Text(root,height=5,width=70,font=("Courier",13))
    input_text.pack(pady=5)

    # buttons
    tk.Button(root,text="Encrypt to Morse",command=encode_text,bg="blue",fg="white",width=20).pack(pady=5)
    tk.Button(root,text="Decrypt to Text",command=decode_text,bg="green",fg="white",width=20).pack(pady=5)
    tk.Button(root,text="Clear",command=clear_text,bg="red",fg="white",width=10).pack(pady=5)

    # output label + text
    tk.Label(root,text="Output :",font=("Arial",15),bg="lightgray").pack(pady=5)
    global output_text
    output_text=tk.Text(root,height=5,width=70,font=("Courier",13))
    output_text.pack(pady=5)
    root.mainloop()

create_gui()

# END 
