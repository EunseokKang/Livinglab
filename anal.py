import pandas as pd

# CSV 파일 경로 설정
csv_file_path = 'final.csv'  # 실제 파일 경로로 변경해주세요.
result_csv_file_path = 'final_3.csv'  # 결과를 저장할 파일 경로로 변경해주세요.

# CSV 파일을 DataFrame으로 읽기
df = pd.read_csv(csv_file_path)

# 3번째 열의 값 평균 및 표준편차 계산
column_3_mean = df.iloc[:, 2].mean()
column_3_std = df.iloc[:, 2].std()

# 평균보다 표준편차의 몇 배 큰지 기준 설정
threshold_multiplier = 2  # 예시로 2배 큰 경우

# 평균보다 threshold_multiplier * 표준편차 큰 행 선택
greater_than_threshold_rows = df[df.iloc[:, 2] > (column_3_mean + threshold_multiplier * column_3_std)]

# 결과를 새로운 CSV 파일에 저장 (index 포함)
greater_than_threshold_rows.to_csv(result_csv_file_path, index=True)

print(f"평균보다 {threshold_multiplier}배 큰 행의 결과를 '{result_csv_file_path}'에 저장했습니다.")
