from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.config import Config

Config.set('graphics', 'width', 960)
Config.set('graphics', 'height', 640)


class MyCalcApp(App):
    def build(self):
        """В этой функции мы создаём общий вид нашего приложения
        :cvar
            Answers: Поле с ответами и кнопкой
            AnswersLabel: Поле вывода ответов
            coefField: Поле коэффициентов
            Layout: Поле характеристик матрицы
            Page1: Поле всей страницы
            rowsCount: Поле количества строк
            variableCount: Поле количества переменных
            x: Ширина Матрицы
            y: Высота матрицы
        """
        self.Page1 = BoxLayout(orientation='vertical')
        self.variablesCount = TextInput(text='2')
        self.rowsCount = TextInput(text='2')
        self.x = x = int(self.variablesCount.text) + 1
        self.y = y = int(self.rowsCount.text)
        self.Layout = GridLayout(cols=2, row_force_default=True, row_default_height=30, padding=10)
        submit = Button(text='Подтвердить характеристики системы', on_press=self.submit)
        self.Layout.add_widget(self.variablesCount)
        self.Layout.add_widget(self.rowsCount)
        self.Layout.add_widget(submit)
        self.coefField = GridLayout(cols=x, row_force_default=True, row_default_height=30, padding=10)
        for i in range(x * y):
            self.coefField.add_widget(TextInput(text='0'))
        self.Answers = BoxLayout(padding=10)
        btnCount = Button(text='Решить', height=30, width=120, on_press=self.countAnswers, size_hint=(.4, .3))
        self.AnswersLabel = TextInput(text='Ответ: x1 - любой, x2 - любой.', size_hint=(.8, .3))
        self.Answers.add_widget(btnCount)
        self.Answers.add_widget(self.AnswersLabel)
        self.Page1.add_widget(self.Layout)
        self.Page1.add_widget(self.coefField)
        self.Page1.add_widget(self.Answers)
        return self.Page1

    def submit(self, obj):
        """Эта функция создаёт правильное поле относительно вводимых значений количества переменных и количества уравнений.
                :cvar
                    x: Ширина Матрицы
                    y: Высота матрицы
        """
        self.AnswersLabel.text = 'Ответ: '
        self.x = int(self.variablesCount.text.replace('\n', '')) + 1
        self.y = int(self.rowsCount.text.replace('\n', ''))
        self.variablesCount.text = self.variablesCount.text.replace('\n', '')
        self.rowsCount.text = self.rowsCount.text.replace('\n', '')
        self.coefField.clear_widgets()
        self.coefField.cols = self.x
        for i in range(self.x * self.y):
            self.coefField.add_widget(TextInput())

    def countAnswers(self, obj):
        """Эта функция выводит ответ от функции Gauss() в поле AnswersLabel."""
        mass = []
        for i in self.coefField.children:
            mass.append(i.text)
        mass.reverse()
        mx = []
        for i in range(self.y):
            mx += [[]]
            for j in range(self.x):
                mx[i].append(MyCalcApp.division_converter(self, mass[i * self.x + j]))
        self.AnswersLabel.text = 'Ответ: ' + MyCalcApp.Gauss(self, mx, self.x, self.y)

    def nod_decreaser(self, m):
        """Данная фунция получает на вход список [a, b], являющийся интерпретацией дроби a/b. На выходе функция выдаёт список, НОД чисел которого равен 1.
        Args:
            m (list): Исходная дробь a/b в виде списка [a, b].
        Returns:
            list: Несократимая дробь a/b в виде списка [a, b].
        """
        if m[0] == m[1]:
            return [1, 1]
        elif m[0] == 0:
            return [0, 1]
        else:
            if m[0] < m[1]:
                indicator = 0
            else:
                indicator = -1
            m1 = m[0 + indicator]
            m2 = m[1 + indicator]
            nod = 1
            if m1 * m2 != 0:
                if m2 % m1 == 0:
                    nod = m1
            while m2 % m1 != 0:
                m1, m2 = m2 % m1, m1
            nod = m1
            m1 = int(m[0] / nod)
            m2 = int(m[1] / nod)
            return [m1, m2]

    def number_returner(self, m):
        """Данная функция получает на вход список [a, b], являющийся интерпретацией дроби a/b. На выход возвращается строка 'a/b'.
        Args:
            self: Источник наследования
            m (list): Исходная дробь a/b в виде списка [a, b].
        Returns:
            Строковое значение от числа.
        """
        if m == [0, 1]:
            return '0'
        elif m[1] == 1:
            return str(m[0])
        elif m[1] == -1:
            return str(-1 * m[0])
        elif m[1] <= -1:
            return str(-1 * m[0]) + '/' + str(-1 * m[1])
        else:
            return str(m[0]) + '/' + str(m[1])

    def division_converter(self, number):
        """Эта функция преобразует текстовую запись числа в список [a, b], являющийся интерпретацией дроби a/b.
        Args:
            self: Источник наследования
            number (str): Текстовый формат числа
        Returns:
            Список вида [a, b]
        """
        # вид: 1/2, 0.5, 0,5, 1 1/2, 1+1/2 превратится в [1, 2] или [3, 2]
        if number.count('.') == 1:
            a_before, a_after = number.split('.')
            result = [int(a_after) + int(a_before) * 10 ** len(a_after), 10 ** len(a_after)]
        elif number.count(',') == 1:
            a_before, a_after = number.split(',')
            result = [int(a_after) + int(a_before) * 10 ** len(a_after), 10 ** len(a_after)]
        elif number.count('/') == 1:
            if number.count(' ') == 1:  # 1 1/2
                a_big, a = number.split(' ')
                a_top, a_bottom = a.split('/')
                result = [int(a_big) * int(a_bottom) + int(a_top), int(a_bottom)]
            elif number.count('+') == 1:  # 1+1/2
                a_big, a = number.split('+')
                a_top, a_bottom = a.split('/')
                result = [int(a_big) * int(a_bottom) + int(a_top), int(a_bottom)]
            else:  # 1/2
                a_top, a_bottom = number.split('/')
                result = [int(a_top), int(a_bottom)]
        elif number == '':
            result = [0, 1]
        elif number == str(number):
            result = [int(number), 1]
        else:
            result = number

        # Сокращение дроби
        return MyCalcApp.nod_decreaser(self, result)

    def sorter(self, mx, stro, sto):  # mx -матрица, sto - столбец
        """Данная функция сортирует строки таким образом, что на пересечении рассматриваемых строки stro и столбца sto не будет нуля в виде [0, 1].
        Args:
            self: Источник наследования
            mx (list): Матрица
            stro (int): Номер строки
            sto (int): Номер столбца
        Returns:
            Лист, для которого первая строка не нулевая в определённом столбце
        """
        if mx[stro][sto] != [0, 1]:  # stro - рассматриваемая строка
            return mx
        else:
            flag = True
            for j in range(stro + 1, len(mx)):  # j - искомая строка
                if mx[j][sto] != [0, 1]:
                    mx[j], mx[stro] = mx[stro], mx[j]
                    return mx
                    flag = False
                    break
            if flag:
                return 'Nothing'

    def math(self, a, b):
        """Эта функция получает на вход два списка - дроби, а возвращает список - сумму дробей.
        Args:
            self: Источник наследования
            a, b (list): Дробь m/n вида [m, n]
        Returns:
            Список-сумму дробей
        """
        result = MyCalcApp.division_converter(self, [a[0] * b[1] + b[0] * a[1], a[1] * b[1]])
        return result

    def divider(self, a, b):
        """Эта функция получает на вход два списка - дроби, а возвращает список - частое дробей.
        Args:
            self: Источник наследования
            a, b (list): Дробь m/n вида [m, n]
        Returns:
            Список-частное дробей
        """
        result = MyCalcApp.division_converter(self, [a[0] * b[1], a[1] * b[0]])
        return result

    def multiplier(self, a, b):
        """Эта функция получает на вход два списка - дроби, а возвращает список - произведение дробей.
        Args:
            self: Источник наследования
            a, b (list): Дробь m/n вида [m, n]
        Returns:
            Список-произведение дробей
        """
        result = MyCalcApp.division_converter(self, [a[0] * b[0], a[1] * b[1]])
        return result

    def stro_count(self, mx, i1, i2, x,
                   k):  # mx - матрица, i1 - исходная строка, i2 - побочная строка, x - дл. строки, k - рассм. столбец
        """Эта функция вычитает строку i1 из строки i2 столько раз, чтобы столбец k обнулился.
        Args:
            self: Источник наследования
            mx (list): Матрица
            i1 (int): Номер исходной строки
            i2 (int): Номер побочной строки
            x (int): Длина строки
            k (int): Рассматриваемый столбец
        Returns:
            Список-матрицу, с посчитанной разностью
        """
        c = MyCalcApp.multiplier(self, MyCalcApp.divider(self, mx[i2][k], mx[i1][k]), [-1, 1])
        for i in range(x):
            mx[i2][i] = MyCalcApp.math(self, MyCalcApp.multiplier(self, c, mx[i1][i]), mx[i2][i])
        return mx

    def mx_solver(self, mx, x, y):
        """Данная функция делит на первый ненулевой коэффициент всю строку.
        Args:
            self: Источник наследования
            mx (list): Матрица
            x (int): Количество коэффициентов по ширине
            y (int): Количество уравнений
        Returns:
            Список-матрицу
        """
        for i in range(y):
            for j in range(x):
                if mx[i][j] != [0, 1]:  # поиск ненулевого элемента
                    c = mx[i][j]  # делитель с последующим делением
                    for l in range(j, x):
                        mx[i][l] = MyCalcApp.divider(self, mx[i][l], c)
                    break
        mx = MyCalcApp.reversed_Gauss(self, mx, x, y)
        return mx

    def Gauss(self, mx, x, y):
        """В этой функции реализован метод Гаусса.
        Args:
            self: Источник наследования
            mx (list): Матрица
            x (int): Количество коэффициентов по ширине
            y (int): Количество уравнений
        Returns:
            Упрощённая матрица в виде списка для поиска корней
        """
        i = 0
        k = 0
        while ((i < y) and (k < x)):
            mx1 = MyCalcApp.sorter(self, mx, i, k)
            if mx1 != 'Nothing':
                mx = mx1
                for a in range(i + 1, y):  # вычитание строк в цикле
                    mx = MyCalcApp.stro_count(self, mx, i, a, x, k)
                i += 1
                k += 1
            if mx1 == 'Nothing':
                k += 1
        # частные случаи с нулевыми строчками:
        i = 0
        flag = True
        for a in range(y - 1, -1, -1):
            checker_Summ = 0
            for j in range(x - 1):
                checker_Summ += abs(mx[a][j][0])
            if checker_Summ == 0 and mx[a][x - 1][0] == 0 and len(mx) > 1:
                mx.pop(a)
                a -= 1
            elif checker_Summ == 0 and mx[a][x - 1][0] != 0:
                flag = False
                return 'Данная система не имеет решений'
        mx = MyCalcApp.mx_solver(self, mx, len(mx[0]), len(mx))
        basis = mx[-1][0]
        variables = ['x' + str(i + 1) for i in range(x - 1)]
        answers = ''
        if mx == [[0, 1]] * x:
            for i in range(len(variables) - 1):
                answers += variables[i] + ' ∈ ℝ, '
            answers += variables[-1] + '.'
        elif flag:
            mx.pop(-1)
            results = []
            a = 0  # переменная
            i = 0  # строка
            while (a < x - 1):
                res = variables[a]
                j = a + 1
                if basis[a] == 0:
                    i -= 1
                    res += ' - любой'  # ∈ ℝ
                else:
                    res += ' = ' + MyCalcApp.number_returner(self, mx[i][-1])
                    while (j < x - 1):
                        updater = MyCalcApp.number_returner(self, MyCalcApp.multiplier(self, mx[i][j], [-1, 1]))
                        if updater != '0':
                            res += ' + ' + updater + '*' + variables[j]
                        j += 1
                i += 1
                a += 1
                res = res.replace('= 0 + ', '= ')
                res = res.replace(' 1*x', ' x')
                res = res.replace(' -1*x', ' -x')
                res = res.replace('+ -', '- ')
                results += res,
            for i in range(len(results) - 1):
                answers += results[i] + ', '
            answers += results[-1] + '.'
        return (answers)

    def reversed_Gauss(self, mx, x, y):
        """Эта функция освобождает матрицу от ненужных элементов методом Гаусса, но снизу-вверх.
        Args:
            self: Источник наследования
            mx (list): Матрица
            x (int): Количество коэффициентов по ширине
            y (int): Количество уравнений
        Returns:
            Список-матрицу, для которой убираются ненужные элементы
        """
        basis = []
        answers = []
        k = 0
        i = 0
        while ((i < y) and k < x):
            if mx[i][k] == [1, 1]:
                basis += 1,
                i += 1
                k += 1
            else:
                basis += 0,
                k += 1
        if len(basis) < x - 1:
            basis += [0] * (x - len(basis) - 1)  # исключение бага, когда теряются переменные в массиве
        basis += 'b',
        for i in range(y):
            answers += [[]]
            for j in range(x):
                if basis[j] == 1 or basis[j] == 'b':
                    answers[i] += [mx[i][j]]
        free_var = basis.count(1)
        k = free_var
        for j in range(free_var - 1, 0, -1):
            k -= 1
            for i in range(j - 1, -1, -1):
                answers = MyCalcApp.stro_count(self, answers, j, i, free_var + 1, k)
        k = x - 1
        a = 0
        i1 = y - 1
        while (i1 > 0):
            k -= 1
            if basis[k] != 0:
                for i2 in range(i1 - 1, -1, -1):
                    mx = MyCalcApp.stro_count(self, mx, i1, i2, x, k)
                i1 -= 1
        return mx + [[basis]]

    def input_decide(self):  # возможности к расширению
        """Консольная вариация программы.
        Args:
            self: Источник наследования
        """
        m = input('Введите ID команды: ')
        if m == '0':
            y, x = input('Введите количество строк и количество переменных через <, >: ').split(', ')
            x = int(x) + 1
            y = int(y)
            a = []
            for i in range(y):
                stroka = input(
                    'Введите коэффициенты переменных и свободный член строки №{} через <, >: '.format(str(i + 1)))
                m = [str(i) for i in stroka.split(', ')]
                a += [m]
                for j in range(x):
                    a[i][j] = MyCalcApp.division_converter(self, a[i][j])
            print('\nОтвет:', MyCalcApp.Gauss(self, a, x, y), '\n')
        else:
            print('\nВашего ID нет в перечне\n\nСправочник по ID:\n'
                  '0 - Нахождение корней системы линейных уравнений\n'
                  '1 - Нахождение определителя квадратной матрицы (в разработке)\n')  # пример для расширения
            MyCalcApp.input_decide()
        Continue = input('Продолжить? (да/нет): ')
        if Continue == 'да' or Continue == 'ДА' or Continue == 'Да' or Continue == '1':
            print('')
            MyCalcApp.input_decide()


if __name__ == '__main__':
    MyCalcApp().run()
