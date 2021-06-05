

import random
channel = int(input('Wellcome to our TV!\n Please choose your channel ')) - 1 #so the channels will start from 1, not 0
class TVController:
    def __init__(self):
        self.Channels = ["BBC", "Discovery", "TV1000"]
    def first_channel(self):
        print('The first channel is:', self.Channels[0])
    def last_channel(self):
        print('The last channel is:', self.Channels[len(self.Channels) - 1])
    def turn_channel(self) -> str:
        print(f'You turned the channel № {channel + 1}', self.Channels[channel])
        return  self.Channels[channel]
    def current_channel(self):
        print('Your current channel is', self.Channels[channel])
    def previous_channel(self):
         print('The previous channel is', self.Channels[channel - 1])
    def is_exist(self, kvargs):
        if kvargs in self.Channels:
            print('Yes')
        elif kvargs <= len(self.Channels):
            print('yes')
        else:
            print('NO!')
class Volume:
    def __init__(self):
        self.defult = 50
    def lower(self, n):
        if n <50:
            self.defult = self.defult - n
            print(f'your volume dropped to {self.defult}')
        else:
            raise Exception ('muted')
    def upper(self, n: int):
        if n<50:
            self.defult = self.defult + n
            print(f'the volume has been raised by {self.defult}')
        else:
            raise Exception ('too loud')


class Battery:
    def __init__(self):
        self.charge_level = 100

def discharge(self):
    new_charge_level = random.randint(self.charge_level - 10, self.charge_level - 1)
    if new_charge_level > 0:
        self.charge_level = new_charge_level
    else:
        raise Exception('Battery has run out of charge. Please put new one.')



TV = TVController()
TV.first_channel()
TV.last_channel()
TV.turn_channel()
TV.current_channel()
TV.previous_channel()
TV.is_exist('BBC')
TV.is_exist(4)
print ('')
vol = Volume
vol.upper(25)
vol.lower(10)



