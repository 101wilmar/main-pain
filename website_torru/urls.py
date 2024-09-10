from django.urls import path
from .views import GraphicListView, GraphicDesignDetailView, MotionListView, MotionDesignDetailView, main_landing
from website_torru import views

app_name = 'torru'

urlpatterns = [
    path('', main_landing , name='homes'),
    path('media/<slug:slug>/', views.media_detail, name='media_detail'),
    path('big-baby-tape/', views.media_bbt, name='media_bbt'),
    path('graphic-designs/', GraphicListView.as_view(), name='graphic_design_list'),
    path('graphic-designs/<int:pk>/', GraphicDesignDetailView.as_view(), name='graphic_design_detail'),
    path('motion-designs/', MotionListView.as_view(), name='motion_design_list'),
    path('motion-designs/<int:pk>/', MotionDesignDetailView.as_view(), name='motion_design_detail'),
]
