class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.cur = -1
        self.values = []
        self.transactions = []
        self.undos = 0
        

    def add(self, num: int):
        self.value += num

        if self.cur == -1 or len(self.values) == self.cur+1:
            self.values.append(self.value)
            self.transactions.append(num)
        else:
            self.values[self.cur + 1]  = self.value
            self.transactions[self.cur + 1] = num
            self.undos += 1

        self.cur += 1

    def subtract(self, num: int):
        self.value -= num

        if self.cur == -1 or len(self.values) == self.cur+1:
            self.values.append(self.value)
            self.transactions.append(-num)
        else:
            self.values[self.cur + 1]  = self.value
            self.transactions[self.cur + 1] = -num
            self.undos+=1

        self.cur += 1



    def undo(self):
        self.cur -= 1
        self.value = self.values[self.cur]
        self.undos += 1


    def redo(self):
        self.cur += 1
        self.value = self.value + self.transactions[self.cur]
        self.undos -= 1

    def bulk_undo(self, steps: int):
        self.cur -= steps
        if self.cur == -1:
            self.value = 0
        else:
            self.value = self.values[self.cur]
            self.undos += steps

    def bulk_redo(self, steps: int):
        step = min(steps, self.undos)
        for i in range(step):
            self.cur+=1
            self.values[self.cur] = self.values[self.cur-1] + self.transactions[self.cur]
            self.undos -= 1
            print(self.values[self.cur])

        # self.cur -= steps
        self.value = self.values[self.cur]
