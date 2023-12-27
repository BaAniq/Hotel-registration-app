from tkinter import *

beige = '#FAF6F0'


# creating a  main window

main_window = Tk()
main_window.minsize(width=300, height=200)
main_window.title('Hotel registration')
main_window.config(bg=beige)

canvas_bg = Canvas(width=189, height=266, bg=beige, highlightthickness=0)
image = PhotoImage(file='hotel.png')
canvas_bg.create_image(94, 133, image=image)

canvas_bg.grid(column=1, row=1, rowspan=3)



def show_menu():
    def menu_list_box_used(event):
        print(menu_listbox.get(menu_listbox.curselection()))
    menu_listbox = Listbox(height=4)
    menu_elements = ["Show the Guest List", "Check in guest", "Check out guest", "Edit data"]
    for element in menu_elements:
        menu_listbox.insert(menu_elements.index(element), element)
    menu_listbox.bind("<<ListboxSelect>>", menu_list_box_used)
    menu_listbox.grid(column=3, row=2)


show_menu()

main_window.mainloop()