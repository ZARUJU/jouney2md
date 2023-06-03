# 「~」の処理を行うプログラム


def remove_newline_after_pattern(file_path, pattern):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if pattern in line:
                line = line.replace(pattern + '\n', pattern)
            file.write(line)

def remove_whitespace_before_pattern(file_path, pattern):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if pattern in line:
                line = line.replace('　' + pattern, pattern)
            file.write(line)

# テキストファイルのパスと検索パターンを指定
file_path = '../result.md'
search_pattern = '~'

# 改行削除を実行
remove_newline_after_pattern(file_path, search_pattern)
remove_newline_after_pattern(file_path, search_pattern)

# 空白削除を実行
remove_whitespace_before_pattern(file_path, search_pattern)

