import tkinter as tk
from views.header_view import cargar_header
from views.productos_view import cargar_productos
ventana = tk.Tk()
ventana.title("Mi tienda")
ventana.geometry("1000x600")
cargar_header(ventana)
ventana.mainloop()  # Este es el método correcto

