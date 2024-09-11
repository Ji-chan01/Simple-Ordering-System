import tkinter as tk
from tkinter import ttk
import uuid


# Class for displaying products inside the treeview table
class ProductsTreeview(ttk.Treeview):
    def __init__(self, parent):
        super().__init__(parent, columns=("Product Name", "Brand", "Stock", "Price"), height=10)
        self.heading("#1", text="Product Name")
        self.heading("#2", text="Brand")
        self.heading("#3", text="Stock")
        self.heading("#4", text="Price")

        self.column("#0", width=0, stretch=tk.NO)
        self.column("Product Name", anchor=tk.W, width=160)
        self.column("Brand", anchor=tk.W, width=160)
        self.column("Stock", anchor=tk.CENTER, width=90)
        self.column("Price", anchor=tk.W, width=100)

        self.place(x=1, y=40)

    def list_of_products(self):
        product_lists = [
        ('Air Filter', 'Bosch', 130, '₱705'),
        ('Axle', 'Suzuki', 588, '₱1,700'),
        ('Back Tire', 'Dunlop', 1089, '₱730'),
        ('Battery', 'Yuasa', 187, '₱1,020'),
        ('Brake Pedal', 'Covingtons', 457, '₱70'),
        ('Carburetor', 'Suzuki', 133, '₱770'),
        ('Chain', 'DID 525VX3 X-Ring Chain', 455, '₱350'),
        ('Clutch Lever', 'CRG RC2', 342, '₱100'),
        ('Connecting Rod', 'Oliver', 406, '₱320'),
        ('Disk Brake', 'Hayes', 220, '₱1,210'),
        ('Drum Brake', 'Bendix Premium Drum and Rotor products', 455, '₱2,000'),
        ('Exhaust Pipe', 'Yoshimura', 80, '₱2,500'),
        ('Frame', 'Honda', 60, '₱930'),
        ('Front Brake lever', 'KTM', 100, '₱200'),
        ('Front Fender', 'Polisport', 400, '₱450'),
        ('Front Tire', 'Dunlop', 341, '₱550'),
        ('Fuel Tank', 'ZJ Moto', 90, '₱2,000'),
        ('Gear Shift', 'Bahn', 60, '₱132'),
        ('Handle Bar', 'Prime Primavera', 30, '₱600'),
        ('Headlight', 'NAOEVO', 67, '₱475'),
        ('Horn', 'PIAA', 140, '₱486'),
        ('Ignition Switch', 'K&L', 231, '₱116'),
        ('Indicator', 'Oxford', 100, '₱50'),
        ('Inner Tube', 'Pirelli', 300, '₱200'),
        ('Pillion', 'Honda Gold Wing', 20, '₱354'),
        ('Mudguard', 'Mucky Nutz', 100, '₱100'),
        ('Rearview Mirror', 'MZS', 96, '₱200'),
        ('Seat', 'RCB Philippines', 103, '₱100'),
        ('Spark Plug', 'NGK', 105, '₱115'),
        ('Speedometer', 'SpeedMotoCo', 189, '₱500'),
        ('Sprocket', 'Renthal', 155, '₱580'),
        ('Shock Absorber', 'Fox Racing Shox', 70, '₱829'),
        ('Signal Light', 'LighTech', 150, '₱110'),
        ('Spokes', 'HALO 2', 188, '₱220'),
        ('Tail Light', 'Ciro', 87, '₱250'),
        ('Wheel', 'Dymag Wheels', 41, '₱1,500'),
        ('Windscreen', 'Puig', 10, '₱500')]

        # Generate unique identifiers for items displayed in the treeview
        for data in product_lists:
            item_id = str(uuid.uuid4())
            self.insert('', 'end', iid=item_id, values=data)