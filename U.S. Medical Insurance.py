#For this project, you will be investigating a medical insurance costs dataset in a .csv file using the Python skills that you have developed. This dataset and its parameters will seem familiar if you have done any of the previous Python projects in the data science path.

#However, you are now tasked with working with the actual information in the dataset and performing your own independent analysis on real-world data! We will not be providing step-by-step instructions on what to do, but we will provide you with a framework to structure your exploration and analysis.

#So, you should to create some tasks for analysis the data.
#I have created some task for me.

#First of all, let's find out how the average age of people, who has 1 child, at least.
#We should import our .csv file and transform it to dictionary.
import csv

people_1more_child_age = []
with open("insurance.csv") as out_file:
    out_file_dict = csv.DictReader(out_file)
    # Let's find out how average age of people, who has 1 child, at least.
    for element in out_file_dict:
        if element["children"] != 0:
            people_1more_child_age.append(int(element["age"]))
average_age = round(sum(people_1more_child_age) / len(people_1more_child_age), 1)
print("The average age of people, who has a 1 child, at least, is equal {age}. This is so bad!".format(age =
                                                                                                      average_age))

# Now we will explore about the difference in charges between people who is smoking and not. (young group,
# middle-age group, and Gendalf one. It would be a preety fuction)
def difference_of_charge(age_group):
    with open("insurance.csv") as out_file:
        out_file_dict = csv.DictReader(out_file)
    # In argument you should write age, and the function will automatically determine the difference in the price of
    # insurance according to the selected age category between smoker and non-smoker people
        list1 = []
        list2 = []
        if 25 > age_group >= 18:
            age_category = "Young"
            x1 = 18
            x2 = 25
        elif 35 > age_group >= 25:
            age_category = "Middle"
            x1 = 25
            x2 = 35
        elif age_group >= 35:
            age_category = "Aged people"
            x1 = 35
            x2 = float("inf")
        else:
            print("None of this category of people exists in our database.")
            return True
        for element in out_file_dict:
            if element["smoker"] == "no":
                if x2 > float(element["age"]) >= x1:
                    list1.append(float(element["charges"]))
     # The same thing we have done for smokers
            else:
                if x2 > float(element["age"]) >= x1:
                    list2.append(float(element["charges"]))
    # What about differences between this group of people?
        difference = ((sum(list1))/len(list1)) - (sum(list2)/len(list1))
        print("The difference in charges between smoker and non-smoker people of category:'{aged}' is {diff}".format(aged =
                                                                                                                age_category, diff = difference))
difference_of_charge(17)



# Let's check about the average charges of old people
def average_smoker():
    list_of_smokers = []
    with open("insurance.csv") as out_file:
        out_file_dict = csv.DictReader(out_file)
        for element in out_file_dict:
            if element["smoker"] == "yes":
                list_of_smokers.append(float(element["charges"]))
        average = round(sum(list_of_smokers) / len(list_of_smokers), 2)
        print("The average charge of smoker people is {average}$.".format(average = average))

average_smoker()


#The next one is about the average percentage of smoker people in main age category.
def diff_smok_age(group_age):
    with open("insurance.csv", "r") as out_file:
        out_file_dict = csv.DictReader(out_file)
        count_of_smoker = 0
        amount_of_dict = 0
        if 25 > group_age >= 18:
            age_category = "Young"
            x1 = 18
            x2 = 25
        elif 35 > group_age >= 25:
            age_category = "Middle"
            x1 = 25
            x2 = 35
        elif group_age >= 35:
            age_category = "Aged people"
            x1 = 35
            x2 = float("inf")
        else:
            print("None of this category of people exists in our database. Try to choose another age.")
            return True
        for element in out_file_dict:
            if x2 > float(element["age"]) >= x1:
                amount_of_dict += 1
                if element["smoker"] == "yes":
                    count_of_smoker += 1
        percentage_of_smoker = round((count_of_smoker / amount_of_dict) * 100, 2)
        print("In {aged} age group there is a {percentage}% smoker people. Ugh!".format(aged = age_category,
                                                                                       percentage = percentage_of_smoker))
diff_smok_age(31)

#Let's explore about the average bmi of woman/man in different group age
def bmi(group_age):
    with open("insurance.csv", "r") as out_file:
        out_file_dict = csv.DictReader(out_file)
        age_man = []
        age_woman = []
        if 25 > group_age >= 18:
            age_category = "Young"
            x1 = 18
            x2 = 25
        elif 35 > group_age >= 25:
            age_category = "Middle"
            x1 = 25
            x2 = 35
        elif group_age >= 35:
            age_category = "Aged people"
            x1 = 35
            x2 = float("inf")
        else:
            print("None of this category of people exists in our database. Try to choose another age.")
            return True

        for element in out_file_dict:
            if x2 > float(element["age"]) >= x1:
                if element["sex"] == "male":
                    age_man.append(float(element["bmi"]))
                else:
                    age_woman.append(float(element["bmi"]))
        difference = round(round(sum(age_man) / len(age_man), 2) - round(sum(age_woman) / len(age_woman), 2),2)

        print("The difference between {group} age gpoup in bmi is approximately equal {dif}.".format(group =
                                                                                                 age_category,
                                                                                              dif = difference))
bmi(21)


# Let's consider where is native state of people
def popular_state(group_of_age):
    with open("insurance.csv", "r") as out_file:
        out_file_dict = csv.DictReader(out_file)
        if 25 > group_of_age >= 18:
            age_category = "Young"
            x1 = 18
            x2 = 25
        elif 35 > group_of_age >= 25:
            age_category = "Middle"
            x1 = 25
            x2 = 35
        elif group_of_age >= 35:
            age_category = "Aged people"
            x1 = 35
            x2 = float("inf")
        else:
            print("None of this category of people exists in our database. Try to choose another age.")
            return True
        currently_state_amount = dict()
        listed_state = []
        for element in out_file_dict:
            if x2 > group_of_age >= x1:
                city = element["region"]
                if not city in listed_state:
                    listed_state.append(city)
                    currently_state_amount[city] = 0
                currently_state_amount[city] += 1
        print(max(currently_state_amount.values()))
        print("The most people from {cat} age category from {reg} region.".format(cat = age_category, reg = max(
            currently_state_amount.keys())))
popular_state(36)


# The last one mission. We have to make class with method
class average_all():
    def __init__(self, age, sex):
        self.age = age
        self.sex = sex
        self.text = open("insurance.csv", "r")
        self.text1 = csv.DictReader(self.text)
    def __repr__(self):
        return ("You have chosen to retrieve some information about {s}, {age} years old.".format(s = self.sex,
                                                                                       age = self.age))
    def group_age(self):
        print(Nastya)
        global x1, x2, age_category
        if 25 > self.age >= 18:
            age_category = "Young"
            x1 = 18
            x2 = 25
        elif 35 > self.age >= 25:
            age_category = "Middle"
            x1 = 25
            x2 = 35
        elif self.age >= 35:
            age_category = "Aged people"
            x1 = 35
            x2 = float("inf")
        else:
            print("None of this category of people exists in our database. Try to choose another age.")
            return True
        average_cost_list = []
        for element in self.text1:
            if element["sex"] == self.sex and x2 > self.age >= x1:
                average_cost_list.append(float(element["charges"]))
        average_price = round(sum(average_cost_list) / len(average_cost_list), 2)
        print("The average cost for this type of person is {cost}$.".format(cost = average_price ))
        self.text.close()

Nastya = average_all(20, "female")
print(Nastya.group_age())

#In tne next project I will improve my sense of syntax sugar, using context manager and something like that.
















