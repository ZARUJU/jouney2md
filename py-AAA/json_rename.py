import json
import os
from datetime import datetime

# JSONファイルが格納されたフォルダのパス
folder_path = 'json'

# フォルダ内のファイルを取得
file_list = os.listdir(folder_path)

for file_name in file_list:
    if file_name.endswith('.json'):  # 拡張子が.jsonのファイルのみ処理する
        # JSONファイルのパス
        json_file = os.path.join(folder_path, file_name)

        # JSONファイルを読み込む
        with open(json_file, 'r') as f:
            data = json.load(f)

        # date_journalの値を取得
        date_journal_unix = data['date_journal']

        # 下3桁を削除
        date_journal_unix = int(date_journal_unix / 1000)

        # UNIX時間から日時文字列に変換
        date_journal = datetime.fromtimestamp(date_journal_unix).strftime('%Y-%m-%d_%H-%M')

        # ファイル名を生成
        new_file_name = f"{date_journal}.json"

        # 新しいファイル名でJSONファイルを移動
        new_file_path = os.path.join(folder_path, new_file_name)
        os.rename(json_file, new_file_path)

print(f"jsonをリネームしました。")
