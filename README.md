# Скрипт для анализа результатов
Скрипт написан для программно-аппаратного комплекса для реабилитации пациентов с нарушением координации.

Разработано в рамках написания ВКР для степени магистра.

## Описание
Скрипт нужен для того, чтобы вычислить точку центра давления (среднее между центрами давления каждой из стелек с учётом распределения веса на каждой из ног), считает метрики и строит статокинезиограмму для визуального представления результата.
Расчёт точки центра давления происходит по следующей формуле:
<img width="516" alt="image" src="https://github.com/KostarevVI/smart-foot-data-analysis/assets/22761161/29bd7637-dd6f-40ef-8409-aeba6be68678">

В качестве метрик для тестирования разработанного решения использовались выбор площади эллипса (EA) и среднеквадратичного отклонения наклона тела (RMS) в передне-заднем (A/P) и медиально-латеральном (M/L) направлениях. Уменьшение метрик  свидетельствует о лучшем контроле равновесия и точности движений.

## Использование
1. Создать и внести в файлы data_left/right.txt координаты точек (x,y) и фактор давления (f) левого/правого модуля-стельки в соответственно, формат - "x,y,f" и каждая записей на новой строке
2. Установить зависимости командой `pip3 install -r requirements.txt`
3. Запустить скрипт вычисления траектории центра давления командой `python3 mid_points.py`
4. Запустить скрипт расчёта метрик и построения статокинезиограммы командой `python3 plot.py`
