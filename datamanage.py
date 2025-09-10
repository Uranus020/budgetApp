import json

FILENAME = "expense.json"

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