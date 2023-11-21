from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .forms import LibrosForm
from .models import Libros
from django.urls import reverse_lazy
# Create your views here.
# class ProyectoLibros(View):

#     def get(self, request):

#         libros = Libros.objects.all()
#         return render(request, 'Libros/listadoLibros.html', {"libros":libros})

class ProyectoLibros(ListView):
    model = Libros
    template_name = 'Libros/listadoLibros.html'

class FormLibro(View):

    def get(self, request):
        form = LibrosForm()

        return render(request, 'Libros/FormLibros.html', {'form':form})

    def post(self, request):
        form = LibrosForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('listadoLibros')
        
        return render(request, 'Libros/FormLibros.html', {'form':form})
    

# class Detalles(View):
#     def get(self, request, pk):
#         detalles = get_object_or_404(Libros, pk=pk)
#         return render(request, 'Libros/detallesLibros.html', {'detalles':detalles})

class Detalles(DetailView):
    model = Libros
    template_name = 'Libros/detallesLibros.html'


class Editar(UpdateView):
    model = Libros
    fields = ['title','author', 'rating','sinopsis','created_at','update_at']
    template_name= "Libros/editar.html"
    success_url = reverse_lazy("listadoLibros")

class Borrar(DeleteView):
    model = Libros
    #fields = ['title','author', 'rating','sinopsis','created_at','update_at']
    template_name= "Libros/borrar.html"
    success_url = reverse_lazy("listadoLibros")
# class Editar(View):

#     def get(self, request, pk):
#         libros = get_object_or_404(Libros, pk=pk)
#         form = LibrosForm(instance=libros)
#         return render(request, 'Libros/Editar.html', {'form': form, 'libro': libros})

#     def post(self, request, pk):
#         libros = get_object_or_404(Libros, pk=pk)
#         form = LibrosForm(request.POST, instance=libros)
#         if form.is_valid():
#             form.save()
#             return redirect('listadoLibros')
#         return render(request, 'Libros/Editar.html', {'form': form, 'libro': libros})