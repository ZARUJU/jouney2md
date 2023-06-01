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
                    date_journal_list.append(modified_date_journal_value)
                if 'text' in json_data:
                    text_value = json_data['text']
                    # 特定の文字列を削除する例（ここでは "<p dir=\"auto\">" と "</p>" を削除）
                    modified_text_value = text_value.replace("<p dir=\"auto\">", "").\
                        replace("</p>", "").\
                        replace("のる", "~").\
                        replace("横川", "移動：　ー 横川").\
                        replace("いつかいち", "五日市").\
                        replace("五日市", "移動：　ー 五日市").\
                        replace("着席", "着席：分前").\
                        replace("終了", "終了：分早い").\
                        replace("ふろはいる", "風呂入る").\
                        replace("風呂入る", "~").\
                        replace("風呂出た", "入浴").\
                        replace("就寝", "就寝<br>").\
                        replace("体温", "体温：").\
                        replace("", "")
                    text_list.append(modified_text_value)
    # date_journalを昇順にソート
    sorted_indices = sorted(range(len(date_journal_list)), key=lambda k: date_journal_list[k])
    date_journal_list = [date_journal_list[i] for i in sorted_indices]
    text_list = [text_list[i] for i in sorted_indices]

    # date_journalを昇順にソート
    sorted_indices = sorted(range(len(date_journal_list)), key=lambda k: date_journal_list[k])
    date_journal_list = [date_journal_list[i] for i in sorted_indices]
    text_list = [text_list[i] for i in sorted_indices]

    # UNIX時間から日時文字列に変換
    date_journal_list = [datetime.fromtimestamp(int(date)).strftime('%H:%M') for date in date_journal_list]

    return date_journal_list, text_list

def save_results_to_markdown(file_path, date_journal_values, text_values):
    with open(file_path, 'w') as file:
        for i in range(len(date_journal_values)):
            file.write(f"{date_journal_values[i]}　{text_values[i]}<br>\n")

def remove_memo_lines(file_a):
    with open(file_a, 'r') as file:
        lines = file.readlines()

    # 「メモ」という文字列を含む行を削除
    lines = [line for line in lines if 'メモ' not in line]

    with open(file_a, 'w') as file:
        file.writelines(lines)

folder_path = './jsonjson'  # 対象のフォルダパスを指定してください
date_journal_values, text_values = read_json_files(folder_path)

result_file = 'result.html'

# 既存のファイルがあれば削除
if os.path.exists(result_file):
    os.remove(result_file)

# 結果をマークダウン形式でファイルに保存
save_results_to_markdown(result_file, date_journal_values, text_values)

remove_memo_lines_file = result_file
remove_memo_lines(remove_memo_lines_file)

print(f"結果が {result_file} に保存されました。")
