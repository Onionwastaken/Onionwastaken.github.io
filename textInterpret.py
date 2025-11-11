import random as rand
import tk as tk
import pyinput as pinput
comNum   = rand.randint(1,10)
pNum     = int(input("think of a number between one and ten."))
fortunes = ["You will have good fortune today.", "You will have bad fortune today.", "You will soon experience police brutality.", "You will have fair fortune today.", "Your lucky color is yellow today.", "You should've worn a different shirt today.", "You will have a restless night.", "You will come across a large sum of money soon.", "You are not that guy."]
index    = abs(comNum-pNum)
print(fortunes[index])
def openWindow():
    window = tk.Toplevel(root)
    window.title("Window")
    window.geometry("200x300")
    tk.label(window, text="You will accept.").pack(pady=20)
    window.focus_set()

root = tk.Tk()
root.title("Main Window")
root.geometry("400x300")

tk.Button(root, text="Open New Window", command=open_new_window).pack(pady=50)