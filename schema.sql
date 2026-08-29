-- Bảng 1: Danh sách Đơn hàng
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    quantity_total INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Bảng 2: Kế hoạch Sản xuất
-- Hỗ trợ quan hệ 1-N (1 order_id có thể có nhiều dòng plan_date/ca khác nhau)
CREATE TABLE IF NOT EXISTS production_plan (
    plan_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    plan_qty INTEGER NOT NULL,
    plan_date DATE NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders (order_id) ON DELETE CASCADE
);

-- Bảng 3: Khối lượng Thực tế
-- Hỗ trợ quan hệ 1-N (1 order_id có thể được cập nhật actual nhiều lần trong ngày)
CREATE TABLE IF NOT EXISTS production_actual (
    actual_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    actual_qty INTEGER NOT NULL,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES orders (order_id) ON DELETE CASCADE
);