import random
class Battery:
    def __init__(self):
        self.charge_level = 100


    def discharge(self):
        new_charge_level = random.randint(self.charge_level - 10, self.charge_level - 1)
        if new_charge_level > 0:
            self.charge_level = new_charge_level
        else:
            raise Exception('Battery has run out of charge. Please put new one.')
        print(new_charge_level)
bt_obj = Battery()

bt_obj.discharge()
