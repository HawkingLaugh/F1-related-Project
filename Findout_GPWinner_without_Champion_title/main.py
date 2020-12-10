import requests
from bs4 import BeautifulSoup

#Get all F1 drivers that had win GP
def get_win():
    res = requests.get('https://en.wikipedia.org/wiki/List_of_Formula_One_Grand_Prix_winners#By_driver')
    soup = BeautifulSoup(res.content, 'lxml')
    win_table = soup.find_all('table')[2]
    names = win_table.find_all(class_="fn")
    winners = []
    for name in names:
        winners.append(name.text)
    return winners

#Get all F1 drivers that had win World Champion title
def get_cham():
    res = requests.get('https://en.wikipedia.org/wiki/List_of_Formula_One_World_Drivers%27_Champions#By_driver')
    soup = BeautifulSoup(res.content, 'lxml')
    cham_table = soup.find_all('table')[2]
    names = cham_table.find_all("a")
    champions = []
    for name in names:
        if name.text.isnumeric() or name.text == '[7]':
            continue
        else:
            champions.append(name.text)
    return champions

#Find out the different both list and print out all F1 GP winners without Champion title
def main(list1, list2):
    different_between_two = set(list1) ^ set(list2)
    print(different_between_two)

if __name__ == "__main__":
    main(get_win(), get_cham())