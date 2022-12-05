from shop.models import Item, Purchase


item1 = Item.objects.create(name='Футболка', price=1000)

item1.purchases.create(name='Алымбеков Мырза', age=25)
item1.purchases.create(name='Мамбетов Курбан', age=26)

item2 = Item.objects.create(name='Куртка', price=2500)

item2.purchases.create(name='Жолдошбек уулу Адиль', age=24)
item2.purchases.create(name='Майрамбек уулу Автандил', age=27)

item3 = Item.objects.create(name='Шарф', price=800)

item3.purchases.create(name='Алымбеков Амантур', age=29)
item3.purchases.create(name='Татыбеков Бакыт', age=53)

item4 = Item.objects.create(name='Свитер', price=1800)

item4.purchases.create(name='Даулет', age=16)
item4.purchases.create(name='Мамбет', age=30)

item5 = Item.objects.create(name='Джинсы', price=2100)

item5.purchases.create(name='Алымбеков Мырза', age=25)
item5.purchases.create(name='Мамбетов Курбан', age=26)

item6 = Item.objects.create(name='Туфли', price=4000)

item6.purchases.create(name='Алманбет', age=45)
item6.purchases.create(name='Кубинский', age=34)

item7 = Item.objects.create(name='Кроссовки', price=3400)

item7.purchases.create(name='Жолдошбек уулу Адиль', age=25)
item7.purchases.create(name='Месси', age=35)

item8 = Item.objects.create(name='Кепка', price=700)

item8.purchases.create(name='Мамбет', age=25)
item8.purchases.create(name='Иманбек', age=22)

item9 = Item.objects.create(name='Рубашка', price=1600)

item9.purchases.create(name='Алымбеков Мырза', age=25)
item9.purchases.create(name='Мамбетов Курбан', age=26)

item10 = Item.objects.create(name='Перчатки', price=500)

item10.purchases.create(name='Алымбеков Мырза', age=25)
item10.purchases.create(name='Мамбет', age=30)
