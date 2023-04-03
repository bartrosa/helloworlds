from random import randint


data = {
    0: [
        'Ja chcę powiedzieć jedną rzecz: ',
        'Trzeba powiedzieć jasno: ',
        'Jak powiedział wybitny krakowianin Stanisław Lem, ',
        'Proszę mnie dobrze zrozumieć: ',
        'Ja chciałem państwu przypomnieć, że ',
        'Niech państwo nie mają złudzeń: ',
        'Powiedzmy to wyraźnie: '
    ],
    1: [
        'przedstawiciele czerwonej hołoty ',
        'ci wszyscy (tfu!) geje ',
        'funkcjonariusze reżymowej telewizji ',
        'tak zwani ekolodzy ',
        'ci wszyscy (tfu!) demokraci ',
        'agenci bezpieki ',
        'feminazistki '
    ],
    2: [
        'zupełnie bezkarnie ',
        'całkowicie bezczelnie ',
        'o poglądach na lewo od komunizmu ',
        'celowo i świadomie ',
        'z premedytacją ',
        'od czasów Okrągego Stołu ',
        'w ramach postępu '
    ],
    3: [
        'nawołują do podniesienia podatków',
        'próbują wyrzucić kierowców z miast',
        'próbują skłócić Polskę z Rosją',
        'głoszą brednie o globalnym ociepleniu',
        'zakazują posiadania broni',
        'nie dopuszczają prawicy do władzy',
        'uczą dzieci homoseksualizmu'
    ],
    4: [
        ', bo dzięki temu mogą kraść ',
        ', bo dostają za to pieniądze ',
        ', bo tak się uczy w państwowej szkole ',
        ', bo bez tego (tfu!) demokracja nie może istnieć ',
        ', bo głupich jest więcej niż mądrych ',
        ', bo chcą tworzyć raj na ziemi ',
        ', bo chcą niszczyć cywilizację białego człowieka '
    ],
    5: [
        'przez kolejne kadencje.',
        'o czym się nie mówi.',
        'i właśnie dlatego Europa umiera.',
        'ale przyjdą muzułmanie i zrobią porządek.',
        '- tak samo zresztą jak za Hitlera.',
        '- proszę zobaczyć, co się dzieje na Zachodzie, jeśli mi państwo nie wierzą.',
        'co lat temu sto nikomu nie przyszłoby nawet do głowy.'
    ]
}


def print_quote(quote):
    print(f'Korwa dziś powiedział, że: "{quote}"\n')


def generate_quote(seed):
    return ''.join([seed[i][randint(0, 6)] for i in seed.keys()])


if __name__ == '__main__':
    print_quote(generate_quote(data))
