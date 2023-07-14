import random


class Perceptron:

    def __init__(self, number_of_inputs, weights = 0, learnig_rate = 0.001, repetitions = 10000):
        self.number_of_inputs = number_of_inputs
        if weights == 0:
            self.weights = [random.uniform(0, 1) for _ in range(number_of_inputs + 1)]
        self.learnig_rate = learnig_rate
        self.repetitions = repetitions

    def update(self, inputs, expected):
        for _ in range(self.repetitions):
            przewidywany = sum(weight * input for weight, input in zip(self.weights, inputs)) + self.weights[-1]
            blad = expected - przewidywany
            self.weights = [weight + input * blad * self.learnig_rate for weight, input in zip(self.weights, inputs)] + [self.weights[-1] + 1 * blad * self.learnig_rate]
        return self.weights

    def predict(self, inputs, weights = 0.0):
        if weights != 0:
            self.weights = weights
        #for krok in range(self.ilosc, len(x)):
        przewidywany = sum(weight * input for weight, input in zip(self.weights, inputs)) + self.weights[-1]
        expected = przewidywany
        return expected


class inputs:
    def __init__(self): #only inputs type float
        self.inputs = []
    def get (self, name_of_file = "", number_of_inputs = 0):
        self.name_of_file = name_of_file
        self.number_of_inputs = number_of_inputs
        if name_of_file == "":
            for _ in range(number_of_inputs):
                new = float(input())
                self.inputs.append(new)
        else:
            file = open(self.name_of_file, "r")
            for line in file.readlines():
                stripped_line = line.strip()
                new = float(stripped_line)
                self.inputs.append(new)
                self.number_of_inputs = self.number_of_inputs + 1
        return (self.inputs,self.number_of_inputs)


class teach:
    def __init__(self):
        inputs_obj = inputs()
        list = inputs_obj.get("list.txt")
        self.list = list[0]
        self.number_of_inputs = list[1]

    def currency_rates(self, ilosc, weights = 0.0):
        perceptron_update = []
        perceptron_test = []
        for step in range(ilosc, self.number_of_inputs // 100 * 70):
            inputs = self.list[step - ilosc:step]
            expected = self.list[step + 1]
            perceptron_obj = Perceptron(len(self.list))
            perceptron_update = perceptron_obj.update(inputs, expected)
            print(perceptron_update)
        for step2 in range (self.number_of_inputs // 100 * 70, self.number_of_inputs - 1):
            inputs = self.list[step2 - ilosc:step2]
            expected = self.list[step2 + 1]
            perceptron_test_obj = Perceptron(len(self.list))
            perceptron_test = perceptron_test_obj.predict(inputs,weights)
            print(perceptron_test,expected)


        return (perceptron_update,perceptron_test)

class test:
    def __init__(self, name_of_file="", number_of_inputs=0):
        inputs_obj = inputs()
        input_results = inputs_obj.get(name_of_file, number_of_inputs)
        self.list = input_results[0]
        self.number_of_inputs = input_results[1]

    def currency_rates_last_4(self, ilosc = 4, weights = [-0.0884719802010076, 0.0064667238037149, 0.141655412000415, 0.5222355651068462, 0.4514820220245377]):
        results = []
        for step2 in range(ilosc, self.number_of_inputs - 1):
            inputs = self.list[step2 - ilosc:step2]
            expected = self.list[step2 + 1]
            perceptron_test_obj = Perceptron(4)
            perceptron_test = perceptron_test_obj.predict(inputs, weights)
            results.append((perceptron_test, expected))
            eur = 100
            usd = 100
            if self.list[step2] < perceptron_test:
                eur = eur + usd / self.list[step2]
                usd = 0
            elif self.list[step2] > perceptron_test:
                usd = usd + eur * self.list[step2]
                eur = 0
            print(perceptron_test, expected)

        return "całość na początku w euro", 100 + 100 / self.list[0], "całość na początku w dolarach", 100 + 100 * self.list[0],"ilosc euro na konciu", eur,"ilosc doalrow na koniec", usd



"""teach_obj = teach()
teaching = teach_obj.currency_rates(4,[-0.0884719802010076, 0.0064667238037149, 0.141655412000415, 0.5222355651068462, 0.4514820220245377])
print(teaching)"""
test_roberta_obj = test("", 100)
test_roberta = test_roberta_obj.currency_rates_last_4(ilosc = 4, weights = [-0.0884719802010076, 0.0064667238037149, 0.141655412000415, 0.5222355651068462, 0.4514820220245377])
print(test_roberta)










