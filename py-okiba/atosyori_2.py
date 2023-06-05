# 日付の処理を行うプログラム


def move_text_after_keyword(file_path, keyword):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        previous_line = ''
        for line in lines:
            if keyword in line:
                line = previous_line.strip() + line.partition(keyword)[-1]
                previous_line = ''
            else:
                previous_line = line
            file.write(line)

# テキストファイルのパスと検索キーワードを指定
file_path = '../result.md'
search_keyword = '起床'

# テキスト移動を実行
move_text_after_keyword(file_path, search_keyword)
