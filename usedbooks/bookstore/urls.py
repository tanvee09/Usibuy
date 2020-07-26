from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='bookstore-home'),
    path('buy/', views.buy, name='bookstore-buy'),
    path('buy/commerce', views.commercebuy, name='commerce-books'),
    path('buy/humanities', views.humanitiesbuy, name='humanities-books'),
    path('buy/engineering', views.engineeringbuy, name='engineering-books'),
    path('buy/medical', views.medicalbuy, name='medical-books'),
    path('sell/', views.sell, name='bookstore-sell'),
    path('notes/', views.note_list, name='note_list'),
    path('notes/upload/', views.upload_note, name='upload_note'),
    path('<int:id>/', views.detail, name="book-detail"),
    path('<int:pk>/update', views.update, name="book-update"),
    path('<int:pk>/delete', views.book_delete, name="book-delete"),
    path('user_post/', views.user_posts, name='user_post'),
    path('search/', views.advancedSearch, name='book_list'),
    path('base/', views.base, name='base'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)