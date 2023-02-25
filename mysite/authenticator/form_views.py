from django.views.generic.edit import FormMixin, ProcessFormView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserFileForm
from .models import UserFile

class UserFileView(LoginRequiredMixin, FormMixin, ProcessFormView, TemplateView):
    template_name = 'form.html'
    form_class = UserFileForm() #need to add user somehow?
    success_url = reverse_lazy('run-algorithm')

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            user_file = form.save(commit=False)
            user_file.user = request.user
            user_file.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
