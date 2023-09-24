from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, ListView

from .forms import CoffeeForm, FeedbackForm, RegisterUserForm, LoginUserForm
from .models import Coffee, Feedback


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'coffee/login.html'

    def get_success_url(self):
        return reverse_lazy('coffee:coffee')


def logout_user(request):
    logout(request)
    return redirect('coffee:login')


class SignUp(CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy("coffee:coffee")
    template_name = 'coffee/registration.html'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title='Registration')
    #     return dict(list(context.items()) + list(c_def.items()))


class CoffeeList(ListView):
    model = Coffee
    template_name = 'coffee/coffee.html'
    context_object_name = 'coffees'
    queryset = Coffee.objects.order_by('price')


#   def coffee(request):
#       coffees = Coffee.objects.order_by('price')
#       return render(request, 'coffee/coffee.html', {'coffees': coffees})


def contact(request):
    return render(request, 'coffee/contact.html', )


# def user_login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request,
#                                 user_login=cd['username'],
#                                 password=cd['password']
#                                 )
#             if user is not None:
#                 if user.is_active():
#                     login(request, user)
#                     return HttpResponse('Authenticated successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#         else:
#             return HttpResponse('Invalid logun')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        coffees = self.object
        feedbacks = coffees.feedbacks.all()
        context['feedbacks'] = feedbacks
        return context


class Update(UpdateView):
    model = Coffee
    template_name = 'coffee/update_coffee.html'
    form_class = CoffeeForm


class Delete(DeleteView):
    model = Coffee
    template = 'coffee/coffee_confirm_delete.html'
    success_url = '/coffee/'


class CreateFeedback(CreateView):
    model = Feedback
    template_name = 'coffee/create_feedback.html'
    form_class = FeedbackForm

    def form_valid(self, form):
        coffee_id = self.kwargs['pk']
        try:
            coffees = Coffee.objects.get(pk=coffee_id)
        except Coffee.DoesNotExist:
            raise Http404("Coffee does not exist")

        feedback = form.save(commit=False)

        if self.request.user.is_authenticated:
            feedback.user = self.request.user.username

        feedback.coffees = coffees
        feedback.save()

        return HttpResponseRedirect(reverse('coffee:info', kwargs={'pk': coffee_id}))

# def add_feedback(request, pk):
#     error = ''
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('info')
#         else:
#             error = 'Invalid form input'
#             print("FORM ERRORS", form.error)
#
#         form = FeedbackForm
#
#         data = {
#             'form': form,
#             'error': error
#         }
#         return render(request, 'create_feedback.html', data)
#
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
