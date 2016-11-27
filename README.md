# blablacar_search_trips
Search trips blablacar.ru

## Installing
Before running the script, you must install the packages following items:
```
$ pip install prettytable
```

## Usage
```
$ blablacar.py -f DEPARTURE_PLACE -t ARRIVAL_PLACE
```
Note that you might need to give executable permissions to the file or you can just run:

```
python blablacar.py
```
Optional args:
* **--db** Date begin
* **--de** Date end
* **--hb** Hour begin
* **--he** Hour end
* **--locale** Available locales. Default: ru_RU
* **--cur** Select the currency you want. Default: RUB
* **--sort** Sorting by date or price
* **--order** Order of the sorting
* **--max** Maximum results
* **--radius** Maximum radius of the search

## Examples
* Search trip St. Petersburg - Moscow in the time interval 19: 00-21: 00:
``` bash
$ python blablacar.py -f санк-петербург -t москва --hb 19 --he 21
+---------------------+------------------------+---------------+------------+------------+------------------------------------+
|         Date        |          From          |       To      |   Price    | Seats left |                Car                 |
+---------------------+------------------------+---------------+------------+------------+------------------------------------+
| 27/11/2016 19:00:27 |    Санкт-Петербург     |     Москва    |  1808 RUB  |     4      |   Model: TOURAN/Make: VOLKSWAGEN   |
|                     |          Росія         |      Росія    | (1548+260) |            |                                    |
+---------------------+------------------------+---------------+------------+------------+------------------------------------+
| 27/11/2016 19:10:03 |    Санкт-Петербург     |     Москва    |  1853 RUB  |     2      |                 -                  |
|                     |          Росія         |      Росія    | (1583+270) |            |                                    |
+---------------------+------------------------+---------------+------------+------------+------------------------------------+
| 27/11/2016 19:30:12 |    Санкт-Петербург     |     Москва    |  1390 RUB  |     1      |    Model: PARTNER/Make: PEUGEOT    |
|                     |         Россия         |     Россия    | (1190+200) |            |                                    |
+---------------------+------------------------+---------------+------------+------------+------------------------------------+
| 27/11/2016 20:00:00 |    Метро Московская    |  Охотный Ряд  |  1120 RUB  |     3      |   Model: TOURAN/Make: VOLKSWAGEN   |
|                     |     Санкт-Петербург    |     Москва    | (960+160)  |            |                                    |
|                     |  город Санкт-Петербург |  город Москва |            |            |                                    |
+---------------------+------------------------+---------------+------------+------------+------------------------------------+
| 27/11/2016 20:00:47 |    Санкт-Петербург     |     Москва    |  1260 RUB  |     2      |      Model: ASTRA/Make: OPEL       |
|                     |         Россия         |     Россия    | (1080+180) |            |                                    |
+---------------------+------------------------+---------------+------------+------------+------------------------------------+
| 27/11/2016 20:20:00 |    Санкт-Петербург     |     Москва    |  1260 RUB  |     4      |    Model: BORA/Make: VOLKSWAGEN    |
|                     |  город Санкт-Петербург |  город Москва | (1080+180) |            |                                    |
+---------------------+------------------------+---------------+------------+------------+------------------------------------+
| 27/11/2016 20:20:39 |    Санкт-Петербург     |     Москва    |  1260 RUB  |     4      | Model: Almera Classic/Make: NISSAN |
|                     |         Россия         |     Россия    | (1080+180) |            |                                    |
+---------------------+------------------------+---------------+------------+------------+------------------------------------+
| 27/11/2016 20:30:00 |    Санкт-Петербург     |     москва    |  1390 RUB  |     1      | Model: CARAVELLE/Make: VOLKSWAGEN  |
|                     |  город Санкт-Петербург |               | (1190+200) |            |                                    |
+---------------------+------------------------+---------------+------------+------------+------------------------------------+
| 27/11/2016 20:50:00 |    Санкт-Петербург     |     Москва    |  1390 RUB  |     4      |                 -                  |
|                     |  город Санкт-Петербург |  город Москва | (1190+200) |            |                                    |
+---------------------+------------------------+---------------+------------+------------+------------------------------------+
| 27/11/2016 20:50:00 |    Санкт-Петербург     |     Москва    |  1390 RUB  |     4      |                 -                  |
|                     |  город Санкт-Петербург |               | (1190+200) |            |                                    |
+---------------------+------------------------+---------------+------------+------------+------------------------------------+

```
