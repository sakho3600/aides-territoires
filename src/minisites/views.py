from django.http import QueryDict, Http404
from django.views.generic import TemplateView

from search.models import SearchPage
from aids.views import SearchView, AdvancedSearchView, AidDetailView
from alerts.views import AlertCreate


class MinisiteMixin:

    def get(self, request, *args, **kwargs):
        self.search_page = self.get_search_page()
        return super().get(request, *args, **kwargs)

    def get_search_page(self):
        """Get the custom page from url.

        This view will be accessed from a `xxx.aides-territoires.beta.gouv.fr`.
        So we need to extract the `xxx` part.
        """

        host = self.request.get_host()
        page_slug = host.split('.')[0]
        qs = SearchPage.objects.filter(slug=page_slug)
        try:
            obj = qs.get()
        except qs.model.DoesNotExist:
            raise Http404('No "Search page" found matching the query')
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_page'] = self.search_page
        return context


class Home(MinisiteMixin, SearchView):
    """A static search page with admin-customizable content."""

    template_name = 'minisites/search_page.html'

    def get_form_kwargs(self):
        """Set the data passed to the form.

        If no data was provided by the user, then we use the initial
        querystring provided by admins.

        If the form was submitted, the GET values are set, we use those
        instead.
        """
        initial_data = QueryDict(
            self.search_page.search_querystring, mutable=True)
        user_data = self.request.GET.copy()
        user_data.pop('page', None)
        user_data.pop('integration', None)
        data = user_data or initial_data
        kwargs = super().get_form_kwargs()
        kwargs['data'] = data
        return kwargs

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        if self.search_page.available_categories:
            categories_qs = self.search_page.available_categories
            form.fields['categories'].queryset = categories_qs

        return form


class Search(MinisiteMixin, AdvancedSearchView):
    """The full search form."""

    template_name = 'minisites/advanced_search.html'


class Aid(MinisiteMixin, AidDetailView):
    """The detail page of a single aid."""

    template_name = 'minisites/aid_detail.html'


class Alert(MinisiteMixin, AlertCreate):
    pass


class LegalMentions(MinisiteMixin, TemplateView):
    template_name = 'minisites/legal_mentions.html'