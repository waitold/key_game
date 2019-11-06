from django.shortcuts import render, redirect
import random

# Create your views here.


def init_game(request):
    request.session['correct_num'] = random.randrange(10)
    request.session['top'] = 0
    request.session['play_limit'] = 5
    direction = ["right", "left"]
    print("direction is " + direction[(random.randrange(2))])
    request.session['direction'] = direction[random.randrange(2)]
    return redirect('key_game')


def key_game(request):

    correct_dir = request.session.get('direction')
    correct_num = request.session.get('correct_num')
    top = request.session.get('top')

    if correct_num is None or correct_dir is None:  # セッションを持っていなければゲームを初期化
        init_game(request)

    if request.method == 'POST' and request.session.get('play_limit') > 0:

        request.session['play_limit'] = request.session.get('play_limit') - 1
        play_limit = request.session.get('play_limit')
        ans_key = int(request.POST['key_value'])
        ans_dir = request.POST['right_or_left']
        print(ans_dir)

        if correct_num == ans_key and correct_dir == ans_dir:  # 正解時
            return render(request, "keygame/key_game.html", {'correct': 1, 'play_limit': play_limit})

        elif inc_ans(rotate_dial(top, ans_key, ans_dir), correct_num) and correct_dir == ans_dir:  # 回転させた中に答えがあった場合
            request.session['top'] = ans_key
            return render(request, 'keygame/key_game.html', {'near': 1, 'play_limit': play_limit,
                                                             'top': ans_key, 'dir': ans_dir})

        else:
            request.session['top'] = ans_key
            return render(request, 'keygame/key_game.html', {'miss': 1, 'play_limit': play_limit,
                                                             'top': ans_key, 'dir': ans_dir})

    elif request.session.get('play_limit') == 0:
        return render(request, 'keygame/key_game.html', {'game_over': 1})

    else:
        # セッションを保持してる状態でリロードした場合プレイ回数を減らさないための処理
        return render(request, 'keygame/key_game.html', {'play_limit': request.session.get('play_limit'), 'top': top})


# 現在のダイアル位置topからtargetまでダイアルを回したときに含む番号をリストとして取得
def rotate_dial(top, target, direction):
    if direction == "right":
        if top - target <= 0:
            return list(map(lambda num: num % 10, list(range(top+9, target+1, -1))))
        else:
            return list(range(top, target+1, -1))

    elif direction == "left":
        if target - top <= 0:
            return list(map(lambda num: num % 10, list(range(top+1, target+10))))
        else:
            return list(range(top+1, target))


def inc_ans(key_list, ans):
    print(key_list)
    if ans in key_list:
        return True
    else:
        return False
