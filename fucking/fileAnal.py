import csv
import glob

def safe_float_conversion(value):
    try:
        return float(value)
    except ValueError:
        return 0

def sum_from_eighth_column(file_name):
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        row_count = 0
        results_gyungro = []
        results_jangaean = []
        for row in csv_reader:
            row_count += 1
            row_string = ''.join(row)
            if '경로' in row_string:
                values = row[7:]
                value_sum = sum(map(safe_float_conversion, values))
                results_gyungro.append(value_sum)
            if '장애인' in row_string:
                values = row[7:]
                value_sum = sum(map(safe_float_conversion, values))
                results_jangaean.append(value_sum)
        return results_gyungro, results_jangaean

folder_path = "fucking/csvFiles/화곡/*.csv"  #폴더/파일 경로 넣으면 돼요. 자세한 건 구글에 glob.glob() 검색하시면 나와요.
csv_files = glob.glob(folder_path)
total_results_gyungro = []
total_results_jangaean = []

for file_name in csv_files:
    results_gyungro, results_jangaean = sum_from_eighth_column(file_name)
    total_results_gyungro.extend(results_gyungro)
    total_results_jangaean.extend(results_jangaean)

total_sum_gyungro = sum(total_results_gyungro)
total_sum_jangaean = sum(total_results_jangaean)

# 결과 출력
print(f"경로 인원 : {total_sum_gyungro}")
print(f"장애 인원 : {total_sum_jangaean}")
