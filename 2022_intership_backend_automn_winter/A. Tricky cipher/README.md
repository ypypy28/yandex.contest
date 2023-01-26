# A. Хитрый шифр

Известная компания Тындекс в очередной раз проводит набор стажёров.
Заботясь о персональных данных соискателей, компания придумала хитрый алгоритм шифрования:

- Подсчитывается количество различных символов в ФИО (регистр важен, А и а — разные символы).
- Берётся сумма цифр в дне и месяце рождения, умноженная на 64.
- Для первой (по позиции в слове) буквы фамилии определяется её номер в алфавите (в 1-индексации), умноженный на 256 (регистр буквы не важен).
- Полученные числа суммируются.
- Результат переводится в 16-чную систему счисления (__в верхнем регистре__).
- У результата сохраняются только 3 младших разряда (если значимых разрядов меньше, то шифр дополняется до 3-х разрядов ведущими нулями).

Ваша задача — помочь вычислить для каждого кандидата его шифр.


## Формат ввода

В первой строке вводится число _N_ (1 ≤ _N_ ≤ 10 000) — количество кандидатов и шифров.
Далее следует _N_ строк в формате CSV (_f<sub>j</sub>_, _i<sub>j</sub>_, _o<sub>j</sub>_, _d<sub>j</sub>_, _m<sub>j</sub>_, _y<sub>j</sub>_) — информация о кандидатах:

- Фамилия _f<sub>j</sub>_, имя _i<sub>j</sub>_, и отчество _o<sub>j</sub>_ (1 ≤ |_f<sub>j</sub>_|, |_i<sub>j</sub>_|, |_o<sub>j</sub>_|  ≤ 15) — строки, состоящие из латинских букв верхнего и нижнего регистра;
- день рождения _d<sub>j</sub>_, месяц рождения _m<sub>j</sub>_, и год рождения _y<sub>j</sub>_ — целые числа, задающие __корректную__ дату в промежутке от 1 января 1950 года до 31 декабря 2021 года.


## Формат вывода

В единственной строке выведите _N_ строк _k<sub>1</sub>_, _k<sub>2</sub>_, ..., _k<sub>Т</sub>_, где _k<sub>j</sub>_ — шифр _j_-го кандидата (__в верхнем регистре__). Кандидаты нумеруются с 1 до _N_ в порядке ввода.
