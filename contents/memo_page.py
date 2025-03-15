import streamlit as st

st.title("メモ帳")

txt = st.text_area(
    "ここに入力してください。",
    "書き終わったらコマンドキーとエンターキーを"
    "同時に押してください。",
)
st.write(f"あなたは {len(txt)} 文字書きました。")
def clear_file(file_path):
    try:
        with open(file_path, "w") as file:
            file.truncate(0)
        return True
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return False
    
with open('text2.txt','a',encoding="utf-8") as file:
    if st.button("保存"):
        file.write(txt + '\n') #'\n'は改行を表すよ!
        st.info("保存しました。")
    if st.button("メモのデータを削除"):
        if clear_file('text2.txt'):
            st.success("データを削除しました。")
        else:
            st.error("削除に失敗しました。")
with open('text2.txt','r',encoding="utf-8") as file:
    if st.button("履歴を引き出す"):
        content = file.read()
        st.text_area("履歴",content,)