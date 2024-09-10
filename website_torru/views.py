from django.http import Http404, HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import GraphicDesign, MotionDesign 
from django.views.generic import ListView, DetailView


def main_landing(request):
    template = loader.get_template('landing.html')
    return HttpResponse(template.render())


class GraphicListView(ListView):
    template_name = 'graphic_list.html'  # Исправлено на template_name
    model = GraphicDesign
    context_object_name = 'graphic_designs'
    ordering = ['-uploaded_at']
    paginate_by = 5


class MotionListView(ListView):
    template_name = 'motion_list.html'  # Исправлено на template_name и правильную модель
    model = MotionDesign  # Исправлено на MotionDesign
    context_object_name = 'motion_designs'  # Исправлено на уникальное имя контекста
    ordering = ['-uploaded_at']
    paginate_by = 5


class GraphicDesignDetailView(DetailView):
    model = GraphicDesign
    template_name = 'graphicdesign_detail.html'
    context_object_name = 'graphic_design'


class MotionDesignDetailView(DetailView):
    model = MotionDesign
    template_name = 'motiondesign_detail.html'  # Исправлено на motiondesign_detail.html
    context_object_name = 'motion_design'

# В views.py или в отдельном конфигурационном файле
MEDIA_ITEMS = [
    {
        'slug': 'alblak-52',
        'title': 'ALBLAK 52',
        'description': 'Проект TORRU DESIGN существует с 2021 года и помогает осуществить идеи клиентов любой сложности. Мы занимаемся как 2D дизайном, так и 3D дизайном, анимацией.',
        'videos': [
            '/static/videos/52.mp4',
            '/static/videos/52-2.mp4',
        ],
        'details_url': '/media/'
    },
    {
        'slug': '10age',
        'title': '10AGE',
        'description': 'Проект TORRU DESIGN существует с 2021 года и помогает осуществить идеи клиентов любой сложности. Мы занимаемся как 2D дизайном, так и 3D дизайном, анимацией.',
        
        'videos': [
            '/static/videos/10age.mp4',
        ],
        'details_url': '/media/'
    },
    {
        'slug': 'treepside',
        'title': 'TREEPSIDE',
        'description': 'Проект TORRU DESIGN существует с 2021 года и помогает осуществить идеи клиентов любой сложности. Мы занимаемся как 2D дизайном, так и 3D дизайном, анимацией.',
        'videos': [
            '/static/videos/treepside.mp4',
        ],
        'details_url': '/media/'
    },
    {
        'slug': 'bushido-zho',
        'title': 'BUSHIDO ZHO',
        'description': 'Проект TORRU DESIGN существует с 2021 года и помогает осуществить идеи клиентов любой сложности. Мы занимаемся как 2D дизайном, так и 3D дизайном, анимацией.',
        'videos': [
            '/static/videos/bush-vid.mp4',
        ],
        'details_url': '/media/'
    },
    {
        'slug': 'onyx',
        'title': 'ONYX',
        'description': 'Проект TORRU DESIGN существует с 2021 года и помогает осуществить идеи клиентов любой сложности. Мы занимаемся как 2D дизайном, так и 3D дизайном, анимацией.',
        'videos': [
            '/static/videos/onyx.mp4',
        ],
        'details_url': '/media/'
    }, 
    {
        'slug': '4n-way',
        'title': '4N WAY',
        'description': 'Проект TORRU DESIGN существует с 2021 года и помогает осуществить идеи клиентов любой сложности. Мы занимаемся как 2D дизайном, так и 3D дизайном, анимацией.',
        'videos': [
            '/static/videos/4nway.mp4',
        ],
        'details_url': '/media/'
    },
     {
        'slug': 'lovv66',
        'title': 'LOVV66',
        'description': 'Проект TORRU DESIGN существует с 2021 года и помогает осуществить идеи клиентов любой сложности. Мы занимаемся как 2D дизайном, так и 3D дизайном, анимацией.',
        'videos': [
            '/static/videos/LOVV66.mp4',
            '/static/videos/LOVV66-2.mp4',
        ],
        'details_url': '/media/'
    },
    {
        'slug': 'chief-keef',
        'title': 'CHIEF KEEF',
        'description': 'Проект TORRU DESIGN существует с 2021 года и помогает осуществить идеи клиентов любой сложности. Мы занимаемся как 2D дизайном, так и 3D дизайном, анимацией.',
        
        'images': [
            '/static/images/chief-img.png'
        ],
        'videos': [
            '/static/videos/chef-kif.mp4',
        ],
        
        'details_url': '/media/'
    },
]




from django.http import Http404
from django.shortcuts import render

# Твой массив MEDIA_ITEMS остается таким же, как был

from django.http import Http404
from django.shortcuts import render

def media_detail(request, slug):
    # Поиск текущего медиа-элемента по слагу
    media_item = next((item for item in MEDIA_ITEMS if item['slug'] == slug), None)
    if media_item is None:
        raise Http404("Media item not found")

    # Найти индекс текущего элемента в списке
    current_index = next((index for index, item in enumerate(MEDIA_ITEMS) if item['slug'] == slug), None)

    # Определить индекс следующего и предыдущего элемента
    next_index = (current_index + 1) % len(MEDIA_ITEMS)
    prev_index = (current_index - 1) % len(MEDIA_ITEMS)

    # Получить слаги следующего и предыдущего элементов
    next_slug = MEDIA_ITEMS[next_index]['slug']
    prev_slug = MEDIA_ITEMS[prev_index]['slug']

    # Построить URL для следующего и предыдущего элементов
    next_url = f"/media/{next_slug}/"
    prev_url = f"/media/{prev_slug}/"

    return render(request, 'prime.html', {
        'media_item': media_item,
        'next_url': next_url,
        'prev_url': prev_url
    })



def media_bbt(request):
    print("media_bbt view called")  # Проверка выполнения представления
    template = loader.get_template('big-baby.html')
    return HttpResponse(template.render({}, request))
