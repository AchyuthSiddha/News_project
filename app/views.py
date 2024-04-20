from django.shortcuts import render

# Create your views here.
def news_info(request):
    return render(request,'result.html')

def Movies(request):
    First_msg='Movies Information'
    second_msg=' Till square super hit movie now days'
    third_msg=' Now director planning to Till cube movie'
    Fourth_msg=' now my aim full pledge the django course'
    type='movies'
    d={'first_msg':First_msg,'second_msg':second_msg,'third_msg':third_msg,'fourth_msg':Fourth_msg,'Type':type}
    return render(request,'news.html',d)

def Sports(request):
    First_msg='Sports Information'
    second_msg=' now days everyone watching ipl matches'
    third_msg=' next year dhoni will retired in ipl'
    Fourth_msg=' now its all about in BCCI'
    type='sports'
    d={'first_msg':First_msg,'second_msg':second_msg,'third_msg':third_msg,'fourth_msg':Fourth_msg,'Type':type}
    return render(request,'news.html',d)


def Politics(request):
    First_msg='politics Information'
    second_msg='Our president is PM Modi'
    third_msg='your chief minster is Ys jagan'
    Fourth_msg='TG cm is Revanth reddy'
    type='politics'
    d={'first_msg':First_msg,'second_msg':second_msg,'third_msg':third_msg,'fourth_msg':Fourth_msg,'Type':type}
    return render(request,'news.html',d)
