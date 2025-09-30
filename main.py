from budget import add_expense, view_expenses, delete_expense
from data_manage import load_expenses, save_as_csv, save_expenses
from analysis import visualize_expense, search_expenses, monthly_report
from budget_manager import set_budget, load_budget, view_budget_status

def print_menu():
    print("\n====== My BudgetApp ======")
    print("1. 지출 추가")
    print("2. 지출 내역 보기")
    print("3. 지출 내역 삭제")
    print("-"*26)
    print("4. 지출 내역 검색하기")
    print("5. 월별 리포트 보기")
    print("-"*26)
    print("6. 예산 설정하기")
    print("7. 예산 대비 지출 현황 보기")
    print("-"*26)
    print("8. CSV 파일로 내보내기")
    print("9. 지출 내역 시각화하기")
    print("10. 프로그램 종료")
    print("="*26)
    

def main():

    # 엑셀 파일을 직접 만들엇기 때문에 단순히 부르는 것이 아닌, 파일 이름을 지정해서 불러줘야함
    DATA_Ex = "지출내역서.xlsx"
    
    expenses = load_expenses(DATA_Ex)
    
    if not expenses:
        expenses = load_expenses(DATA_Ex) or []
    
    #원래 5번 항목에 들어가 있던 것을 매번 load하는 것이 아닌, 한 번만 load시키고 메뉴 고르도록 하기
    budget_data = load_budget()
    
    while True:
        print_menu()
        choice = input("메뉴를 선택하시오: \n")
        
        if choice == '1':
            add_expense(expenses)
            save_expenses(expenses)    
        elif choice == '2':
            expenses = load_expenses(DATA_Ex)
            view_expenses(expenses)
        elif choice == '3':
            delete_expense(expenses)
            save_expenses(expenses)
        elif choice == '4':
            search_expenses(expenses)
        elif choice == '5':
            monthly_report(expenses, budget_data)
        elif choice == '6':
            set_budget()
            budget_data = load_budget()
        elif choice == '7':
            view_budget_status(expenses)
        elif choice == '8':
            save_as_csv(expenses)
        elif choice == '9':
            visualize_expense("expenses.csv")
        elif choice == '10':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 메뉴입니다. 다시 선택하세요. ")
            
if __name__ == "__main__":
    main()