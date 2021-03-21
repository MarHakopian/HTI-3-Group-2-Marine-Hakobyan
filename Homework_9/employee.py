from datetime import datetime, date

gender_options = {
    'M': 'Male',
    'F': 'Female',
}
date_formats = ['%d.%m.%Y', '%d/%m/%Y', '%d-%m-%Y']


class Employee:
    def __init__(
            self,
            first_name,
            last_name,
            gender,
            salary,
            join_date,
            leave_date=date.today().strftime("%d-%m-%Y"),
            phone_number=None,
            trial_passed=False
    ):
        self.first_name = first_name
        self.last_name = last_name
        self._gender = None
        self.gender = gender
        self._salary = None
        self.salary = salary
        self._join_date = None
        self.join_date = join_date
        self._leave_date = None
        self.leave_date = leave_date
        self._phone_number = None
        self.phone_number = phone_number
        self.trial_passed = trial_passed
        self._work_email = None

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, value):
        first_name, last_name = value.split()
        self.first_name = first_name
        self.last_name = last_name

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        if value not in gender_options:
            raise ValueError('gender must be M or F')

        self._gender = gender_options[value]

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError('Please include only numbers')
        self._salary = amount

    @property
    def join_date(self):
        return self._join_date

    @join_date.setter
    def join_date(self, raw_date):
        for i in date_formats:
            try:
                self._join_date = datetime.strptime(raw_date, i).date()
                break
            except ValueError:
                pass
        else:
            raise ValueError(
                "Please follow one of these formats '%d.%m.%Y', '%d/%m/%Y', '%d-%m-%Y', when entering any date.")

    @property
    def leave_date(self):
        return self._leave_date

    @leave_date.setter
    def leave_date(self, date_r):
        for i in date_formats:
            try:
                self._leave_date = datetime.strptime(date_r, i).date()
                break
            except ValueError:
                pass
        else:
            raise ValueError(
                "Please follow one of these formats '%d.%m.%Y', '%d/%m/%Y', '%d-%m-%Y', when entering any date.")

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        # if self.is_phone_number(value):
        self._phone_number = value

    @property
    def work_email(self):
        if self._work_email:
            return self._work_email
        return f'{self.first_name.lower()}.{self.last_name.lower()}@company.com'

    @work_email.setter
    def work_email(self, value):
        self._work_email = value

    def __add__(self, other):
        return self.salary + other.salary

    def __radd__(self, other):
        if isinstance(other, int):
            return self.salary + other
        return self.salary + other.salary

    def __repr__(self):
        return f"{self.full_name}, Phone number - {self.phone_number}, Email - {self.work_email}"

    def __lt__(self, other):
        return self.salary < other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __bool__(self):
        return self.leave_date != date.today()

    def __len__(self):
        """ how many days the employee has been working/ worked at the company"""
        exp = self.leave_date - self.join_date
        return exp.days


empl1 = Employee('Davit', 'Tovmasyan', 'M', 150000, '22.02.2018', trial_passed=True, phone_number='077 12 34 56')
empl2 = Employee('Tovmas', 'Davtyan', 'M', 450000, '11.01.2020', leave_date='25.07.2020', trial_passed=False,
                 phone_number='077 12 34 56')

print(empl1)
print(empl2)

if empl2:
    del empl2
# deletes, if the employee left
# print(empl2)
