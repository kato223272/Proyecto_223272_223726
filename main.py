import tkinter as tk
from maquina_turing import MaquinaTuring

def iniciar_maquina():
    codigo = entrada_codigo.get().strip().upper()
    if codigo:
        maquina = MaquinaTuring(codigo)
        label_resultado.config(text="")
        avanzar_paso(maquina)
    else:
        label_resultado.config(text="Por favor, ingrese un código de falla.", fg="red")

def avanzar_paso(maquina):
    if not maquina.es_finalizado():
        maquina.paso()
        ventana.after(500, lambda: avanzar_paso(maquina))
    else:
        label_resultado.config(text=maquina.obtener_resultado(), fg="#1ABC9C")

ventana = tk.Tk()
ventana.title("Simulación de Máquina de Turing - Detección de Fallas de Sensores Nissan")
ventana.configure(bg="#2E4053")
ventana.geometry("600x400")

titulo = tk.Label(ventana, text="Detección de Fallas en Sensores de Automóviles Nissan", 
                  font=("Helvetica", 16, "bold"), fg="white", bg="#2E4053")
titulo.pack(pady=10)

entrada_frame = tk.Frame(ventana, bg="#2E4053")
entrada_frame.pack(pady=10)

label_codigo = tk.Label(entrada_frame, text="Ingrese el código de falla:", 
                        font=("Helvetica", 12), fg="white", bg="#2E4053")
label_codigo.pack(side="left", padx=5)

entrada_codigo = tk.Entry(entrada_frame, font=("Helvetica", 12), width=10, justify="center")
entrada_codigo.pack(side="left", padx=5)

boton_iniciar = tk.Button(entrada_frame, text="Iniciar", command=iniciar_maquina, 
                          font=("Helvetica", 12), bg="#1ABC9C", fg="white", 
                          activebackground="#16A085", activeforeground="white")
boton_iniciar.pack(side="left", padx=10)

label_cinta = tk.Label(ventana, text="⟶ P0101   P0171   P0300   P0301   P0420   P0455   P0500   P0603   P0705", 
                       font=("Courier", 14), fg="white", bg="#34495E")
label_cinta.pack(pady=10)

label_resultado = tk.Label(ventana, text="", font=("Helvetica", 14), fg="#1ABC9C", bg="#2E4053")
label_resultado.pack(pady=20)

ventana.mainloop()
