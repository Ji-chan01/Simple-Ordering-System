import tkinter as tk
from tkinter import ttk, messagebox
import widget
import product


# Class for the first window
class MainDoor(tk.Tk):
    def __init__(self, title, size):
        super().__init__()

        # Setting up the first window
        self.title(title)
        self.resizable(False, False)
        self.geometry(f'{size[0]}x{size[1]}')
        self.configure(bg='#E8EAED')
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure('Text.TButton', font=('Courier New', 15), padding=(1, 1, 1, 1))

        # Calling the methods to automatically call the method
        self.create_frames()
        self.create_widgets()

        # Creating a mainloop to execute the program
        self.mainloop()

    # Creating frame for the first window
    def create_frames(self):
        self.frame1 = widget.BaseFrame(self, 480, 209, 10, 10)

    # Creating widgets for the first window
    def create_widgets(self):
        widget.LabelWidget(self.frame1, text='GearMasters', font=('Helvetica', 30, 'bold', 'italic'), pos=(100, 5))
        widget.LabelWidget(self.frame1, text='Motorsports', font=('Helvetica', 30, 'bold', 'italic'), pos=(105, 44))
        widget.LabelWidget(self.frame1, text='®', font=('Helvetica', 20, 'bold', 'italic'), pos=(340, 44))
        widget.LabelWidget(self.frame1, text='PARTS AND ACCESSORIES', font=('Times New Roman', 10), pos=(143, 89))
        widget.ButtonWidget(self.frame1, text='SHOP NOW', command=self.lists, style='Text.TButton', x=154, y=140)

    # A command which redirects window 2 when the button is clicked
    def lists(self):
        Products(self, 'GearMaster Motorsports', (548,306))
        self.withdraw()


# Class for the second window
class Products(tk.Toplevel):
    def __init__(self, root, title, size):
        super().__init__(root)

        # Setting up the second window
        self.title(title)
        self.resizable(False, False)
        self.geometry(f'{size[0]}x{size[1]}')
        self.configure(bg='#E8EAED')
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.frame = widget.BaseFrame(self, 538, 295, 5, 5)

        # Displaying the treeview lists
        self.treeview = product.ProductsTreeview(self.frame)
        self.treeview.list_of_products()

        # Setting up the scrollbar widget
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.treeview.yview)
        scrollbar.place(x=514, y=85, height=201)
        self.treeview.config(yscrollcommand=scrollbar.set)

        widget.LabelWidget(self.frame, text='UNLEASH YOUR RIDE\'S POTENTIAL WITH SUPERIOR MOTORSPORT', font=('Courier New', 9, 'bold'), pos=(50, 1))
        widget.LabelWidget(self.frame, text='PARTS AND ACCESSORIES!', font=('Courier New', 9, 'bold'), pos=(155, 17))
        widget.OrdinaryButtonWidget(self.frame, text='Back', font=('Helvetica', 10, 'bold'), command=self.back_button,padx=0, x=1, y=1)
        widget.OrdinaryButtonWidget(self.frame, text='Order Now', font=('Helvetica', 10, 'bold'), command=self.order_button,padx=0, x=440, y=1)

    def back_button(self):
        self.destroy()
        MainDoor('GearMasters MotorSports', (500, 229))

    def order_button(self):
        MainApp('GearMasters MotorSports', (600, 215))


# Class for the main window
class MainWindow(tk.Tk):
    def __init__(self, title, size):
        super().__init__()

        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure('Accent.TButton', font=('Arial', 9), padding=(1, 1, 1, 1))
        self.resizable(False, False)

    def clear_table(self, table):
        for data in table.get_children():
            table.delete(data)

    def add_item(self, values, table):
        table.insert("",tk.END, values=(values[0],values[1], values[2], values[3]))


class MainApp(MainWindow):
    def __init__(self, title, size):
        super().__init__(title, size)
        # Empty array for saving temporary datas
        self.__products = []
        self.__product_names = []

        # Creating 2 frames for the main window
        self.frame1 = widget.BaseFrame(self, 300, 195, 10, 10)
        self.frame2 = widget.BaseFrame(self, 270, 195, 320, 10)

        # Label widgets for main window
        widget.LabelWidget(self.frame1, text='GEARMASTERS MOTORSPORTS ®', font=('Arial', 8, 'bold'), pos=(5, 5))
        widget.LabelWidget(self.frame1, text='Quantity:', font=('Times New Roman', 12), pos=(10, 105))
        widget.LabelWidget(self.frame2, text='TOTAL PURCHASE:', font=('Arial', 9, 'bold'), pos=(1, 158))
        widget.LabelWidget(self.frame2, text='₱', font=('Arial', 11, 'bold'), pos=(163, 157))

        # Entry widget for placing items
        self.entry_items = widget.EntryWidget(self.frame1, fg='gray', width=20, font=('Arial', 12), pos=(10, 40))
        self.entry_placeholder = 'Add items here'
        self.entry_items.insert(0, self.entry_placeholder)

        # Creating instance for MainTreeview class
        self.treeview = MainTreeview(self.frame2)

        # Entry widget for number of quantities
        self.counter_quantity = 0
        self.entry_quantity = widget.EntryWidget(self.frame1, disabledbackground='black', disabledforeground='white',
                                                 width=3, font=('Arial', 10, 'bold'), pos=(70, 107))
        self.entry_quantity.insert(0, self.counter_quantity)
        self.entry_quantity['state'] = 'disable'

        # Entry widget for total price
        self.total_entry = widget.EntryWidget(self.frame2, fg='gray', width=7, font=('Arial', 12, 'bold'),
                                              pos=(180, 156))
        self.total_entry.insert(0, 0)
        self.total_entry['state'] = 'disable'
        self.total_entry['disabledbackground'] = 'black'
        self.total_entry['disabledforeground'] = 'white'

        # Button widgets for adding, removing, resetting items
        widget.ButtonWidget(self.frame1, text='ADD', command=self.add_button, style='Accent.TButton', x=10, y=70)
        widget.ButtonWidget(self.frame1, text='REMOVE', command=self.remove_button, style='Accent.TButton', x=100, y=70)
        widget.ButtonWidget(self.frame1, text='RESET', command=self.reset_button, style='Accent.TButton', x=190, y=70)

        # Button widgets for adding/subtracting quantity
        widget.OrdinaryButtonWidget(self.frame1, text='+', command=self.quantity_add, font=('Arial', 8, 'bold'), padx=3,
                                    x=98, y=105)
        widget.OrdinaryButtonWidget(self.frame1, text='-', command=self.quantity_subtract, font=('Arial', 8, 'bold'),
                                    padx=3, x=121, y=105)

        # An attribute to check if the input items matched
        self.available_products = {'air filter': [self.entry_quantity.get(), 705],
                                   'axle': [self.entry_quantity.get(), 1700],
                                   'back tire': [self.entry_quantity.get(), 730],
                                   'battery': [self.entry_quantity.get(), 1020],
                                   'brake pedal': [self.entry_quantity.get(), 70],
                                   'carburetor': [self.entry_quantity.get(), 770],
                                   'chain': [self.entry_quantity.get(), 350],
                                   'clutch lever': [self.entry_quantity.get(), 100],
                                   'connecting rod': [self.entry_quantity.get(), 320],
                                   'disk brake': [self.entry_quantity.get(), 1210],
                                   'drum brake': [self.entry_quantity.get(), 2000],
                                   'exhaust pipe': [self.entry_quantity.get(), 2500],
                                   'frame': [self.entry_quantity.get(), 930],
                                   'front brake lever': [self.entry_quantity.get(), 200],
                                   'front fender': [self.entry_quantity.get(), 450],
                                   'front tire': [self.entry_quantity.get(), 550],
                                   'fuel tank': [self.entry_quantity.get(), 2000],
                                   'gear shift': [self.entry_quantity.get(), 132],
                                   'handle bar': [self.entry_quantity.get(), 600],
                                   'headlight': [self.entry_quantity.get(), 475],
                                   'horn': [self.entry_quantity.get(), 486],
                                   'ignition switch': [self.entry_quantity.get(), 116],
                                   'indicator': [self.entry_quantity.get(), 50],
                                   'inner tube': [self.entry_quantity.get(), 200],
                                   'pillion': [self.entry_quantity.get(), 354],
                                   'mudguard': [self.entry_quantity.get(), 100],
                                   'rearview mirror': [self.entry_quantity.get(), 200],
                                   'seat': [self.entry_quantity.get(), 100],
                                   'spark plug': [self.entry_quantity.get(), 115],
                                   'speedometer': [self.entry_quantity.get(), 500],
                                   'sprocket': [self.entry_quantity.get(), 580],
                                   'shock absorber': [self.entry_quantity.get(), 829],
                                   'signal light': [self.entry_quantity.get(), 110],
                                   'spokes': [self.entry_quantity.get(), 220],
                                   'tail light': [self.entry_quantity.get(), 250],
                                   'wheel': [self.entry_quantity.get(), 1500],
                                   'windscreen': [self.entry_quantity.get(), 500]}

        # Binding sets to focus in
        self.entry_items.bind('<FocusIn>', self.on_entry_focus_in)
        self.treeview.bind("<Double-Button-1>", self.treeview_double_click)

    def add_button(self):
        self.quantity = int(self.entry_quantity.return_value())
        self.entered_product = self.entry_items.return_value().lower().strip()
        if self.entered_product and self.counter_quantity != 0 and self.entered_product != self.entry_placeholder:
            if self.entered_product in self.available_products:
                product_name = self.entered_product
                self.__products.append({'Product': product_name, 'Quantity': self.quantity, 'Price': self.price()})
                self.treeview.insert('', 'end', values=(self.entered_product.title(), self.quantity, self.price()))
                self.entry_items.delete(0, tk.END)
                self.entry_quantity['state'] = 'normal'
                self.counter_quantity = 0
                self.entry_quantity.delete(0, tk.END)
                self.entry_quantity.insert(0, self.counter_quantity)
                self.entry_quantity['state'] = 'disable'
            else:
                messagebox.showerror('Unavailable item', f'No item called "{self.entered_product}" in the database')
        else:
            messagebox.showerror('No entries', 'Put an entry and quantity first')
        self.total()

    def on_entry_focus_in(self, event):
        if self.entry_items.get() == self.entry_placeholder:
            self.entry_items.delete(0, tk.END)
            self.entry_items.config(fg='black')

    def treeview_double_click(self, event):
        self.click_count = 1
        item = self.treeview.selection()
        self.click_count += 1
        print(self.click_count)
        if item and self.click_count >= 2:
            self.custom_messagebox()
            self.click_count = 1
        print(self.click_count)

    def custom_messagebox(self):
        self.custom_message = tk.Toplevel(self)
        self.custom_message.title('Update')
        self.custom_message.geometry('230x150')
        self.frame3 = widget.BaseFrame(self.custom_message, width=220, height=140, x=5,y=5)
        widget.LabelWidget(self.frame3, 'Quantity:', ('Times New Roman', 15), (5, 20))
        self.entry_toplevel = widget.EntryWidget(self.frame3, pos=(83, 20), width=3, font=('Arial', 15))
        if self.treeview.selection():
            quantity = int(self.treeview.item(self.treeview.selection(), 'values')[1])
            self.entry_toplevel.insert(0, quantity)
        self.style.configure('Link.TButton', font=('Arial', 10), padding=(1, 1, 1, 1))
        widget.OrdinaryButtonWidget(self.frame3, '+', self.update_quantity_add, ('Arial', 14), 4, 125,15)
        widget.OrdinaryButtonWidget(self.frame3, '-', self.update_quantity_subtract, ('Arial', 14), 5, 162, 15)
        widget.ButtonWidget(self.frame3, 'SAVE', self.update_save_button,'Link.TButton', 60, 85)

    def remove_button(self):
        selection = self.treeview.selection()
        if selection:
            self.treeview.delete(selection)
        else:
            messagebox.showerror('NO SELECTION', 'Select item first')
        self.removed_total()

    def removed_total(self):
        total_price = sum(int(self.treeview.item(i, 'values')[2]) for i in self.treeview.get_children())
        self.total_entry['state'] = 'normal'
        self.total_entry.delete(0, tk.END)
        self.total_entry.insert(0, total_price)
        self.total_entry['state'] = 'disabled'

    def reset_button(self):
        confirm = messagebox.askyesno('Are you sure?', 'Are you sure you want to delete all products?')
        if self.treeview.size == 0:
            messagebox.showerror('Place an entry first', 'No items')
        elif confirm:
            self.treeview.delete(*self.treeview.get_children())
            self.__products = []
            self.total()

    def quantity_add(self):
        if self.entry_items.get() and self.entry_items.get() != self.entry_placeholder:
            self.entry_quantity['state'] = 'normal'
            self.entry_quantity.delete(0, tk.END)
            res = self.counter_quantity + 1
            self.entry_quantity.insert(0, res)
            self.counter_quantity = res
            self.entry_quantity['state'] = 'disable'

    def quantity_subtract(self):
        self.entry_quantity['state'] = 'normal'
        if self.counter_quantity != 0:
            self.entry_quantity.delete(0, tk.END)
            res = self.counter_quantity - 1
            self.entry_quantity.insert(0, res)
            self.counter_quantity = res
        self.entry_quantity['state'] = 'disable'

    def update_quantity_add(self):
        self.entry_toplevel.insert(0, 0)
        self.entry_toplevel.delete(0, tk.END)
        res = self.quantity + 1
        self.entry_toplevel.insert(0, res)
        self.quantity = res

    def update_quantity_subtract(self):
        if self.quantity > 0:
            self.entry_toplevel.insert(0, 0)
            self.entry_toplevel.delete(0, tk.END)
            res = self.quantity - 1
            self.entry_toplevel.insert(0, res)
            self.quantity = res

    def update_save_button(self):
        selected_item = self.treeview.selection()
        self.quantity_new = int(self.entry_toplevel.return_value())
        if selected_item:
            product_name = self.treeview.item(selected_item, 'values')[0]
            self.remove_button()
            self.__product_names.append(product_name)
            product_names = self.__product_names[0]
            for product in self.__products:
                if product['Product'] == product_name:
                    product['Quantity'] == self.quantity_new
                    product['Price'] == self.price()
            self.__products.append({'Product': product_names, 'Quantity': self.quantity_new, 'Price': self.price()})
            self.treeview.insert('', 'end',values=(product_names.title(), self.entry_toplevel.return_value(), self.price()))
        self.__product_names = []
        self.total()
        self.custom_message.destroy()

    def price(self):
        for product, details in self.available_products.items():
            if product == self.entered_product:
                true_price = details[-1]
        return self.quantity * true_price

    def total(self):
        total_price = 0
        for i in self.treeview.get_children():
            price = int(self.treeview.item(i, 'values')[2])
            total_price += price
        self.total_entry['state'] = 'normal'
        self.total_entry.delete(0, tk.END)
        self.total_entry.insert(0, total_price)
        self.total_entry['state'] = 'disabled'


class MainTreeview(ttk.Treeview):
    def __init__(self, parent):
        super().__init__(parent, columns=("Items", "Quantity", "Price"), height=6)
        # Setting heading names
        self.heading("#1", text="Items")
        self.heading("#2", text="Quantity")
        self.heading("#3", text="Price")

        # Resizing columns
        self.column("#0", width=0, stretch=tk.NO)
        self.column("Items", anchor=tk.W, width=100)
        self.column("Quantity", anchor=tk.W, width=65)
        self.column("Price", anchor=tk.CENTER, width=84)

        # Placing treeview
        self.place(x=1, y=1)

if __name__ == '__main__':
    MainDoor('GearMasters MotorSports', (500, 230))
