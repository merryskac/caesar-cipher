from tkinter import *
from chipp import encrypts, decrypts

root = Tk()
root.title("Caesar Cipher")

main_label = Label(root,text="Caesar Cipher",font=30, padx=10,pady=20)
main_label.grid(row=0,column=0, columnspan=2)

input_word_label = Label(root,text="Masukkan kata/kalimat", anchor='e')
input_word_label.grid(row=1,column=0,padx=10, sticky=W+E)
input_word_box = Entry(root, width = 50)
input_word_box.grid(row = 1, column=1,padx=10)

input_num_label = Label(root,text="(Required) Key (1-26)",anchor='e')
input_num_label.grid(row=2,column=0,padx=10, sticky=W+E)
input_num_box = Entry(root, width = 50)
input_num_box.grid(row =2, column=1,padx=10)

input_trans_label = Label(root,text="Translate", anchor='e')
input_trans_label.grid(row=3,column=0,pady=(0,10),padx=10, sticky=W+E)
input_trans_box = Entry(root, width = 50)
input_trans_box.grid(row =3, column=1,pady=(0,10))

def encrypt():
    global e
    word = input_word_box.get()
    key = input_num_box.get()
    enkripsi = encrypts(word,key)
    input_trans_box.configure(state='normal')
    input_trans_box.delete(0,END)
    input_trans_box.insert(0,enkripsi)
    input_trans_box.configure(state='disabled')

def decrypt():
    # e=input_trans_box.get()
    # input_word_box.delete(0,END)
    # input_word_box.insert(0,e)
    word = input_word_box.get()
    key = input_num_box.get()
    dekripsi = decrypts(word,key)
    input_trans_box.configure(state='normal')
    input_trans_box.delete(0,END)
    input_trans_box.insert(0,dekripsi)
    input_trans_box.configure(state='disabled')

def reset():
    input_trans_box.delete(0,END)
    input_word_box.delete(0,END)
    input_num_box.delete(0,END)

encrypt_button = Button(root,text='Encrypt', command=encrypt)
encrypt_button.grid(row=4,column=0,pady=(0,10),padx=20, columnspan=2, sticky=W+E)
decrypt_button = Button(root,text='Decrypt', command=decrypt)
decrypt_button.grid(row=5,column=0,pady=(0,10),padx=20, columnspan=2, sticky=W+E)
reset = Button(root,text="reset", command=reset)
reset.grid(row=6, column=1, sticky=W+E, padx=20, pady=(0,10))
exit=Button(root,text="Exit",background='red',command=root.destroy)
exit.grid(row=6, column=0,sticky=W+E, padx=20, pady=(0,10))

nama = Label(root, text='Merryska C / F55120034', relief=SUNKEN, anchor='e')
nama.grid(row=7, sticky=W+E, columnspan=2,pady=(5,0))

root.mainloop()