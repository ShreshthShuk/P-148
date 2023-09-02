from tkinter import *
import random

root = Tk()
root.title("Picnic Bag List")
root.geometry("500x500")

list_of_items = Label(root)
random_numbers = Label(root)

list1 = ["Tiffin Box", "Water Bottle", "Bedsheet", "Phone", "Camera","Wallet", "Id Card", "First Aid Box"]
list_of_items["text"] ="Listed Items :" + str(list1)

def RandomNumber():
    numbers = random.sample(range(0,8), 1)
    random_numbers["text"] = "Put Item Number" + str(numbers) + "in bag"

btn = Button(root, text = "Put item", command=RandomNumber, bg = "red", fg = "white")
btn.place(relx = 0.5, rely = 0.6, anchor=CENTER)
    
list_of_items.place(relx = 0.5, rely = 0.5, anchor=CENTER)   
random_numbers.place(relx = 0.5, rely = 0.7, anchor=CENTER)
     
root.mainloop()