class snake:
    i_am= "Les enfants terribles"
    def speek(self):
        print(f"I'm {self.i_am}")
    def say_we_are(self):
        print(f"And we are {self.i_am}!")

solid=snake()
solid.i_am= "Solid"
solid.speek()

liquid=snake()
liquid.i_am= "Liquid"
liquid.speek()

solidus=snake()
solidus.i_am= "Solidus"
solidus.speek()

big_boss_sons=snake()
big_boss_sons.say_we_are()