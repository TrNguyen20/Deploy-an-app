import sqlite3

def init_sqlite_db(db_name="mes_mvp.db"):
    """
    Input: Tên file database.
    Action: Kết nối (tạo mới nếu chưa có) và thực thi schema 3 bảng MES cốt lõi.
    Database thay đổi: File .db được tạo tại thư mục local với cấu trúc rỗng chuẩn xác.
    """
    # Khởi tạo kết nối (tạo file db nếu chưa tồn tại)
    conn = sqlite3.connect(db_name)
    
    # Bật tính năng kiểm soát Khóa ngoại (Foreign Keys) bắt buộc đối với SQLite
    conn.execute("PRAGMA foreign_keys = ON;")
    
    cursor = conn.cursor()

    # Thực thi Schema
    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            quantity_total INTEGER NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS production_plan (
            plan_id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            plan_qty INTEGER NOT NULL,
            plan_date DATE NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders (order_id) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS production_actual (
            actual_id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            actual_qty INTEGER NOT NULL,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (order_id) REFERENCES orders (order_id) ON DELETE CASCADE
        );
    """)
    
    conn.commit()
    conn.close()

# Chạy thử kiểm tra
if __name__ == "__main__":
    init_sqlite_db()
    print("Database SQLite đã được khởi tạo thành công.")