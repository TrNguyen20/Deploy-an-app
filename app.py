import sqlite3
import pandas as pd
import streamlit as st

# 1. Kết nối Database (Tự động tạo file mes_mvp.db nếu chưa có)
conn = sqlite3.connect('mes_mvp.db', check_same_thread=False)

# 2. Khởi tạo Schema tối giản cho MVP
def init_db():
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id TEXT PRIMARY KEY,
            product_name TEXT,
            plan_qty INTEGER,
            actual_qty INTEGER DEFAULT 0
        )
    ''')
    conn.commit()

init_db()

# 3. Giao diện Web-app Streamlit
st.title("MES MVP - Theo dõi tiến độ")

# Form nhập liệu Actual
st.subheader("Cập nhật sản lượng")
with st.form("update_form"):
    order_input = st.text_input("Mã đơn hàng (Order ID)")
    actual_input = st.number_input("Số lượng thực tế (Actual Qty)", min_value=0)
    submitted = st.form_submit_button("Xác nhận")

    if submitted and order_input:
        cursor = conn.cursor()
        # UPSERT logic cơ bản cho SQLite
        cursor.execute('''
            INSERT INTO orders (order_id, actual_qty) 
            VALUES (?, ?)
            ON CONFLICT(order_id) DO UPDATE SET actual_qty = actual_qty + ?
        ''', (order_input, actual_input, actual_input))
        conn.commit()
        st.success(f"Đã cập nhật {actual_input} sản phẩm cho đơn {order_input}")

# Hiển thị trạng thái
st.subheader("Trạng thái sản xuất")
df = pd.read_sql_query("SELECT * FROM orders", conn)
st.dataframe(df)