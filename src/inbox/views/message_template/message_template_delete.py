from django.urls import reverse_lazy
from django.views.generic import DeleteView
from src.inbox.models.message_template import MessageTemplate
from django.contrib.auth.mixins import LoginRequiredMixin

class MessageTemplateDeleteView(DeleteView, LoginRequiredMixin):
    model = MessageTemplate
    template_name = 'object_confirm_delete.html'
    success_url = reverse_lazy('inbox:message_template_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete(soft=True)
        return self.success_url