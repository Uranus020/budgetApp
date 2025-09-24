import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import datetime

# 폰트가 깨져서 나타나기 때문에 폰트 설정도 미리 해줘야함
try:
    plt.rcParams['font.family'] = 'AppleGothic'
except:
    plt.rcParams['font.family'] = 'Malgun Gothic'

# 지출 내역 검색 기능
# 특정 키워드를 통해서 분류할 수 있게 만들어주기
# 해당 항목을 입력하거나, 분류 기준을 넣으면 그것들만 담은 리스트를 만들어서 뽑아낼 수 있게 해주기
def search_expenses(expenses):
    if not expenses:
        print("검색할 지출 내역이 없습니다.")
        return
    
    keyword = input("검색할 내역 또는 항목을 입력하세요: ")
    # 새 리스트에 해당 키워드만 뽑아서 내역을 추가해주기
    results = [
        exp for exp in expenses
        if keyword in k['item'] or keyword in k['category']
    ]
    
    if not results:
        print(f"'{keyword}'에 해당하는 지출 내역을 찾을 수 없습니다.")
    else:
        print(f"\n ----- '{keyword} 검색 결과 -----")
        from budget import view_expenses
        view_expenses(results)


# 월별 리포트 기능 
def monthly_report(expenses, budget_data):
    
    # 1. 사용자 입력으로 리프토를 확인할 월 지정
    while True:
        month_input = input("리포트를 확인할 월을 입력하시오 (YYYY-MM): ")
        try:
            datetime.datetime.strptime(month_input, '%Y-%m')
            break
        except ValueError:
            print("잘못된 날짜 형식입니다. YYYY-MM 형식으로 다시 입력해주세요.")
            
    # 2. 해당 입력 월의 지출 내역 
    monthly_expenses = [
        exp for exp in expenses
        if exp['date'].startswith(month_input)
    ]
    
    if not monthly_expenses:
        print(f"{month_input}월의 지출 내역이 없습니다.")
        return

    # 3. 총 지출액 계산
    total_spent = sum(exp['amount'] for exp in monthly_expenses)
    
    # 4. 카테고리별 지출 분석
    category_spending = {}
    for exp in monthly_expenses:
        # category = exp['category'] 
        # 만약 지출 중 하나라도 'category' 키가 없으면 프로그램 멈출 수도 있음
        category = exp.get('category', '미분류')
    
        amount = exp['amount']
        # if category not in category_spending:
        #     category_spending[category] = 0
        # category_spending[category] += amount
        # 간략하게 한 줄로 바꾸기
        category_spending[category] = category_spending.get(category, 0) + amount
    
    # 5. 예산 정보 가져오고 업데이트하기
    monthly_budget  = budget_data.get(month_input, 0) # 만약에 예산이 없다면 0으로 처리하기
    remaining_budget = monthly_budget - total_spent if monthly_budget > 0 else "N/A" 
    
    
    # 6. 리포트 출력
    print(f"\n====== {month_input} 월별 리포트 ======")
    print(f"총 지출: {total_spent: ,}원")
    if monthly_budget > 0:
        print(f"설정 예산: {monthly_budget: ,}원 (남은 예산: {remaining_budget: ,}원)")
    
    else:
        print("해당 월의 예산이 설정되지 않았습니다.")
    print("\n--- 카테고리별 지출 상세 ---")
    
    # 지출액이 큰 순서대로 정렬해서 보이기
    sorted_categories = sorted(category_spending.items(), key = lambda item: item[1], reverse=True)
    
    for category, amount in sorted_categories:
        percentage = (amount / total_spent) *100 if total_spent>0 else 0
        print(f"- {category: <10}: {amount>10,}원 ({percentage:.1f}%)")
    print("=" *40)




# 지출 내역 시각화 기능
def visualize_expense(filename):
    """
    CSV 파일을 읽어서 사용자 선택에 따라 여러 데이터 시각화를 제공
    1. 막대 그래프 (항목별 지출)
    2. 원그래프 (항목별 지출 비율)
    3. 선그래프 (일자별 지출 추이)
    """
    
    try:
        df = pd.read_csv(filename, encoding="utf-8-sig")
        df["금액"] = pd.to_numeric(df["금액"], errors="coerce")
        df.dropna(subset=['금액'], inplace=True)
        # 날짜 데이터를 시계열 데이터로 변환 
        df['날짜'] = pd.to_datetime(df['날짜'],errors ='coerce')
        df.dropna(subset=['날짜'],inplace=True)
        
        print("\n===지출 내역 시각화===")
        print("1. 항목별 지출 (막대그래프)")
        
        print("2. 항목별 지출 (원그래프)")
        
        print("3. 항목별 지출 (선그래프)")
        choice = 
       
       
       
       
        
    except FileNotFoundError:
        print(f"'{filename}' 파일을 찾을 수 없습니다. 메뉴 4번으로 CSV 파일을 먼저 내보내주세요.")    
    except Exception as e:
        print(f"시각화 중 오류 발생: , {e}")