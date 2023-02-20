from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from recognition import views as recog_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('santri/', include('app.urls')),

    path("", recog_views.home, name="home"),
    path("dashboard/", recog_views.dashboard, name="dashboard"),
    path("train/", recog_views.train, name="train"),
    path("add_photos/", recog_views.add_photos, name="add-photos"),
    path("delete_photos/", recog_views.delete_photos, name="delete-photos"),
    path("login/",auth_views.LoginView.as_view(template_name="users/login.html"),name="login",),
    path("logout/",auth_views.LogoutView.as_view(template_name="recognition/home.html"),name="logout",),
    path("register/", users_views.register, name="register"),
    path('absen_list/', users_views.AbsenList, name='absen_list'),
    path('absen_view/<int:pk>', users_views.AbsenDetail, name='absen_detail'),
    path('absen_delete/<int:pk>/', users_views.AbsenDelete, name='absen_delete'),
    path('absen_update/<int:pk>/', users_views.AbsenUpdate, name='absen_update'),
    path('absen_cari/', users_views.AbsenCari, name='absen_cari'),
    path("mark_your_attendance",recog_views.mark_your_attendance,name="mark-your-attendance",),
    path("mark_your_attendance_out",recog_views.mark_your_attendance_out,name="mark-your-attendance-out",),
    path("view_attendance_home",recog_views.view_attendance_home,name="view-attendance-home",),
    path("view_attendance_date",recog_views.view_attendance_date,name="view-attendance-date",),
    path("view_attendance_siswa",recog_views.view_attendance_siswa,name="view-attendance-siswa",),
    path("view_attendance_siswa_buka",recog_views.view_attendance_siswa_buka,name="view-attendance-siswa-buka",),
    path("view_my_attendance",recog_views.view_my_attendance_siswa_login,name="view-my-attendance-siswa-login",),
    path("not_authorised", recog_views.not_authorised, name="not-authorised"),
    path('detail_csv/', users_views.Detail_csv, name='detail_csv'),
]

admin.site.site_title = "EMIS Admin | PAD"
admin.site.site_header = 'EMIS Admin | Pondok Pesantren Abdul Dhohir'