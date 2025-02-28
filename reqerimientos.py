import tkinter as tk

Transportadora = tk.Tk()                   
Transportadora.title('Registro_Vehiculos')    
Transportadora.geometry('700x700')  

Registro_Vehiculos = tk.StringVar()  

titulo = tk.Label(Transportadora,text='Sistema de Administración de Flotas de Vehículos  ',font=('Arial',16,'bold'),padx=20,pady=40,bg='#e6a698',fg='#000000')
titulo.pack() 


holaNombre = tk.Label(Transportadora,text='Modelo',font=('arial',18,),padx=20,pady=10)
holaNombre.pack()   
nombre = tk.Entry(Transportadora,font=('arial',15,))     
nombre.pack(padx=20,pady=10)    

holaNombre = tk.Label(Transportadora,text='Numero de matricula  ',font=('arial',18,),padx=20,pady=10)
holaNombre.pack()   
nombre = tk.Entry(Transportadora,font=('arial',15,))     
nombre.pack(padx=20,pady=10)

holaNombre = tk.Label(Transportadora,text='Año de fabricación',font=('arial',18,),padx=20,pady=10)
holaNombre.pack()      
nombre = tk.Entry(Transportadora,font=('arial',15,))     
nombre.pack(padx=20,pady=10)    

holaNombre = tk.Label(Transportadora,text='Capacidad de carga',font=('arial',18,),padx=20,pady=10)
holaNombre.pack()   
nombre = tk.Entry(Transportadora,font=('arial',15,))     
nombre.pack(padx=20,pady=10)    

holaNombre = tk.Label(Transportadora,text='Estado de mantenimiento',font=('arial',18,),padx=20,pady=10)
holaNombre.pack()   
nombre = tk.Entry(Transportadora,font=('arial',15,))     
nombre.pack(padx=20,pady=10)    

boton = tk.Button(Transportadora,text='Agregar vehiculo',font=('arial',15,))
boton.pack(padx=20,pady=10)

Transportadora.mainloop() 