import time
from selenium import webdriver


def load_db():
    in_file = open("DataBase.txt", "r")
    lines = in_file.readlines()
    in_file.close()
    db = {"Questions": [],
          "Answers": []}
    cont = 0
    for line in lines:
        if cont % 2 == 0:
            cleaned = line.strip('\n')
            db["Questions"].append(cleaned)
        else:
            cleaned = line.strip('\n')
            db["Answers"].append(cleaned)
        cont += 1
    return db


def get_from_test(path):
    browser = webdriver.Chrome(executable_path=r'D:/Universitate/Semestrul 2/SO/chromedriver.exe')
    browser.get(path)
    questions = browser.find_elements_by_xpath("//div[@class='qtext']")
    answers = browser.find_elements_by_xpath("//div[@class='rightanswer']")
    ret = []
    for index in range(len(questions)):
        que = questions[index].get_attribute('innerHTML')
        ans = answers[index].get_attribute('innerHTML')
        ret.append([que, ans])
    time.sleep(1)
    browser.quit()
    return ret


def print_to_db(data, new_elems):
    contor = 0
    for elem in new_elems:
        if elem[0] not in data["Questions"]:
            contor += 1
            data["Questions"].append(elem[0])
            data["Answers"].append(elem[1])
    print(contor, " intrebari au fost introduse in baza de data")
    out_file = open("DataBase.txt", 'w')
    for index in range(len(data["Questions"])):
        out_file.write(data["Questions"][index])
        out_file.write('\n')
        out_file.write(data["Answers"][index])
        out_file.write('\n')
    out_file.close()


data_base = load_db()
returned = get_from_test('D:/Universitate/Semestrul 2/SO/Preexamen1.html')
print_to_db(data_base, returned)
