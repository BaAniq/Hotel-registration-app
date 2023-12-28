from tkinter import *

beige = '#FAF6F0'
menu_listbox = None
labels_to_delete = None

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
    global menu_listbox, labels_to_delete
    menu_listbox = Listbox(height=4)
    menu_elements = ["Show the Guest List", "Check in guest", "Check out guest", "Edit data"]
    for element in menu_elements:
        menu_listbox.insert(menu_elements.index(element), element)
    menu_listbox.bind("<<ListboxSelect>>", menu_list_box_used)
    menu_listbox.grid(column=3, row=2)
    labels_to_delete = [menu_listbox]

def menu_list_box_used(event):
    global menu_listbox
    choice = menu_listbox.get(menu_listbox.curselection())
    if choice == "Show the Guest List":
        pass
    elif choice == "Check in guest":
        check_in_guest()
def check_in_guest():
    destroy_view()
    name_label = Label(text='Name', font=('Calibre', 10), bg=beige, padx=3)
    name_label.grid(column=2, row=1)

    name_textbox = Entry(width=8)
    name_textbox.grid(column=3, row=1)
def destroy_view():
    global labels_to_delete
    for label in labels_to_delete:
        label.destroy()

show_menu()

main_window.mainloop()