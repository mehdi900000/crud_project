from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete

urlpatterns=[

    path ('', PostList.as_view(), name='home'),
    path ('post/new/', PostCreate.as_view(), name='post_new'),
    path ('post/<int:pk>/', PostDetail.as_view() , name='post_detail'),
    path ('post/<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
    path ('post/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]


