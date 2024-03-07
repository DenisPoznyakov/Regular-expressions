import re
from pprint import pprint
import csv

def normalised_contacts(file_name):

    with open(file_name, encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    for x in contacts_list:
        fio = " ".join(x[:3])
        i = fio.split(" ")
        x[0] = i[0]
        x[1] = i[1]
        x[2] = i[2]

    for contact in contacts_list:
        last_name = contact[0]
        first_name = contact[1]
        for new_contact in contacts_list:
            new_last_name = new_contact[0]
            new_first_name = new_contact[1]
            if first_name == new_first_name and last_name == new_last_name:
                if contact[2] == "": contact[2] = new_contact[2]
                if contact[3] == "": contact[3] = new_contact[3]
                if contact[4] == "": contact[4] = new_contact[4]
                if contact[5] == "": contact[5] = new_contact[5]
                if contact[6] == "": contact[6] = new_contact[6]
            new_contacts_list = list()
            for i in contacts_list:
                if i not in new_contacts_list:
                    new_contacts_list.append(i)

    for x in new_contacts_list:
        pattern = r"(\+7|8)[\s(]*(\d{3})[)\s*-]*(\d{3})*[\s*-]*(\d{2})[\s*-]*(\d{2})\s*[(доб.\s]*(\d+)*"
        substitute = r"+7(\2)\3-\4-\5 доб.\6."
        result = re.sub(pattern, substitute, str(x[5]))
        x[5] = result

    for i in new_contacts_list:
        if len(i[5]) == 26:
            i[5] = i[5]
        else:
            j = i[5].split(" ")
            i[5] = j[0]

    with open("phonebook.csv", "w", newline='', encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_contacts_list)

if __name__ == '__main__':
    file_name = "phonebook_raw.csv"
    normalised_contacts(file_name)