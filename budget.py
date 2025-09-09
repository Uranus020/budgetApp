def add_expense(expenses):
    print("새 지출 내역 추가")
    date = input("날짜 (YYYY-MM-DD): ")
    item = input("내역: ")    
    amount = int(input("금액: "))
    type = input("항목: ")
    
    new_expense = {'data' : date, 'item': item, 'amount': amount, 'type': type}
    expenses.append(new_expense)
    print("새 지출이 추가되었습니다.")
    
    
    
    
    
def view_expenses(expenses):
    print("전체 지출 내역")
    if not expenses:
        print("지출 내역이 없습니다")
        return
    else:
        for i in expenses:
            print(f"날짜: {i['date']}, 내역: {i['item']}, 금액: {i['amount']}원, 항목: {i['type']}")
            
            
def delete_expense(expenses):
    print("특정 지출 내역 삭제")
    name = input("삭제할 내역을 입력하시오: ")
    for i in expenses:
        if i['item'] == name:
            expenses.remove(i)
            print(f"'{name}' 항목이 삭제되었습니다\n")
            break
    else:
        print(f"입력한 '{name}'은 존재하지 않습니다")
    
        
        


def exrate(expenses):
        return