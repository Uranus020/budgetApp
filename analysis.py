import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

try:
    plt.rcParams['font.family'] = 'AppleGothic'
except:
    plt.rcParams['font.family'] = 'Malgun Gothic'

def search_expenses(expenses):
    return


def monthly_report(expenses):
    return






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