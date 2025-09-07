def add_expense(expenses):
    print("새 지출 내역 추가")
    date = input("날짜 (YYYY-MM-DD): ")
    item = input("항목: ")    
    amount = int(input("금액: "))
    
    new_expense = {'data' : date, 'item': item, 'amount': amount}
    expenses.append(new_expense)
    print("새 지출이 추가되었습니다.")
    
    return expenses
    
    
    
def view_expenses(expenses):
    print("전체 지출 내역")
    if not expenses:
        print("지출 내역이 없습니다")
        return
    else:
        for i in expenses:
            print(f"날짜: {i['date']}, 항목: {i['item']}, 금액: {i['amount']}원")
            
            
def delete_expense(expenses):
    print("특정 지출 내역 삭제")


def statistic_ex(expenses):
        return