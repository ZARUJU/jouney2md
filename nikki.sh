#!/bin/bash

if [ ! -d venv ];then
    python3 -m venv venv
    pip install -r requirements.txt
fi

if [ -d venv ];then
    source venv/bin/activate
fi

    cd py-AAA
# jsonをYYYY-MM-DD_hh-mmに変更
    python3 json_rename.py
# 指定した日付以外のjsonを削除
    python3 json_jogai.py "$@"
# mdにまとめる
    python3 journey_md.py
# 改行等の処理
    python3 atosyori_1.py
# mdから指定日の「MM-DD-」を削除する
# 引数として与えた文字列をファイルの先頭に追加
    text="$1"
    file_path="../result.md"
    echo "$text" | cat - "$file_path" > temp && mv temp "$file_path"