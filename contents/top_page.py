import streamlit as st
import datetime
import time

st.title("こんにちは")

# 曜日を漢字に変換する辞書
weekdays = {
    0: "(月)",
    1: "(火)",
    2: "(水)",
    3: "(木)",
    4: "(金)",
    5: "(土)",
    6: "(日)"
}

# 更新する場所を作る
time_display = st.empty()
date_display = st.empty()
greeting_display = st.empty()

while True:
    # 現在の日時を取得
    now = datetime.datetime.now()

    # 時刻をフォーマットして取得
    current_time = now.strftime("%H:%M:%S")  
    # 日付をフォーマットして取得
    current_date = now.strftime("%Y年%m月%d日")  
    # 曜日を取得
    weekday_number = now.weekday()
    weekday_name = weekdays[weekday_number]  

    # 時間帯による挨拶を設定
    hour = now.hour
    if hour < 9:
        greeting = "おはよう"
    elif hour < 18:
        greeting = "こんにちは"
    else:
        greeting = "こんばんは"

    # 時刻を表示
    time_display.markdown(f"<h1 style='text-align: center; font-size: 60px;'>{current_time}</h1>", unsafe_allow_html=True)
    # 日付と曜日を表示
    date_display.markdown(f"<h1 style='text-align: center; font-size: 60px;'>{current_date} {weekday_name}</h1>", unsafe_allow_html=True)

    # 1秒待つ
    time.sleep(1)


