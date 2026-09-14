import streamlit as st
import random

st.title("💸 課堂 PaaS 測試：比特幣盲猜賭場")
st.write("目前你的虛擬帳戶餘額：10,000 USDT")

# 模擬簡單的狀態保存 (State Machine)
if 'balance' not in st.session_state:
    st.session_state.balance = 10000

guess = st.radio("下一秒比特幣是漲還是跌？", ["漲 📈", "跌 📉"])
bet = st.number_input("下注金額", min_value=100, max_value=5000, step=100)

if st.button("確認下注發送 API"):
    result = random.choice(["漲 📈", "跌 📉"])
    st.write(f"伺服器結算結果：{result}")
    if guess == result:
        st.session_state.balance += bet
        st.success(f"贏了！目前餘額：{st.session_state.balance}")
    else:
        st.session_state.balance -= bet
        st.error(f"爆倉！目前餘額：{st.session_state.balance}")