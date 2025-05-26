from flask import Blueprint,send_file, redirect
from PIL import Image
import qrcode
import pymupdf
import shutil
import os

qr_bp=Blueprint("qr", __name__)

# Funcion que va a crear una imagen QR. La URI almacenada va a ser dinamica, cuando se conecte con la BDD el 'id_restaurante' variara dependiendo del restaurante
def crear_imgqr():
    img_qr=qrcode.make("http://localhost:8100/reseña/id_restaurante")
    img_qr.save("front-end/qr_code.png")

# Funcion que va a crear el archivo PDF que va a contener el QR y luego lo va a guardar
@qr_bp.route("/crear-pdfqr")
def crear_pdfqr():
    crear_imgqr()                           # Creo la imagen QR con la URI hacia el template que le permite al usuario reservar

    # Creo una copia del archivo base a modificar ya que la librería 'PyMuPDF' realiza cambios sobre este y los mismos se quedan almacenados a pesar de eliminarlo al terminar la edicion. Esto no es lo que busco
    shutil.copy("front-end/FoodyBA_crudo.pdf", "front-end/FoodyBA_edit.pdf")

    # Abro el documento PDF con la libreria 'pymupdf'
    doc_pdf=pymupdf.open("front-end/FoodyBA_edit.pdf")
    pagina=doc_pdf[0]                                           # Selecciono la pagina actual

    pag_width,pag_height=pagina.rect.width, pagina.rect.height
    # ----------------- NOMBRE DEL COMERCIO -----------------------

    nombre_comercio = "Restaurante A"                            # Dato extraido de la BDD

    # Creo el rectangulo de texto que va a contener el nombre del comercio
    rect_name_bss=pymupdf.Rect((pag_width/3) - 150,(pag_height/6),(pag_width/3) + 350,(pag_height/6) + 150)

    # Inserto el nombre del comercio
    pagina.insert_textbox(
        rect_name_bss,
        nombre_comercio,
        fontname="helv",
        fontsize=25,
        color=(0,0,0),
        align=1
        )

    # ----------------- TEXTO GENERICO -----------------------
    texto_generico="¡Deja tu reseña!"
    rect_generic_text=pymupdf.Rect((pag_width/3) - 150, (pag_height/5) + 25, (pag_width/3) + 350, (pag_height/5) + 325)

    pagina.insert_textbox(
        rect_generic_text,
        texto_generico,
        fontname="helv",
        fontsize=30,
        color=(0,0,0),
        align=1
    )

    # ----------------- IMAGEN QR -----------------------

    # Abro la imagen para poder tener las dimensiones de la misma y asi escalar el tamaño con el de la pág
    img=Image.open("front-end/qr_code.png")
    img_width,img_height=img.size

    escala=min(pag_width/img_width, pag_height/img_height, 0.7)           
    final_width_img=img_width*escala
    final_height_img=img_height*escala

    x0=(pag_width - final_width_img)/2
    y0=(pag_height - final_height_img)/2
    x1=x0 + final_width_img
    y1=y0 + final_height_img
    
    rect_img_qr=pymupdf.Rect(x0,y0,x1,y1)
    pagina.insert_image(rect_img_qr, filename="front-end/qr_code.png")

    # ----------------- DIRECCIÓN DEL COMERCIO -----------------------

    direccion_comercio="Avenida Siempreviva 742"                   # Dato extraido de la BDD

    rect_dir_bss=pymupdf.Rect(85, pag_height - 167, 250, pag_height - 100)

    pagina.insert_textbox(
        rect_dir_bss,
        direccion_comercio,
        fontname="helv",
        fontsize=10,
        color=(1,1,1),
        align=0
    )

    # ----------------- TELEFONO DEL COMERCIO -----------------------

    telefono_comercio="+54 4545 8000 "                            # Dato extraido de la BDD

    rect_tel_bss=pymupdf.Rect(85, pag_height - 123, 250, pag_height - 50)

    pagina.insert_textbox(
        rect_tel_bss,
        telefono_comercio,
        fontname="helv",
        fontsize=10,
        color=(1,1,1),
        align=0
    )

    new_pdf_path="front-end/pdf_qr.pdf"
    # Elimino previas versiones del PDF con el QR personalizado.

    # Verifico si existe un PDF de salida previo, en el caso de que si lo elimino.
    # Si no se hace esto, como se menciono previamente, en el PDF de salida se van a quedar cambios previamente realizados
    if os.path.exists(new_pdf_path):
        os.remove(new_pdf_path)

    # Si no existia previamente
    doc_pdf.save(new_pdf_path)
    os.remove("front-end/FoodyBA_edit.pdf")                 # Elimino el PDF editable para futuras modificaciones
    doc_pdf.close()

    return redirect("/"),200

# Endpoint que va a enviar un archivo con contenido al cliente.
@qr_bp.route("/descargar-pdfqr")
def descargar_pdfqr():
    return send_file("pdf_qr.pdf", as_attachment=True)