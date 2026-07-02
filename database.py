from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)

    # بيانات العميل
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))  # يطلع فقط عند اختيار التوصيل

    # تفاصيل الطلب
    product = db.Column(db.String(100), nullable=False)   # اسم المنتج
    price = db.Column(db.Float)                           # سعر المنتج
    quantity = db.Column(db.Integer, default=1)           # الكمية
    sweetness = db.Column(db.Integer)                     # 1-5

    # الإضافات (قائمة مفصولة بفواصل)
    extras = db.Column(db.String(300))                    # مثل: "كريمة إضافية, مكسرات"

    # طريقة الاستلام
    delivery_method = db.Column(db.String(20))            # Pickup / Delivery

    # السعر النهائي
    total = db.Column(db.Float)
