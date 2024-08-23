from faker import Faker


class DataGenerator:
    def __init__(self):
        self.fake = Faker(["ru_RU"])
        self.email = ""
        self.name = ""
        self.first_name = ""
        self.last_name = ""
        self.password = ""

        self.new_email()
        self.new_name()
        self.new_password()

    def new_name(self):
        self.first_name = self.fake.first_name_male().replace("-", "")
        self.last_name = self.fake.last_name_male().replace("-", "")
        self.name = self.first_name + " " + self.last_name
        return self.name

    def new_email(self):
        self.email = self.fake.email()
        return self.email

    def new_password(self):
        self.password = self.fake.password(length=8, special_chars=False)
        return self.password
