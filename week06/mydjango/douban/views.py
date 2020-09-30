from django.shortcuts import render

# Create your views here.
from .models import T1
from django.db.models import Avg

def books_short(request):
    ###  从models取数据传给template  ###
    shorts = T1.objects.all()
    # 评论数量
    counter = T1.objects.all().count()

    # 平均星级
    # star_value = T1.objects.values('n_star')
    star_avg =f" {T1.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f} "
    # 情感倾向
    sent_avg =f" {T1.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "

    # # 正向数量
    # queryset = T1.objects.values('sentiment')
    # condtions = {'sentiment__gte': 0.5}
    # plus = queryset.filter(**condtions).count()
    
    # 大于三星级
    queryset = T1.objects.values('n_star')
    condtions = {'sentiment__gte': 3}
    plus = queryset.filter(**condtions)

    # 负向数量
    queryset = T1.objects.values('sentiment')
    condtions = {'sentiment__lt': 0.5}
    minus = queryset.filter(**condtions).count()

    # return render(request, 'douban.html', locals())
    return render(request, 'result.html', locals())


 def start_lt_3(request):
     if request.method == "GET":
         key = request.GET.get('q', "")
         conditions = {'n_star__gt': 3}
         keys = None
         if key:
             conditions['short__icontains'] = key
             safe = "/#%[]=:;$&()+,!?*@'~"
             keys = []
             for i, k in enumerate(key):
                 if k in safe:
                     k = '%{:02X}'.format(ord(k))
                 keys.append(k)
             keys = ''.join(keys)

         shorts = T1.objects.filter(**conditions)
         return render(request, 'index2.html', {'shorts': shorts, 'keys': keys})