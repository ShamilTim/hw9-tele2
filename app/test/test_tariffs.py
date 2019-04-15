from app.tariffs import Tariff, TariffManager


def test_actual_and_archived():
    manager = TariffManager()
    my_talk = Tariff('Мой разговор', price=190, gb=3, minutes=250)
    my_tele2 = Tariff('Мой Теле2', price=7, price_period='day', gb=6)
    univer = Tariff('Универ', price=None, minutes_unlim_tele2=None, archived=True)
    my_start = Tariff('Мой старт', price=99, gb=2, minutes=100, minutes_unlim_tele2=False, archived=True)
    manager.add(my_talk)
    manager.add(my_tele2)
    manager.add(univer)
    manager.add(my_start)
    actual = manager.actual()
    archived = manager.archived()
    assert [my_talk, my_tele2] == actual
    assert [univer, my_start] == archived
