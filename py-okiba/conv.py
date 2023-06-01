import os
import re

folder_path = "conv"

# フォルダ内のファイルを走査
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    
    # マークダウンファイルであるかを確認
    if file_name.endswith(".md"):
        # ファイルを読み込み、改行を削除
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            content = re.sub(r"\n+", "\n", content)
        
        # 改行を削除した内容でファイルを上書き保存
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
