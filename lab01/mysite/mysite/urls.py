from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the homepage!")  # Tạo một response đơn giản cho trang chủ

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),  # Đường dẫn polls đã được định nghĩa
    path('', home),  # Đường dẫn cho trang chủ
]
