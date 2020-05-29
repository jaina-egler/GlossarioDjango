from django.urls import path

from management.views import AdminMenuView, AddTermView, DeleteTermView, AllTermsView,DetailsTermView,AllMessagesView

urlpatterns = [
    path('management/',AdminMenuView.as_view(),name='management'),
    path('management/add/',AddTermView.as_view(),name='add'),
    path('management/all/',AllTermsView.as_view(),name='all'),
    path('management/<int:pk>/delete/',DeleteTermView.as_view(), name='delete' ),
    path('management/<int:pk>/details/',DetailsTermView.as_view(), name='details' ),
    path('management/messages',AllMessagesView.as_view(), name='allMessages')
]#acesso aos arquivos de midia nos templates

