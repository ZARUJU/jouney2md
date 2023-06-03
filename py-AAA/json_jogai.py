import os
import sys

# 日付を拡大

def delete_json_files_except_title(folder_path, target_strings):
    for filename in os.listdir(folder_path):
        if filename.endswith('.json') and not any(target_string in filename for target_string in target_strings):
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)
    print(f"不要なJSONファイルを削除しました")

# 使用例
arg1 = sys.argv[1]
folder_path = '../json'
target_strings = [arg1]
delete_json_files_except_title(folder_path, target_strings)

