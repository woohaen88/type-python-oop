class Robot:

    # 클래스 변수
    population = 0

    def __init__(self, name, code):
        self.name = name
        self.code = code
        Robot.population += 1

    def say_hi(self):
        print(f"Greetings, my masers call me {self.name}")

    def cal_add(self, a, b):
        return a + b

    def die(self):
        print(f"{self.name} is being destroyed")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one")
        else:
            print(f"There are still {Robot.population} robot working.")

    @classmethod
    def how_many(cls):
        print(f"we have {cls.population} robot!!")


if __name__ == "__main__":
    print(Robot.population)
    siri = Robot("siri", "123")
    siri.die()

    aa = Robot("haha", "1234")
    aa.how_many()

    bb = Robot("hadha", "1234")
    bb.how_many()
    bb.die()
