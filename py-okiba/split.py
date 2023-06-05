import re
import datetime
import os
import shutil

delimiter = "起床"
start_date = datetime.date(2023, 5, 1)  # ファイル名の最初の日付
output_directory = "./split-output"  # 出力先ディレクトリ

# 既存の split-output フォルダが存在する場合は削除
if os.path.exists(output_directory):
    shutil.rmtree(output_directory)

# split-output フォルダを作成
os.makedirs(output_directory)

# .gitkeep ファイルを生成
gitkeep_file = os.path.join(output_directory, ".gitkeep")
with open(gitkeep_file, 'w'):
    pass

with open('result.md', 'r') as input_file:
    content = input_file.read()

segments = re.split(delimiter, content)

for i, segment in enumerate(segments):
    current_date = start_date + datetime.timedelta(days=i)
    formatted_date = current_date.strftime("%Y%m%d")
    output_file_name = os.path.join(output_directory, f"{formatted_date}.md")
    with open(output_file_name, 'w') as output_file:
        output_file.write(formatted_date + "\n" + segment)
