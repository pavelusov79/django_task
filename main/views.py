from django.contrib.auth.views import LoginView, auth_login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import BasePermission

from django_filters import rest_framework as filters

from .serializers import LogsModelSerializer
from .models import Logs


class MemberOfLogGroup(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name__in=['log']).exists()


class ProjectFilter(filters.FilterSet):
    ip_field = filters.CharFilter(lookup_expr='contains')
    min_date = filters.DateFilter(field_name='datetime_field', lookup_expr='gte')
    max_date = filters.DateFilter(field_name='datetime_field', lookup_expr='lte')

    class Meta:
        model = Logs
        fields = ['ip_field']


class ProjectPaginationClass(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'


class LogsView(ListModelMixin, GenericViewSet):
    permission_classes = [MemberOfLogGroup]
    filterset_class = ProjectFilter
    pagination_class = ProjectPaginationClass
    queryset = Logs.objects.all()
    serializer_class = LogsModelSerializer


class UserLoginView(LoginView):
    template_name = 'main/index.html'

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        if form.get_user().is_superuser:
            return HttpResponseRedirect(reverse('admin:index'))
        elif form.get_user().groups.filter(name__in=['log']).exists():
            return HttpResponseRedirect(reverse('admin:main_logs_changelist'))
        else:
            return HttpResponse('Доступ запрещен. Обратитесь к администратору за допуском.')







