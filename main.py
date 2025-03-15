import streamlit as st

def main():
    top_page = st.Page(
        page="contents/top_page.py", title="トップ", icon=":material/home:", default=True
    )
    about = st.Page(
        page="contents/denntaku_page.py", title="電卓", icon=":material/apps:"
    )
    about2 = st.Page(
        page="contents/memo_page.py", title="メモ", icon=":material/apps:"
    )
    pg = st.navigation([top_page, about,about2])
    pg.run()

# ユーザー名とパスワードを辞書で管理
user_credentials = {}
st.session_state.show_input = True

with open('text3.txt', 'r', encoding="utf-8") as file:
    for line in file:
        # 行を分割してユーザー名とパスワードを取得
        username, password = line.strip().split(':')
        user_credentials[username] = password
if st.session_state.show_input == True:
    username = st.text_input("ユーザー名:")
    password = st.text_input("パスワード:", type="password")
    if st.button("ログイン"):
        if username in user_credentials and user_credentials[username] == password:
            st.write("ようこそ、" + username + "さん！")
            st.session_state.show_input = False
            if __name__ == "__main__":
                main()
        else:
            st.write("ユーザー名またはパスワードが間違っています。")
