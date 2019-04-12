import os

import waitress
from flask import Flask, render_template

from app.tariffs import TariffManager, Tariff


def start():

    app = Flask(__name__)

    manager = TariffManager()
    my_online = Tariff('Мой Онлайн', price=290, hit=True, gb=15, gb_unlim=['vk', 'fb'], minutes=400)
    my_online_plus = Tariff('Мой Онлайн+', price=390, gb=20, gb_unlim=['vk', 'fb'], minutes=600)
    my_talk = Tariff('Мой разговор', price=190, gb=3, minutes=250)
    my_tele2 = Tariff('Мой Теле2', price=7, price_period='day', gb=6)
    unlim = Tariff('Безлимит', price=350, gb=-1, minutes=500, sms=50)
    premium = Tariff('Премиум', price=1100, gb=40, minutes=2000, sms=500)
    classic = Tariff('Классический', price=0, minutes_unlim_tele2=False)
    univer = Tariff('Универ', price=None, minutes_unlim_tele2=None, archived=True)
    my_start = Tariff('Мой старт', price=99, gb=2, minutes=100, minutes_unlim_tele2=False, archived=True)

    manager.add(my_online)
    manager.add(my_online_plus)
    manager.add(my_talk)
    manager.add(my_tele2)
    manager.add(unlim)
    manager.add(premium)
    manager.add(classic)
    manager.add(univer)
    manager.add(my_start)

    @app.route('/')
    def index():
        actual = manager.actual()
        return render_template('index.html', actual=actual)

    @app.route('/archive')
    def archive():
        archived = manager.archived()
        return render_template('archive.html', archived=archived)

    if os.getenv('APP_ENV') == 'PROD' and os.getenv('PORT'):
        waitress.serve(app, port=os.getenv('PORT'))
    else:
        app.run(port=9876, debug=True)


if __name__ == '__main__':
    start()
