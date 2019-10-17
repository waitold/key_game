from django.shortcuts import render, redirect
import random

# Create your views here.


def key_game(request):

    if request.session.get('correct_num') is None:  # セッションを持っていなければゲームを初期化
        request.session['correct_num'] = random.randrange(10)
        return render(request, 'keygame/key_init.html')

    if request.method == 'POST':    # POSTだった場合答え合わせをし、正解の場合rightをフラグにして送る
        if request.session.get('correct_num') == int(request.POST['key_value']):
            return render(request, "keygame/key_game.html", {'right': 1})
        else:
            return render(request, 'keygame/key_game.html', {})

    return render(request, 'keygame/key_game.html')
