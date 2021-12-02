books = ['Coding Fundamentals', 'Jobs in Tech',
         'Java', 'JavaScript', 'Python', 'HTML and CSS']
dictionary = {'Alice': [5, 3, 0, 0, 4, 0], 'Tom': [
    0, 2, 4, 0, 0, 4], 'Jon': [0, 4, 1, 0, 0, 1], 'Josh': [0, 1, 5, 3, 0, 1]}

display = {}

for i in range(len(books)):
    el = books[i]
    count = 0
    summ = 0
    for x, y in dictionary.items():
        summ += y[i]
        if(y[i] > 0):
            count += 1
    if(count == 0):
        avg = 0
    else:
        avg = summ/count
    display[format(avg, '.2f')] = el
display = dict(sorted(display.items(), reverse=True))


def main_menu():
    print("Welcome to the EduWra Book Recommendation System")
    print("1: All books average ratings")
    print("2: Recommend books for a particular user")
    print("q: Exit the page")


def display_r(display):
    for x, y in display.items():
        print("The average ratings for", y, "is", x)
    print()


def calc_similarity(user1, user2):
    product = 0
    sum = 0
    for i in range(len(dictionary[user1])):
        product = (dictionary[user1][i]) * (dictionary[user2][i])
        sum = sum + product
    return sum


def recommend_books(user):
    mylist = []
    for x, y in dictionary.items():
        if(x != user):
            mylist.append([calc_similarity(user, x), x])

    mylist.sort(key=lambda x: x[0], reverse=True)

    # only top 3 items
    dic = {}

    for i in range(len(books)):
        el = books[i]
        count = 0
        summ = 0
        for j in range(3):
            name = mylist[j][1]
            ls = dictionary[name]
            summ += ls[i]
            if(ls[i] > 0):
                count += 1
        if(count == 0):
            avg = 0
        else:
            avg = summ/count
        dic[format(avg, '.2f')] = el
    dic = dict(sorted(dic.items(), reverse=True))
    display_r(dic)


while True:
    main_menu()
    choice = input("Select one of the options above: \n")

    if choice == "1":
        display_r(display)
    elif choice == "2":
        name = input("Please enter the customer's name: ")
        if name not in dictionary:
            display_r(display)
        else:
            recommend_books(name)

    elif choice == "q":
        print("Have a nice day!")
        break
    else:
        print("Invalid input")
