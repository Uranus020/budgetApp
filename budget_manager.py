import json

BUDGET_FILENAME = "budget.json"

# 예산 budget.json 호출
def load_budget():
    # 파일이 형성되어 있던 안 되어 있던 우선 open해보고 없을 시 오류를 일으키고 빈 딕셔너리 생성하기
    try:
        with open(BUDGET_FILENAME, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError: 
        return {}
    
# 예산 파일 작성해서 저장
def save_budget(budget_data):
    with open(BUDGET_FILENAME, 'w', encoding='utf-8') as f:
        json.dump(budget_data,f, ensure_ascii=False, indent=4)
        
    
# 월별 예산 설정 기능
def set_budget():
    budget_data = load_budget()
    
    month_input = input("예산을 설정할 월을 입력하세요: ")
    
    try:
        amount_input = int(input(f"{month_input}월의 총 예산을 입력하세요: "))
        budget_data[month_input] = amount_input
        save_budget(budget_data)
        print(f"{month_input}월의 예산이 {amount_input:,}원으로 설정되었습니다.")
    
    except ValueError:
        print("잘못된 형식입니다. 금액은 숫자로만 입력해주세요.")

# 예산과 비교하여 지출 현황 확인 기능
def view_budget_status(expenses):
    budget_data = load_budget()
    
    month_input = input("확인할 월을 입력하세요: ")
    
    if month_input not in budget_data:
        print(f"{month_input}월의 예산이 설정되지 않았습니다. 먼저 예산을 설정해주세요.")
        return
    
    # 해당 월의 예산 설정 정보 불러오기
    monthly_budget = budget_data[month_input]
   
    # 해당 월의 지출액
    monthly_spent = sum(
        k['amount'] for k in expenses if k['date'].startswith(month_input)
    )
    
    remaining = monthly_budget - monthly_spent
    if monthly_budget>0:
        percent_spent = (monthly_spent/monthly_budget) * 100
        
    else:
        percent_spent = 0
        
    # 간단한 진행률 표시줄 만들기
    progress_bar = "#" * int(percent_spent / 10)
    empty_bar = "-" * (10 - len(progress_bar))

    print(f"\n======= {month_input} 예산 대비 지출 현황 =======")
    print(f"설정 예산: {monthly_budget:,}원")
    print(f"현재 지출: {monthly_spent:,}원")
    print(f"남은 예산: {remaining:,}원")
    print("------------------------------------------")
    print(f"예산 사용률: [{progress_bar}{empty_bar}] {percent_spent:.1f}%")
    print("==========================================")
    
    
    