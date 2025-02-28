import tkinter as tk

Transportadora = tk.Tk()                   
Transportadora.title('Registro_Vehiculos')    
Transportadora.geometry('700x700')  

Registro_Vehiculos = tk.StringVar()  

vehiculos = []  

def agregar_vehiculo():
    vehiculo = {
        "Modelo": modelo.get(),
        "Numero de matricula": matricula.get(),
        "Año de fabricación": anio.get(),
        "Capacidad de carga": carga.get(),
        "Estado de mantenimiento": mantenimiento.get()
    }
    vehiculos.append(vehiculo) 
    
    
    modelo.delete(0, tk.END)
    matricula.delete(0, tk.END)
    anio.delete(0, tk.END)
    carga.delete(0, tk.END)
    mantenimiento.delete(0, tk.END)

titulo = tk.Label(Transportadora, text='Sistema de Administración de Flotas de Vehículos',font=('Arial', 16, 'bold'), padx=20, pady=40, bg='#e6a698', fg='#000000')
titulo.pack()

tk.Label(Transportadora, text='Modelo', font=('arial', 18), padx=20, pady=10).pack()
modelo = tk.Entry(Transportadora, font=('arial', 15))
modelo.pack(padx=20, pady=10)

tk.Label(Transportadora, text='Numero de matricula', font=('arial', 18), padx=20, pady=10).pack()
matricula = tk.Entry(Transportadora, font=('arial', 15))
matricula.pack(padx=20, pady=10)

tk.Label(Transportadora, text='Año de fabricación', font=('arial', 18), padx=20, pady=10).pack()
anio = tk.Entry(Transportadora, font=('arial', 15))
anio.pack(padx=20, pady=10)

tk.Label(Transportadora, text='Capacidad de carga', font=('arial', 18), padx=20, pady=10).pack()
carga = tk.Entry(Transportadora, font=('arial', 15))
carga.pack(padx=20, pady=10)

tk.Label(Transportadora, text='Estado de mantenimiento', font=('arial', 18), padx=20, pady=10).pack()
mantenimiento = tk.Entry(Transportadora, font=('arial', 15))
mantenimiento.pack(padx=20, pady=10)


boton = tk.Button(Transportadora, text='Agregar vehiculo', font=('arial', 15), command=agregar_vehiculo)
boton.pack(padx=20, pady=10)

Transportadora.mainloop()
