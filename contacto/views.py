from django.shortcuts import render, redirect
from .forms import formularioContacto
from django.core.mail import EmailMessage

def contacto(request):

    formulario_contacto=formularioContacto()

    if request.method=="POST":
        formulario_contacto=formularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje desde App Django",
            "El usuario con nombre {} con el correo {} escrobe lo siguiente: \n\n {}".format(nombre, email, contenido),
            "",["Karinrodriguez30@gmail.com"], reply_to=[email])

            try:
                email.send()

                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?invalido")


    return render(request, "contacto/contacto.html",{'miFormulario':formulario_contacto})



