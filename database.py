def add_patient(patient_name, patient_id, age):
    list_patient = [patient_name, patient_id, age, []]#[] put a blank list in behind
    return list_patient

def main():
    db = []
    x = add_patient("Anna Ables", 342, 40)
    db.append(x)
    y = add_patient("Bob", 50, 50)
    db.append(y)
    z = add_patient("CC", 111, 35)
    db.append(z)
    db.append(add_patient("DD", 22,122))
    founpatient = find_patient(db, [1])
    print(founpatient)
    print(db)


    
def find_patient(db, id_no):
    for patient in find_patient:
        if patient[1] == id_no:
            return patient
    return

def add_test_to_patient(db, id_no, test_name, test_result):
    for patient in db:
        if patient[1] == id_no:
            return patient
    return



#   print(x)
#    print(y)
#    print(z)
#    print(db)
#    print(db[1][2])#second item in the list third item in the second item
#    print(db[-1])#last item in the list
#    print(db[0:3])#print item from 0 item to 2 = db[:3]

def print_directory(db):
    rooms = ["Room 13", "Room 12", "Room 99", "Room 3"]
    for i, patient in enumerate(db):
        print("{} {}".format(1, patient[0]))
    
    
    
    for i in range(len(db)):
        print("Room: {} Room {}".format(db[1][0],rooms[1]))
        



    for patient in db:
        print("Room: {}".format(patient[0]))



if __name__ == "__main__":
    main()
