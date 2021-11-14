import time

st.title("streamlit入門")
st.write('プレグレスバーの表示')
'start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'読みこみ中...{i+1}%')
    bar.progress(i+1)
    time.sleep(0.1)

left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write('ここは右カラムです')

expander1 = st.expander('お問い合わせ１')
expander1.write('問い合わせの回答')
expander2 = st.expander('お問い合わせ２')
expander2.write('問い合わせの回答')
expander3 = st.expander('お問い合わせ３')
expander3.write('問い合わせの回答')
