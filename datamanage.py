import json
import csv 


FILENAME = "expense.json"
CSV_FILENAME = "expenses.csv"

def load_expenses():
    "파일에서 지출 내역 데이터를 불러옵니다."
    try:
        with open(FILENAME,'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []    
    

def save_expenses(expenses):
    "지출 내역 데이터를 파일에 저장합니다."
    with open(FILENAME, 'w', encoding='utf-8') as f:
        json.dump(expenses,f,ensure_ascii=False, indent = 4)
        

def save_as_csv(expenses):
    "지출 내역 데이터를 CSV파일로 내보냅니다."
    try:
        with open(CSV_FILENAME,'w', newline='', encoding='utf-8-sig') as f:
             writer = csv.writer(f)
             
             writer.writerow(['날짜', '내역', '금액', '항목'])
             
             for i in expenses:
                 writer.writerow([i['date'], i['item'], i['amount'], i['category']])
        print(f"'{CSV_FILENAME}' 파일로 내보내기 완료")
    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")