import time
import io
from selenium import webdriver


def load_db():
    with io.open("DataBase.txt", "r",encoding='utf8') as in_file:
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
    with io.open("DataBase.txt", 'w',encoding='utf8') as out_file:
        for index in range(len(data["Questions"])):
            out_file.write(data["Questions"][index])
            out_file.write('\n')
            out_file.write(data["Answers"][index])
            out_file.write('\n')
        out_file.close()


def make_it_easy(path_name):
    data_base = load_db()
    returned = get_from_test(path_name)
    print_to_db(data_base, returned)


make_it_easy('D:/Universitate/Semestrul 2/SO/Preexamen2.html')
make_it_easy('D:/Universitate/Semestrul 2/SO/Preexamen3.html')
make_it_easy('D:/Universitate/Semestrul 2/SO/Preexamen4.html')
make_it_easy('D:/Universitate/Semestrul 2/SO/Preexamen5.html')
make_it_easy('D:/Universitate/Semestrul 2/SO/Preexamen6.html')
make_it_easy('D:/Universitate/Semestrul 2/SO/Preexamen7.html')
make_it_easy('D:/Universitate/Semestrul 2/SO/Preexamen10.html')
make_it_easy('D:/Universitate/Semestrul 2/SO/Preexamen9.html')
make_it_easy('D:/Universitate/Semestrul 2/SO/Preexamen11.html')
make_it_easy('D:/Universitate/Semestrul 2/SO/Preexamen12.html')
make_it_easy('D:/Universitate/Semestrul 2/SO/Preexamen13.html')
make_it_easy('D:/Universitate/Semestrul 2/SO/Preexamen14.html')
make_it_easy('D:/Universitate/Semestrul 2/SO/Preexamen15.html')
make_it_easy('D:/Universitate/Semestrul 2/SO/Preexamen16.html')
make_it_easy('D:/Universitate/Semestrul 2/SO/Preexamen17.html')
make_it_easy('D:/Universitate/Semestrul 2/SO/Preexamen18.html')
make_it_easy('D:/Universitate/Semestrul 2/SO/Preexamen19.html')
make_it_easy('D:/Universitate/Semestrul 2/SO/Preexamen20.html')
make_it_easy('D:/Universitate/Semestrul 2/SO/Preexamen21.html')
make_it_easy('D:/Universitate/Semestrul 2/SO/Preexamen22.html')
make_it_easy('D:/Universitate/Semestrul 2/SO/Preexamen23.html')
make_it_easy('D:/Universitate/Semestrul 2/SO/Preexamen24.html')
make_it_easy('D:/Universitate/Semestrul 2/SO/Preexamen25.html')
make_it_easy('D:/Universitate/Semestrul 2/SO/Preexamen26.html')
make_it_easy('D:/Universitate/Semestrul 2/SO/Preexamen27.html')
make_it_easy('D:/Universitate/Semestrul 2/SO/Preexamen28.html')
make_it_easy('D:/Universitate/Semestrul 2/SO/Preexamen29.html')
make_it_easy('D:/Universitate/Semestrul 2/SO/Preexamen30.html')