from budget import*
from datamanage import*

def print_menu():
    print("My BudgetApp")
    print("1. 지출 추가")
    print("2. 지출 내역 보기")
    print("3. 지출 내역 삭제")
    print("4. 지출 내역 csv파일로 내보내기")
    print("5. 환율 계산")
    print("6. 프로그램 종료")
    

def main():
    expenses = load_expenses()
    while True:
        print_menu()
        choice = input("메뉴를 선택하시오: \n")
        
        if choice == '1':
            add_expense(expenses)
            save_expenses(expenses)    
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            delete_expense(expenses)
            save_expenses(expenses)
        elif choice == '4':
            save_as_csv(expenses)
        elif choice == '5':
            exrate(expenses)
        elif choice == '6':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 메뉴입니다. 다시 선택하세요. ")
            
if __name__ == "__main__":
    main()