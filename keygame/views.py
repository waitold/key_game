from django.shortcuts import render
import random

# Create your views here.


def init_key_game(request):  # セッションに正解の値を持たせる
    request.session['correct_num'] = random.randrange(10)
    return render(request, "keygame/key_init.html")


def check_answer(request): # postの内容を取得し正誤を判定
    if request.method == 'POST':
        if request.session.get['correct_num'] == request.POST['key_value']:
            return render(request, "keygame/game.html", {'right': 1})
        else:
            return render(request, 'keygame/game.html', {'right': -1})
    else:
        return render(request, 'keygame/access_failed.html')
