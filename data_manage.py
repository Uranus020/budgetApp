import json
import csv 
import pandas as pd

FILENAME = "expense.json"
CSV_FILENAME = "expenses.csv"

def load_expenses(filename="지출내역서.xlsx"):
    """
    직접 만든 지출내역서 파일에서 지출 내역 데이터를 불러옵니다.
    """
    try:
        # 엑셀 파일 읽기
        df = pd.read_excel(filename)
        
        # 엑셀 파일 속의 항목명들을 프로그램에서 각 label들과 맞춰서 연결시켜주기
        df.rename(columns={
            '날짜' : 'date', '내역' : 'item', '금액': 'amount', '항목' : 'category'
        }, inplace=True)
        
        # 날짜 형식도 맞춰주기
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
        
        # 딕셔너리 리스트 형태로 변환시키기
        return df.to_dict('records')
    
    # 예외 함수 처리 중 파일이 없는 경우
    except FileNotFoundError:
        print(f"'{filename}'파일을 찾을 수 없습니다.")
        print("프로젝트 폴더에 엑셀 파일이 있는지 확인해주세요.")
        return []
    
    # 예외 함수 처리 중 파일은 있으나 다른 오류가 발생한 경우
    except Exception as e:
        print(f"엑셀 파일을 읽는 중 문제가 발생했습니다.: {e}")
        return []
    # 엑셀 파일을 직접 만들어서 넣기 전에 구현했던 load 함수는 파일을 일근 것만 구현했었음    
    # try:
    #     with open(FILENAME,'r', encoding='utf-8') as f:
    #         return json.load(f)
    # except FileNotFoundError:
    #     return []    
    

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
        
        
