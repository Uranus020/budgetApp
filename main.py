from budget import*
from datamanage import*
from analysis import*
from budget_manager import*

def print_menu():
    print("\n====== My BudgetApp ======")
    print("1. 지출 추가")
    print("2. 지출 내역 보기")
    print("3. 지출 내역 삭제")
    print("-"*15)
    print("4. 지출 내역 검색하기")
    print("5. 월별 리포트 보기")
    print("-"*15)
    print("6. 예산 설정하기")
    print("7. 예산 대비 지출 현황 보기")
    print("-"*15)
    print("8. CSV 파일로 내보내기")
    print("9. 지출 내역 시각화하기")
    print("10. 프로그램 종료")
    print("="*20)
    

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
            search_expenses(expenses)
        elif choice == '5':
            monthly_report(expenses)
        elif choice == '6':
            set_budget()
        elif choice == '7':
            view_budget_status(expenses)
        elif choice == '8':
            save_as_csv(expenses)
        elif choice == '9':
            visualize_expense(CSV_FILENAME)
        elif choice == '10':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 메뉴입니다. 다시 선택하세요. ")
            
if __name__ == "__main__":
    main()