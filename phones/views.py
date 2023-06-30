from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from phones.forms import PhoneForm
from phones.models import Phone
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView


# не полная информация о товаре


class PhoneListView(ListView):
    template_name = 'phone_list.html'
    model = Phone

    def get_queryset(self):
        return Phone.objects.all()


# def phone_list_view(request):
#     if request.method == "GET":
#         phones = Phone.objects.all()
#         return render(request, 'phone_list.html', {'phones': phones})


# Полная информация об объекте по id

class PhoneDetailView(DetailView):
    template_name = "phone_detail.html"

    def get_object(self, **kwargs):
        phone_id = self.kwargs.get("id")
        return get_object_or_404(Phone, id=phone_id)


# def phone_detail_view(request, id):
#     if request.method == "GET":
#         phone = Phone.objects.get(id=id)
#         return render(request, 'phone_detail.html', {'phone': phone})


# создание объектов через формы

class CreatePhoneView(CreateView):
    template_name = 'create_phone.html'
    form_class = PhoneForm
    model = Phone
    success_url = '/phones/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreatePhoneView, self).form_valid(form=form)


# def create_object_view(request):
#     if request.method == "POST":
#         form = PhoneForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Успешно добавлен в Базу Данных")
#     else:
#         form = PhoneForm()
#     return render(request, "create_phone.html", {'form': form})

# Редактирование


class UpdatePhoneView(UpdateView):
    template_name = 'update_phone.html'
    form_class = PhoneForm
    success_url = '/phones/'

    def get_object(self, **kwargs):
        phone_id = self.kwargs.get('id')
        return get_object_or_404(Phone, id=phone_id)

    def form_valid(self, form):
        return super(UpdatePhoneView, self).form_valid(form=form)


# def update_object_view(request, id):
#     phone = Phone.objects.get(id=id)
#     if request.method == 'POST':
#         form = PhoneForm(instance=phone, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Данные успешно обновлены')
#     else:
#         form = PhoneForm(instance=phone)
#     context = {
#         'form': form,
#         'phone': phone
#     }
#     return render(request, 'update_phone.html', context)


# Удаление из базы


class DeletePhoneView(DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/phones/'

    def get_object(self, **kwargs):
        phone_id = self.kwargs.get('id')
        return get_object_or_404(Phone, id=phone_id)


# def delete_object_view(request, id):
#     phone = Phone.objects.get(id=id)
#     phone.delete()
#     return HttpResponse('Телефон удален из Базы данных')

# Кнопка поиск
class Search(ListView):
    template_name = "phone_list.html"
    context_object_name = "phone"
    paginate_by = 5

    def get_queryset(self):
        return Phone.objects.filter(title__icontains=self.request.GET.get("q")).order_by('id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context
