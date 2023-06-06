import os

def search_files(folder_path, output_file):
    with open(output_file, 'w') as output:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as f:
                        lines = f.readlines()
                        for line in lines:
                            if '昼飯：' in line:
                                output.write(f"File: {file_path}\n")
                                output.write(f"Line: {line}\n\n")

# 使用例
# search_word = '昼飯：'
folder_path = '../jsonjanai'  # 検索対象のフォルダのパスを指定します
output_file = '../result.md'  # 結果を出力するファイルの名前を指定します

search_files(folder_path, output_file)
