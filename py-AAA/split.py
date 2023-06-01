import re
import datetime
import os

delimiter = "起床"
start_date = datetime.date(2023, 4, 17)  # ファイル名の最初の日付
output_directory = "./split-output"  # 出力先ディレクトリ

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

with open('result.md', 'r') as input_file:
    lines = input_file.readlines()

segments = []
current_segment = ""

for line in lines:
    if delimiter in line:
        if current_segment:
            segments.append(current_segment)
            current_segment = ""
    current_segment += line

if current_segment:
    segments.append(current_segment)

for i, segment in enumerate(segments):
    current_date = start_date + datetime.timedelta(days=i)
    formatted_date = current_date.strftime("%Y%m%d")
    output_file_name = os.path.join(output_directory, f"{formatted_date}.md")
    with open(output_file_name, 'w') as output_file:
        output_file.write(segment)
