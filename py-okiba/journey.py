import os
import json
from datetime import datetime

def read_json_files(folder_path):
    date_journal_list = []
    text_list = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                json_data = json.load(file)
                if 'date_journal' in json_data:
                    date_journal_value = str(json_data['date_journal'])
                    # 下位3桁を削除する例
                    modified_date_journal_value = date_journal_value[:-3]
                    # UNIX時間から日時文字列に変換する例
                    date_journal_string = datetime.fromtimestamp(int(modified_date_journal_value)).strftime('%Y-%m-%d %H:%M')
                    date_journal_list.append(date_journal_string)
                if 'text' in json_data:
                    text_value = json_data['text']
                    # 特定の文字列を削除する例（ここでは "<p dir=\"auto\">" と "</p>" を削除）
                    modified_text_value = text_value.replace("<p dir=\"auto\">", "").replace("</p>", "")
                    text_list.append(modified_text_value)

    # date_journalを昇順にソートし、textも対応するように並び替える
    date_journal_list, text_list = zip(*sorted(zip(date_journal_list, text_list)))

    return date_journal_list, text_list

def save_results_to_markdown(file_path, date_journal_values, text_values):
    with open(file_path, 'w') as file:
        for i in range(len(date_journal_values)):
            file.write(f"- {date_journal_values[i]}\n")
            file.write(f"  {text_values[i]}\n")

folder_path = './jsonjson'  # 対象のフォルダパスを指定してください
date_journal_values, text_values = read_json_files(folder_path)

result_file = 'result.md'

# 既存のファイルがあれば削除
if os.path.exists(result_file):
    os.remove(result_file)

# 結果をマークダウン形式でファイルに保存
save_results_to_markdown(result_file, date_journal_values, text_values)

print(f"結果が {result_file} に保存されました。")
