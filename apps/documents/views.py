from django.views.generic import CreateView

from .models import Document


class DocumentCreate(CreateView):
    model = Document
    fields = ['description', 'file']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.owner_id = self.kwargs['employee_pk']

        if form.is_valid():
            return self.form_valid(form)
        else:
            self.form_invalid(form)
