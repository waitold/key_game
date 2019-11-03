from django.shortcuts import render, redirect
import random

# Create your views here.


def init_game(request):
    request.session['correct_num'] = random.randrange(10)
    request.session['top'] = 0
    request.session['play_limit'] = 3
    return redirect('key_game')


def key_game(request):
    if request.session.get('correct_num') is None:  # セッションを持っていなければゲームを初期化
        init_game(request)

    if request.session.get('direction') is None:
        direction = ["right", "left"]
        print("direction is " + direction[(random.randrange(2))])
        request.session['direction'] = direction[random.randrange(2)]

    if request.method == 'POST':
        if request.session.get('correct_num') == int(request.POST['key_value']) and \
                request.session.get('direction') == request.POST['right_or_left']:
            return render(request, "keygame/key_game.html",
                          {'right': 1, 'play_limit': request.session.get('play_limit')})

        elif inc_ans(rotate_dial(request.session.get('top'), int(request.POST['key_value']),
                                 request.session.get('direction')), request.session.get('correct_num')):
            return render(request, 'keygame/key_game.html',
                          {'near': 1, 'play_limit': request.session.get('play_limit')})

        else:
            return render(request, 'keygame/key_game.html',
                          {'miss': 1, 'play_limit': request.session.get('play_limit')})

    return render(request, 'keygame/key_game.html', {'play_limit': request.session.get('play_limit')})


def rotate_dial(top, target, direction):
    if direction == "right":
        if top - target <= 0:
            return list(map(lambda num: num % 10, list(range(top+10, target-1, -1))))
        else:
            return list(range(top, target, -1))

    elif direction == "left":
        if target - top <= 0:
            return list(map(lambda num: num % 10, list(range(top, target+9))))
        else:
            return list(range(top, target))
    else:
        print('unti')
        print(direction)


def inc_ans(key_list, ans):
    print(key_list)
    if ans in key_list:
        return True
    else:
        return False
