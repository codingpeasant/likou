# DD上的每家店铺有自己的营业时间，以"mon 2:02 pm"或者"wed 00:13 am"这样的格式来显示开门和关门时间。
# 店铺营业期间，DD会每隔5分钟给外卖小哥发消息，提醒可能会出现的订单；而且发消息时的分钟数一定是5的倍数。例如，店铺A营业期间，DD在xx:00会发一次通知；xx:05的时候再发一次；xx:10再发一次；以此类推。
# DD会一直给外卖小哥发消息，直到店铺关门才停止。
# 以某一家店铺的开门时间为例，如果这家店铺开门时间的分钟数不是5的倍数，DD会选择一个离开门时间最近的时候来发送消息。例如，店铺A今天的开门时间是10:03 AM，DD会在10:05 AM的时候发出第一条消息（因为10:05比10:00距离开门时间更近）。 又比如说店铺A今天的开门时间是10:02 AM，DD会在10:00 AM发出第一条消息，即使店铺A实际上还没有开门。
# 关门时间同理：例如，店铺A今天的关门时间是11:03 PM，DD会在11:05 PM的时候发出最后一条消息，即使店铺A实际上已经关门。又比如说店铺A今天的关门时间是11:02 PM，DD会在11:00 PM发出最后一条消息。

# 现在希望能写一个function：
# 输入是一家店铺的开门时间，"xxx xx:xx xx", 和关门时间，"xxx xx:xx xx"；
# 要求输出一个List，里面是DD为这家店铺发出通知的所有时间（time intervals）。

# 例子1：
# openTime = "mon 10:01 am", closeTime = "mon 10:10 am";
# output = {"11000", "11005", "11010"}.


class Clock:
    dayToNum = {"mon": 1, "tue": 2, "wed": 3, "thu": 4, "fri": 5, "sat": 6, "sun": 7}

    def __init__(self, inputTime: str):
        timeTokens = inputTime.split(" ")
        hourMin = timeTokens[1].split(":")
        self.day = Clock.dayToNum[timeTokens[0]]
        hour = int(hourMin[0])
        self.hour = hour if timeTokens[2] == "am" else hour % 12 + 12
        minute = int(hourMin[1])
        remainder = minute % 5
        self.minute = minute - remainder if remainder < 3 else minute + 5 - remainder

    def addFive(self):
        self.minute = (self.minute + 5) % 60
        if self.minute == 0:
            self.hour = (self.hour + 1) % 24
            if self.hour == 0:
                self.day = (self.day + 1) % 7

    def theSame(self, inputClock: "Clock"):
        return (
            self.minute == inputClock.minute
            and self.hour == inputClock.hour
            and self.day == inputClock.day
        )

    def __str__(self):
        print(self.day, self.hour, self.minute)
        hour = str(self.hour) if self.hour >= 10 else "0" + str(self.hour)
        minute = str(self.minute) if self.minute >= 10 else "0" + str(self.minute)
        return str(self.day) + hour + minute


class Solution:
    def getAllTimes(self, startTime: str, endTime: str) -> list:
        res = []
        startClock = Clock(startTime)
        endClock = Clock(endTime)

        while not endClock.theSame(startClock):
            res.append(startClock.__str__())
            startClock.addFive()
        res.append(startClock.__str__())

        return res


s = Solution()
print(s.getAllTimes("mon 10:01 am", "mon 10:13 am"))
