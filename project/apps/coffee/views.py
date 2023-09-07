from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView

from .forms import CoffeeForm
from .models import Coffee


def coffee(request):
    coffees = Coffee.objects.order_by('price')
    return render(request, 'coffee/coffee.html', {'coffees': coffees})


def contact(request):
    return render(request, 'coffee/contact.html', )


class Create(CreateView):
    model = Coffee
    template_name = 'coffee/create_coffee.html'
    form_class = CoffeeForm

    def form_valid(self, form):
        self.object = form.save(commit=False)

        picture = self.request.FILES.get('picture')
        if isinstance(picture, InMemoryUploadedFile):
            picture_data = picture.read()
            self.object.picture.save(picture.name, ContentFile(picture_data), save=False)

        self.object.save()
        return super().form_valid(form)


class Info(DetailView):
    model = Coffee
    template_name = 'coffee/info.html'
    context_object_name = 'coffee'


class Update(UpdateView):
    model = Coffee
    template_name = 'coffee/update_coffee.html'

    form_class = CoffeeForm


class Delete(DeleteView):
    model = Coffee
    template = 'coffee/coffee_confirm_delete.html'
    success_url = '/coffee/'

# def create(request):
#     error = ''
#     if request.method == 'POST':
#         form = CoffeeForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('coffee')
#         else:
#             error = 'Invalid form input'
#             print("Form errors:", form.errors)
#
#     form = CoffeeForm()
#
#     data = {
#         'form': form,
#         'error': error
#     }
#     return render(request, 'coffee/create_coffee.html', data)

# def update(request, pk):
#     error = ''
#     coffee_instance = Coffee.objects.get(pk=pk)
#     if request.method == "POST":
#         form = CoffeeForm(request.POST, request.FILES, instance=coffee_instance)
#         if form.is_valid():
#             form.save()
#             return redirect('coffee')
#         else:
#             error = 'Invalid form input'
#             print("Form errors:", form.errors)
#     else:
#         form = CoffeeForm(instance=coffee_instance)
#
#         data = {
#             'form': form,
#             'pk': pk,
#             'error': error
#         }
#         print("debug:", data)
#         return render(request, 'coffee/update_coffee.html', data)

# def delete(request, pk):
#     coffee_instance = get_object_or_404(Coffee, pk=pk)
#     if request.method == 'POST':
#         coffee_instance.delete()
#         print('confirm')
#         return redirect('coffee')
#     return render(request, 'coffee/coffee_confirm_delete.html', {'coffee_instance': coffee_instance})
