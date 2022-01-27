

class Sign:

    alert_algorithm_title = '\nBEM-VINDO AO IDENTIFICADOR DE SIGNOS\n'
    alert_algorithm_question = 'Should the algorithm run?\n'
    alert_make_algorithm_start = 'Para continuar: aperte "1" ou qualquer outra tecla \n'
    alert_make_algorithm_cease = 'Para sair: aperte "0" \n'

    alert_instructions = '\nINSTRUCTIONS\n'
    alert_day = '1 - Provide the day you were born \n'
    alert_month = '2 - Provide the month you were born \n'
    alert_year = '3 - Provide the year you were born\n'
    alert_algorithm_procedures = "4 - The algorithm will return user's sign and time of existence\n"

    alert_input_name = '\nProvide input: NAME\n'
    alert_input_name_instruction = 'Digite somente letras, SEM caracteres especiais\n'

    alert_input_first = '\nProvide input: BIRTH DAY\n'
    alert_input_first_instruction = 'Digite um valor entre 1 até 31\n'

    alert_input_second = 'Provide input: BIRTH MONTH\n'
    alert_input_second_instruction = 'Digite um valor entre 1 até 12\n'

    alert_input_third = 'Provide input: BIRTH YEAR\n'
    alert_input_third_instruction = 'Digite um valor entre 1 até 9999\n'

    alert_ok = '\nObrigado por informar, vamos ao próximo passo.\n'
    alert_not_ok = '\nVocê não forneceu o dado esperado.\n'

    alert_where_to_type = 'Por favor, digite após a seta -----> '
    alert_shutdown = '\nAlgorithm has been shut.'

    alert_report = \
        """
        ========== REPORT ==========
        Your birth      || {}
        Your sign       || {}
        Your days alive || {}
        """

    @staticmethod
    def ink(text: str):

        from random import choice

        inks: tuple = (
            '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m',
            '\033[1:37m', '\033[1:38m',
        )

        return f"{choice(inks)}{text}{inks[-1]}"

    @staticmethod
    def skip_line(text):
        return '\n' + text

    @staticmethod
    def indented(text):
        return '    ' + text

    @staticmethod
    def launch_algorithm(text_instruction, breaker, text_closure):

        launcher = input(text_instruction)
        for data in breaker:
            if launcher == data:
                print(Sign.ink(text=text_closure))
                return True
        return None

    @staticmethod
    def get_name(text_instruction, message_success, message_error):

        allowed = [
            ' ',
            *'a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z'.split('.'),
            *'a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z'.upper().split('.')
        ]

        yes = 0
        no = 0

        while True:

            this_input = input(text_instruction)
            for letter in this_input:
                if letter in allowed:
                    yes += 1
                else:
                    no += 1

            if no != 0:
                print(message_error)
                yes = 0
                no = 0
            else:
                print(message_success)
                return this_input

    @staticmethod
    def get_input(text_instruction, integer_based, from_integer, to_integer, message_success, message_error):

        while True:
            if integer_based:
                box = tuple(range(from_integer, to_integer + 1))
                box_str = tuple(str(number) for number in box)

                this_input = input(text_instruction)
                if this_input in box_str:
                    print(message_success)
                    return this_input
                else:
                    print(message_error)

    @staticmethod
    def get_birthday_data(year: int = 1, month: int = 1, day: int = 1):

        from datetime import datetime

        the_birthday = datetime(year=year, month=month, day=day)

        return the_birthday

    @staticmethod
    def get_birthday_str(year: int = 1, month: int = 1, day: int = 1):

        the_birthday_srt = f'{year}/{month}/{day}'

        return the_birthday_srt

    @staticmethod
    def get_lifetime(day_were_born):
        from datetime import datetime
        today_data = datetime.today()
        today = datetime(year=today_data.year, month=today_data.month, day=today_data.day)
        calculus = today - day_were_born
        calculus = f'{str(calculus).split()[0]} days'
        return calculus

    @staticmethod
    def find_sign(day, month):

        each_sign_first_month_days = (
            range(22, 32), range(21, 32), range(19, 32), range(21, 32), range(21, 32), range(21, 32),
            range(21, 32), range(23, 32), range(23, 32), range(23, 32), range(23, 32), range(22, 32)
        )

        each_sign_second_month_days = (
            range(1, 21), range(1, 19), range(1, 21), range(1, 21), range(1, 21), range(1, 21),
            range(1, 23), range(1, 23), range(1, 23), range(1, 23), range(1, 22), range(1, 22)
        )

        each_sign_first_month = (12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
        each_sign_second_month = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

        signs: tuple = (
            'Capricorn', 'Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini',
            'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Saggitarius')

        index = 0
        while index < len(signs):

            if day in each_sign_first_month_days[index] and month == each_sign_first_month[index] \
             or day in each_sign_second_month_days[index] and month == each_sign_second_month[index]:

                return signs[index]

            else:
                index += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_value):
        self.__name = new_value

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, new_value):
        self.__birthday = new_value

    def __init__(self, name, birthday):
        self.__name = name
        self.__birthday = birthday

    @staticmethod
    def mysql_init(box: tuple):
        """
        :param box: tuple with string data with this order: nome of the host, username, password, name of the database
        :return:
        """
        import mysql.connector as mysql

        instance_ = mysql.connect(host=box[0], username=box[1], password=box[2], database=box[3])
        command_ = instance_.cursor()
        return instance_, command_

    @staticmethod
    def mysql_insert_object(_instance, _exec, *args):
        _arguments = args
        _syntax = "INSERT INTO pessoas (nome, nascimento) VALUES (%s, %s)"
        _exec.execute(_syntax, _arguments)
        _instance.commit()

    @staticmethod
    def mysql_select_table(_exec, temporary_database):
        _exec.execute('SELECT * FROM pessoas;')
        for data in _exec:
            temporary_database.append(data)

    # TODO: Método que varia dados [indexes & json_table] de acordo com a quantidade de campos que uma tabela possui
    # Var [ indexes ] relaciona o número de campos que o banco de dados possui
    @staticmethod
    def json(target_table, json_table):

        index_counter = 0
        indexes = (0, 1, 2)  # índices aninhados que serão chamados no loop

        while index_counter < len(target_table):
            json_table.append(
                {
                    "id": target_table[index_counter][indexes[0]],
                    "nome": target_table[index_counter][indexes[1]],
                    "nascimento": target_table[index_counter][indexes[2]],
                }
            )

            index_counter += 1


if __name__ == '__main__':

    mysql_instance, mysql_cursor = Sign.mysql_init(box=('localhost', 'lucasf1', 'mysqluser1', 'lucasf1_bdd_1st'))

    message_welcome = Sign.ink(Sign.alert_algorithm_title)

    block_id = (
        Sign.ink(Sign.alert_input_name),
        Sign.alert_input_name_instruction,
        Sign.alert_where_to_type,
    )

    block_1 = (
        Sign.ink(Sign.alert_algorithm_question),
        Sign.alert_make_algorithm_start,
        Sign.alert_make_algorithm_cease,
        Sign.alert_where_to_type
    )

    block_2 = (
        Sign.ink(Sign.alert_instructions),
        Sign.alert_day,
        Sign.alert_month,
        Sign.alert_year,
        Sign.alert_algorithm_procedures,
    )

    block_3 = (
        Sign.ink(Sign.alert_input_first),
        Sign.alert_input_first_instruction,
        Sign.alert_where_to_type
    )

    block_4 = (
        Sign.ink(Sign.alert_input_second),
        Sign.alert_input_second_instruction,
        Sign.alert_where_to_type
    )

    block_5 = (
        Sign.ink(Sign.alert_input_third),
        Sign.alert_input_third_instruction,
        Sign.alert_where_to_type
    )

    while True:
        print(message_welcome)

        decision = Sign.launch_algorithm(text_instruction=block_1[0] + block_1[1] + block_1[2] + block_1[3],
                                         breaker=('0',),
                                         text_closure=Sign.ink(Sign.alert_shutdown))

        if decision:
            break
        print(block_2[0] + block_2[1] + block_2[2] + block_2[3] + block_2[4])

        the_name = Sign.get_name(text_instruction=block_id[0] + block_id[1] + block_id[2],
                                 message_success=Sign.ink(Sign.alert_ok),
                                 message_error=Sign.ink(Sign.alert_not_ok))

        if the_name:

            the_day = Sign.get_input(text_instruction=block_3[0] + block_3[1] + block_3[2],
                                     integer_based=True,
                                     from_integer=1,
                                     to_integer=31,
                                     message_success=Sign.ink(Sign.alert_ok),
                                     message_error=Sign.ink(Sign.alert_not_ok))

            the_month = Sign.get_input(text_instruction=block_4[0] + block_4[1] + block_4[2],
                                       integer_based=True,
                                       from_integer=1,
                                       to_integer=12,
                                       message_success=Sign.ink(Sign.alert_ok),
                                       message_error=Sign.ink(Sign.alert_not_ok))

            the_year = Sign.get_input(text_instruction=block_5[0] + block_5[1] + block_5[2],
                                      integer_based=True,
                                      from_integer=1,
                                      to_integer=9999,
                                      message_success=Sign.ink(Sign.alert_ok),
                                      message_error=Sign.ink(Sign.alert_not_ok))

            the_day, the_month, the_year = int(the_day), int(the_month), int(the_year)

            birthday_data = Sign.get_birthday_data(year=the_year, month=the_month, day=the_day)
            birthday_str = Sign.get_birthday_str(year=the_year, month=the_month, day=the_day)
            days_alive = Sign.get_lifetime(day_were_born=birthday_data)
            user_sign = Sign.find_sign(day=the_day, month=the_month)

            print(Sign.alert_report.format(birthday_str, user_sign, days_alive))

            # TODO: Objeto
            new_person = Sign(name=the_name, birthday=birthday_str)

            # TODO: Adição do objeto ao bdd
            table_pessoas = []
            table_pessoas_json = []

            # Inserção dos atributos de instância aos campos do banco
            Sign.mysql_insert_object(mysql_instance, mysql_cursor, new_person.name, new_person.birthday)
            # Transferência dos dados no cursor (SELECT * from nome_tabela) para uma var lista separada
            Sign.mysql_select_table(_exec=mysql_cursor, temporary_database=table_pessoas)
            # Conversão dessa lista de tupla para lista de dicionários
            Sign.json(target_table=table_pessoas, json_table=table_pessoas_json)
            # break
