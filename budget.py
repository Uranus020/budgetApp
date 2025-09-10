import datetime

def add_expense(expenses):
    print("새 지출 내역 추가")
    
    while True:
        date = input("날짜 (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
            break
        except ValueError:
            print("잘못된 날짜 형식입니다. YYYY-MM-DD형식으로 다시 입력하시오.")
            
    item = input("내역: ")    
    
    while True:
        try:
            amount = int(input("금액: "))
            break
        except ValueError:
            print("잘못된 금액 형식입니다. 숫자로 다시 입력하시오.")
    
    category = input("항목: ")
    

    new_expense = {'date' : date, 'item': item, 'amount': amount, 'category': category}
    expenses.append(new_expense)
    print("새 지출이 추가되었습니다.")
    
    
    
    
    
def view_expenses(expenses):
    print("\n--- 전체 지출 내역 ---\n")
    if not expenses:
        print("지출 내역이 없습니다")
        return
    else:
        print(f"{'날짜':<12} {'내역':^10} {'금액':^20} {'항목':^15}")
        print("-" * 63)
        
        for i in expenses:
            print(f"{i['date']:<12}   {i['item']:^10} {f'{i['amount']:,}원':^20}  {i['category']:^15}")
        print("-"* 63, "\n")  
            
def delete_expense(expenses):
    print("특정 지출 내역 삭제")
    name = input("삭제할 내역을 입력하시오: ")
    
    delete_item = None
    
    for i in expenses:
        if i['item'] == name:
            delete_item = i
            break
    
    if delete_item:
        expenses.remove(delete_item)
        print(f"'{name}' 내역이 삭제되었습니다\n")
    else:
        print(f"입력한 '{name}'은 존재하지 않습니다")
    
        
        


def exrate(expenses):
        return