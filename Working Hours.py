print("===Υπολογισμός Μισθοδοσίας και Εργατοωρών===")

shifts={}

def add_expense(shift_dict,name,hours,rate):
    if name in shift_dict:
        old_hours = shift_dict[name]["hours"]
        old_rate = shift_dict[name]["hourly_rate"]
        old_total_pay=old_hours*old_rate
        new_pay=hours*rate
        total_hours=old_hours+hours
        shift_dict[name]["hours"]=total_hours
        new_average_pay=(old_total_pay+new_pay)/total_hours
        shift_dict[name]["hourly_rate"]=new_average_pay
        print(f"Προστέθηκαν {hours}  ώρες στο/στη {name}. ")
        print(f"Νέες συνολικές ώρες: {total_hours:.1f} με ωρομίσθιο {new_average_pay:.1f}€/ώρα. ")
    else:
        shift_dict[name]={"hours":hours,"hourly_rate":rate}
        print(f"Καταχωρήθηκε ο/η {name} με {hours:.1f} ώρες και ωρομίσθιο {rate:.1f}€/ώρα. ")

def calculate_payroll(shift_dict):
    total_payroll=0.0
    for name,data in shifts.items():
        hours=data["hours"]
        rate=data["hourly_rate"]
        employee_pay=hours*rate
        total_payroll=employee_pay
        print(f"*{name}:{hours:.1f} ώρες * {rate:.2f}€ = {employee_pay:.2f}€. ")
    return total_payroll

def deduct_hours(shift_dict,name,hours_to_remove):
    if name not in shift_dict:
        print(f"Ο/Η {name} δεν βρέθηκε στις καταχωρήσεις. ")
        return
    current_hours=shift_dict[name]["hours"]
    if hours_to_remove>current_hours:
        print(f"Διορθώστε τη ποσότητα ο εγγεγραμένος έχει καταγγεγραμένες μόνο {current_hours:.1f} ώρες. ")
    else:
        shift_dict[name]["hours"]-=hours_to_remove
        new_hours=shift_dict[name]["hours"]
        print(f"Αφαιρέθηκαν {hours_to_remove:.1f} ώρες από τον/την {name}. ")
        print(f"Νέο υπόλοιπο {current_hours:.1f} ώρες. ")


while True:
    print("")
    print("---ΜΕΝΟΥ ΔΙΑΧΕΙΡΙΣΗΣ---")
    print("1. Καταχώρηση Βάρδιας: ")
    print("2. Αφαίρεση/Αναίρεση Ωρών: ")
    print("3. Προβολή Μισθοδοσίας & Συνολικού Κόστους:")
    print("4. Έξοδος")

    choice=float(input("Διάλεξε (1-4). "))

    if choice == 1:
        name=input("Όνομα Εργαζομένου: ").strip().capitalize()
        if not name:
            print("Το όνομα δε μπορεί να είναι κενό. ")
            continue
        try:
            hours=float(input("Ώρες Εργασίας: "))
            rate=float(input("Ωρομίσθιο: (€/ώρα) "))

            if hours <=0 or rate<=0:
                print("Οι ώρες και το ωρομίσθιο πρέπει να είναι πάνω από 0.")
            else:
                add_expense(shifts,name,hours,rate)
        except ValueError:
            print("Παρακαλώ δώσε έγκυρους αριθμούς για ώρες και ωρομίσθιο.")
    elif choice==2:
        name=input("Όνομα Εργαζομένου: ")
        if name in shifts:
            try:
                hours_to_remove=float(input(f"Πόσες ώρες θέλεις να αφαιρέσεις από τον/την {name}; "))
                if hours_to_remove<=0:
                    print("Παρακαλώ δώσε θετικό αριθμό ωρών. ")
                else:
                    deduct_hours(shifts,name,hours_to_remove)
            except ValueError:
                print("Δώσε έγκυρο αριθμό ωρών. ")
        else:
            print(f"Ο/Η {name} δεν υπάρχει στη λίστα. ")
    
    elif choice==3:
        print("--Ανάλυση Μισθοδοσίας--")
        if len(shifts)<=0:
            print("Δεν υπάρχουν καταγεγραμμένες βάρδιες.")
        else:
            total_cost=calculate_payroll(shifts)
            total_cost=(f"Συνολικό Κόστος Μισθοδοσίας: {total_cost:.2f}€. ")

    elif choice==4:
        print("Αντίο! Καλή συνέχεια στη διαχείριση. ")
        break
    else:
        print("Μη έγκυρη επιλογή δοκίμασε ξανά 1,2 ή 3")