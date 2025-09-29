import datetime
from wcwidth import wcswidth

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
    
    """
    view_expenses에서 기존의 코드로 지출 내역 목록을 출력하게 되면
    날짜의 경우 형식이 동일하기 때문에 줄에 맞춰서 잘 나타나나,
    내역부터는 글자 수가 다양해지기 때문에 이에 따라서
    그 이후의 칼럼인 금액과 항목에서 숫자와 글자들이 일렬로 정렬된 형태가 아닌
    제각각으로 나타남 
    => 이는 글자수를 정중앙에 맞추서 정렬하려 했지만, wcwidth함수를 통해서 글자 너비를 고려하여 정렬해야함
    """

def _disp_width(s:str) -> int:
    return wcswidth(str(s) if s is not None else "")

def _pad(s: str,width: int, align="left") -> str:
    s = "" if s is None else str(s)
    w = _disp_width(s)
    pad = max(0, width -w)
    if align == "center":
        left = pad //2
        right = pad - left
        return " " * left + s + " " *right
    
    elif align == "right":
        return " "* pad + s

    else: 
        return s + " " * pad

    
def view_expenses(expenses):
    print("\n" + '-'*23 + "전체 지출 내역" +'-'*23 +"\n")
    if not expenses:
        print("지출 내역이 없습니다")
        return
            
    W_DATE = 12
    W_ITEM = 22
    W_AMOUNT = 14
    W_CAT = 12
    
    header = (
        _pad("날짜", W_DATE, "center") +
        _pad("내역", W_ITEM, "center")+
        _pad("금액", W_AMOUNT, "center")+
        _pad("항목", W_CAT, "center")
    ) 
    print(header)
    print("_"* (W_DATE + W_ITEM + W_AMOUNT + W_CAT))
     
      # else:
    #     print(f"{'날짜':<12} {'내역':^10} {'금액':^20} {'항목':^15}")
    #     print("-" * 63)
    
    
    for exp in expenses:
       date = exp.get('date', '')
       item = exp.get('item', '')  
       category = exp.get('category', '')  
       
       try:
           amt = int(exp.get('amount', 0))
           amount_str = f"{amt:,}원"
       except Exception:
           amount_str = str(exp.get('amount',''))
           
       row = (
         _pad(date, W_DATE, "center")+
         _pad(item, W_ITEM, "center")+
         _pad(amount_str, W_AMOUNT, "right")+
         _pad(category, W_CAT, "center")
       )
       print(row)
    print("_"* (W_DATE + W_ITEM + W_AMOUNT + W_CAT), "\n")
     
    #     for exp in expenses:
    #         print(f"{exp['date']:<12} {exp['item']:^10} {f'{exp['amount']:,}원':^20} {exp['category']:^15}")
    #     print("-"* 63, "\n")  
            
           
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
    
        
