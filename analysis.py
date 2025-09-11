import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

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
        k for k in expenses
        if keyword in k['item'] or keyword in k['category']
    ]
    
    if not results:
        print(f"'{keyword}'에 해당하는 지출 내역을 찾을 수 없습니다.")
    else:
        print(f"\n ----- '{keyword} 검색 결과 -----")
        from budget import view_expenses
        view_expenses(results)


# 월별 리포트 기능 
def monthly_report(expenses):
    return




# 지출 내역 시각화 기능
def visualize_expense(filename):
    try:
        df = pd.read_csv(filename, encoding="utf-8-sig")
        df["금액"] = pd.to_numeric(df["금액"], errors="coerce")
        
        df.groupby("항목")["금액"].sum().plot(kind="bar", title="항목별 지출")
        plt.xlabel("항목")
        plt.ylabel("금액")
        plt.tight_layout()
        plt.show()
        
    except FileNotFoundError:
        print(f"'{filename}' 파일을 찾을 수 없습니다. 메뉴 4번으로 CSV 파일을 먼저 내보내주세요.")    
    except Exception as e:
        print(f"시각화 중 오류 발생: , {e}")