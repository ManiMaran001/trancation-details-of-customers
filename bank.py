import pickle
import datetime
import time


# bannering for the projects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'
BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def color_text(text: str, *effects: str) -> str:
    effected_string = "".join(effects)
    output = "{} {} {}".format(effected_string, text, RESET)
    return output


def banner_area(text: str = '') -> None:
    screen_width = 100
    if len(text) >= screen_width - 4:
        raise ValueError("{} size is overlapping the screen sizes {} ".format(text, screen_width - 4))

    if text == "*":
        print("*" * screen_width)
    else :
        words = color_text(text, BOLD, GREEN)
        centered_text = words.center(screen_width + 9)
        output = "**{}**".format(centered_text)
        print(output)


def menu():
    banner_area("*")
    banner_area("1.insert a  record")
    banner_area("2.display all records")
    banner_area("3.update a records")
    banner_area("4.delete a records")
    banner_area("5.debit from account")
    banner_area("6.credit from account")
    banner_area("8.debit and credit reports menus")
    banner_area("9.search account vise debit details")
    banner_area("10.search account vise credits detaisl")
    banner_area("11.search account no vise account details")
    banner_area("10.Exit")
    banner_area("*")


def show_banner() :
    banner_area("*")
    banner_area("harsh bank management systems")
    banner_area("*")


def get_valid_name(prompt) :
    while True :
        temp = input(prompt)
        # len(temp) >= 4 and len(temp) <= 15:
        if 4 <= len(temp) <= 15 and temp.isalpha() :
            return temp
        else :
            print("length between 2 t0 10 characters")


def get_valid_mobile(prompt) :
    while True :
        temp = input(prompt)
        if len(temp) != 10 or (not (temp.startswith(('9', '8')))) or not (temp.isdigit() == True) :
            print("number between 1 to 10 must be digits")
        else :
            return temp


def get_valid_mail(prompt) :
    while True :
        temp = input(prompt)
        example = "gm123@gmail.com"
        if '@' not in list(temp) or '.' not in list(temp) :
            print("please enter the two symbols strictly {}".format(example))
        else :
            return temp


def insert(f) :
    fil = open(f, 'ab+')
    if fil.tell() > 0 :
        fil.seek(0)
        rec = pickle.load(fil)
    else :
        rec = []
    while True :
        account_no = int(input("enter the account number "))
        name = get_valid_name("enter the name:")
        mobile_no = get_valid_mobile("enter the mobile no:")
        address = get_valid_name("enter the address:")
        city = get_valid_name("enter the city:")
        email_id = get_valid_mail("enter the mail id")
        amounts = float(input("enter the amounts"))
        r = [account_no, name, mobile_no, address, city, email_id, amounts]
        rec.append(r)
        ch = input("do you want to more records y/n")
        if ch == 'N' or ch == 'n' :
            break
    with open(f, 'wb') as fil :
        fil.seek(0)
        print(fil.tell())
        pickle.dump(rec, fil)


def display(f) :
    fil = open(f, 'rb')
    rec = pickle.load(fil)
    print(color_text("account_no\t\tname\t\tmobile_no\t\taddress\t\tcity\t\temail_id\t\tamounts", BLUE, BOLD))
    try :
        for i in rec :
            for j in i :
                print(color_text(j, MAGENTA, BOLD), end='\t')
            print()

    except EOFError :
        fil.close()


def update(f) :
    """
    function going to update
    :param f: coming from the calling side file name
    :return: none
    """
    try :
        with open(f, 'rb+') as fil :
            found = 0
            a = int(input("enter the acc no to update:"))
            rec = pickle.load(fil)
            c = len(rec)
            while True and found == 0 :
                for i in range(0, len(rec)) :
                    if rec[i][0] == a :
                        found += 1
                        ch = input("do you want to update account_no(y/n)")
                        if ch == 'Y' or ch == 'y' :
                            rec[i][0] = int(input("enter the new account_no"))
                        ch = input("do you want to update name(y/n)")
                        if ch == 'Y' or ch == 'y' :
                            rec[i][1] = get_valid_name("enter the new name")
                        ch = input("do you want to update mobile(y/n)")
                        if ch == 'Y' or ch == 'y' :
                            rec[i][2] = get_valid_mobile("enter the new mobile_no")
                        ch = input("do you want to update address(y/n)")
                        if ch == 'Y' or ch == 'y' :
                            rec[i][3] = get_valid_name("enter the new address")
                        ch = input("do you want to update city(y/n)")
                        if ch == 'y' or ch == 'Y' :
                            rec[i][4] = get_valid_name("enter the city:")
                        ch = input("do you want to update email(y/n)")
                        if ch == 'Y' or ch == 'y' :
                            rec[i][5] = get_valid_name("enter the email_id")
                print("record read in file", c)
                if found == 0 :
                    print("record not found")
                    break
            fil.seek(0)
            pickle.dump(rec, fil)
    except FileNotFoundError :
        print(fil, 'doesnt exist')


def sort_acc_no(f) :
    with open(f, 'rb+')as fil :
        rec = pickle.load(fil)

        pickle.dump(rec, fil)


def delete(f) :
    with open(f, 'rb+') as fil :
        found = 0
        k = []
        a = int(input(color_text("enter the acc:", RED, BOLD)))
        rec = pickle.load(fil)
        while True :
            for i in range(0, len(rec)) :
                if rec[i][0] == a :
                    found += 1
                else :
                    k.append(rec[i])

            if found == 0 :
                print("that record is not found")
                break
            else :
                print(color_text("record is deleted account no",BLUE, BOLD))
                menu()
                fil.seek(0)
                pickle.dump(k, fil)
                break


def check_acc_no(acc) :
    f = 'bank'
    with open(f, 'rb') as fil :
        status = 0
        rec = pickle.load(fil)
        for ins in range(0, len(rec)) :
            for i in rec :
                if i[0] == acc :
                    status += 1
                    return status
            if status == 0 :
                return status


def debit(f) :
    with open(f, 'rb+') as fil :
        found = 0
        rec = pickle.load(fil)
        a = int(input(color_text("enter the account no:", GREEN, BOLD)))
        acc_found = check_acc_no(a)
        if acc_found == 1 :
            print(color_text("account founded", MAGENTA, BOLD))
            amt = float(input(color_text("enter the amount withdraw from account no {}".format(a), CYAN, BOLD)))
            for i in range(0, len(rec)) :
                if a == rec[i][0] :
                    if rec[i][6] - amt >= 3000 :
                        rec[i][6] -= amt
                        ch='D'
                        found += 1
                        dat = datetime.datetime.now()
                        dates = dat.date()
                        tim = time.strftime("%X", time.localtime())
                        r = [a, rec[i][1], amt, dates, tim,ch]
                        debit_summary(r)
                        break
                    else :
                        print("amount must be greater than the 3000")
                        found = 0
                        ch = input("if you want to check balance:y/n")
                        if ch == 'Y' or ch == 'y' :
                            print("acc_no: {} for balance is {} "
                                  .format(color_text(str(a), CYAN), color_text(str(rec[i][6]), CYAN)))
                        break
            if found == 0 :
                print(color_text("amount not debited", RED, BOLD))
            else :
                print(color_text("amount  debited", RED, BOLD))
            fil.seek(0)
            pickle.dump(rec, fil)
        else :
            print("account no not found")
            menu()


def credit(f) :
    with open(f, 'rb+') as fil :
        found = 0
        a = int(input(color_text("enter the account_no:", BLUE, BOLD)))
        rec = pickle.load(fil)
        acc_found = check_acc_no(a)
        if acc_found == 1 :
            print("account founded")
            amt = float(input(color_text("enter the amount you want to credit in account no {}".format(a),BLUE,BOLD)))

            for i in range(0, len(rec)) :
                if rec[i][0] == a :
                    if amt <= 50000 :
                        rec[i][6] += amt
                        found += 1
                        ch='C'
                        dat = datetime.datetime.now()
                        dates = dat.date()
                        tim=time.strftime("%X",time.localtime())
                        r = [a,rec[i][1], amt, dates,tim,ch]
                        credit_summary(r)
                        break
                    else :
                        print(color_text("you only debit within 50000", RED, BOLD))
                        found = 0
                        break
            if found == 0 :
                print(color_text("amount not credited",RED,BOLD))
            else :
                print(color_text("amount credited",MAGENTA,BOLD))
            fil.seek(0)
            pickle.dump(rec, fil)

        else :
            print(color_text("account not found",YELLOW,BOLD))
            menu()


def credit_summary(r) :
    file = 'summary'
    f = open(file, 'ab+')
    if f.tell() > 0 :
        f.seek(0)
        rec1 = pickle.load(f)
    else :
        rec1 = []
    with open(file, 'wb') as fi :
        # r = [a, amt, dat]
        rec1.append(r)
        f.seek(0)
        pickle.dump(rec1, fi)


def debit_summary(r):

    file='summary'
    f=open(file,'ab+')
    if f.tell()>0:
        f.seek(0)
        rec=pickle.load(f)
    else:
        rec=[]
    with open(file,'wb') as fil:
        rec.append(r)
        fil.seek(0)
        pickle.dump(rec,fil)


def show_all_summary() :

    with open('summary', 'rb') as fil :
        rec = pickle.load(fil)
        print(color_text("account_no\t\tname\t\tamount\t\t\tdate\t\t\ttime",YELLOW,BOLD))
        for i in rec :
            for j in i :
                print(color_text(j,BLUE,BOLD), end='\t\t\t')
            print()


def show_acc_no_vise_report_credits():
    """
    showing account no vise reporting credit details
    :return: none
    """
    print(show_acc_no_vise_report_credits.__doc__)
    file='summary'
    with open(file,'rb') as fil:
        found=0
        print(color_text("credit vise reports",GREEN,BOLD,REVERSE))
        a=int(input(color_text("enter the account no :",RED,BOLD)))
        rec=pickle.load(fil)
        print(color_text("account_no\t\tname\t\tamount\t\t\tdate\t\t\ttime\t\t\tcredits",MAGENTA,BOLD))
        for i in range(0,len(rec)):
            if rec[i][0]==a and rec[i][5]=='C':
                found+=1
                for ins in rec[i]:
                    print(color_text(ins,RED,BOLD),end='\t\t\t')
                print()


        if found==0:
            print(color_text("record not found",RED,BOLD,REVERSE))
            menu()
        else:
            print(color_text("record found",YELLOW,BOLD))


def show_acc_no_vise_report_debits():
     file = 'summary'
     with open(file, 'rb') as fil :
         found = 0
         print(color_text("DEBIT vise reports", GREEN, BOLD, REVERSE))
         a = int(input("enter the account no :"))
         rec = pickle.load(fil)
         print("account_no\t\tname\t\tamount\t\t\tdate\t\t\ttime\t\t\t\tdebits")
         for i in range(0, len(rec)) :
             if rec[i][0] == a and rec[i][5] == 'D' :
                 found += 1
                 for ins in rec[i] :
                     print(ins, end='\t\t\t')
                 print()

         if found == 0 :
             print("record not found")
             menu()
         else :
             print("record found")


def search_acc_no_vice_extract(f):
    with open(f,'rb') as fil:
        rec=pickle.load(fil)
        found=0
        a=int(input("search vise acc_no"))
        for i in range(0,len(rec)):
            if rec[i][0]==a:
                found+=1
                for ins in rec[i]:
                    print(ins,end='\t')
                print()

        if found==0:
            print("record not found")
        else:
            print("record found")

        





def summary() :
    file = 'summary'
    r = []
    banner_area("1.show credits summary report")
    banner_area("2.show_debits summary report")
    banner_area("5.outcome of the report")
    while True :
        choice = input("enter the choice:")
        if choice == '1' :
            show_all_summary()
        elif choice == '5' :
            print("outcomed from the report area")
            menu()
            break



# main program starting

show_banner()
menu()
file = 'bank'

while True :
    choice = input(color_text("enter the choice in the menu", YELLOW, BOLD))
    if choice == '1' :
        insert(file)
    elif choice == '2' :
        display(file)
    elif choice == '3' :
        update(file)
    elif choice == '4' :
        delete(file)
    elif choice == '5' :
        debit(file)
    elif choice == '6' :
        credit(file)
    elif choice == '8' :
        summary()
    elif choice=='9':
        show_acc_no_vise_report_credits()
    elif choice=='10':
        show_acc_no_vise_report_debits()
    elif choice=='11':
        search_acc_no_vice_extract(file)
    elif choice == '0' :
        break
    else :
        print(color_text("nothing selected", RED, REVERSE))

