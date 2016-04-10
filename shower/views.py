from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import ListView, View
from django.views.generic.detail import SingleObjectMixin
from .models import RegistryItem


class RegistryListView(ListView):
  model = RegistryItem


class RegistryItemCompletedView(SingleObjectMixin, View):
  model = RegistryItem

  def post(self, request, *args, **kwargs):
    self.object = self.get_object()
    self.object.picked = True
    self.object.save()

    return HttpResponseRedirect(reverse('registry'))
