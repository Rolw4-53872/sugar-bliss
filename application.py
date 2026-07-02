from flask import Flask, render_template, request, redirect, url_for, flash
from database import db, Order
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import os

# ===================================================
# 1. إعداد تطبيق Flask وتعريف الأسعار
# ===================================================

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cake.db'
application.config['SECRET_KEY'] = os.urandom(24)

db.init_app(application)

with application.app_context():
    db.create_all()
    print("Database created successfully!")


# ===================================================
# 2. تفعيل لوحة الأدمن
# ===================================================

admin = Admin(application, name='Cake Admin')
admin.add_view(ModelView(Order, db.session))

# ===================================================
# 3. الأسعار الأساسية
# ===================================================

# أسعار المنتجات الأساسية (مأخوذة من قائمة order.html)
PRICES = {
    "كرانشي كراميل": 14,
    "بير بلو": 16,
    "بلو بيري دريم": 14,
    "دولتشي شوكلت": 12,
    "كعكة التوت والكرز المكرمل": 30,
    "كيك قراندي لافندر": 50,
    "رانشي تشوكلت": 50,
    "ريد بيري كيك": 45,
    "بودينغ التشوكلت": 14,
    "بودينغ التوت": 18,
    "بودينغ بلو بيري": 12,
    "بودينغ الكارميل": 15
}

# أسعار ثابتة للإضافات والتوصيل (لأغراض الحساب)
EXTRA_PRICE = 5 
DELIVERY_PRICE = 10 

# ===================================================
# 2. دوال عرض الصفحات (GET Routes)
# ===================================================

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/hht')
def hht_page():
    return render_template('hht.html')

@application.route('/mine')
def mine_page():
    return render_template('mine.html')

@application.route('/order')
def order_page():
    return render_template('order.html')

@application.route('/orders')
def orders_page():
    all_orders = Order.query.all()
    return render_template('orders.html', orders=all_orders)


# ===================================================
# 3. دالة معالجة إرسال نموذج الطلب (POST Route - بدون خصم)
# ===================================================

@application.route('/submit_order_action', methods=['POST'])
def submit_order_action():
    
    # --- 1. قراءة البيانات ---
    try:
        product_full_name = request.form['product'].split(' - ')[0].strip() 
    except:
        product_full_name = "منتج غير محدد"
        
    name = request.form.get('name', 'عميلنا العزيز')
    phone = request.form.get('phone', '').strip() 
    address = request.form.get('address', '').strip() 
    email = request.form.get('email', '').strip() 

    pickup_date = request.form.get('pickupDate', '').strip() 
    pickup_time = request.form.get('pickupTime', '').strip() 
    quantity = int(request.form.get('quantity', 1))
    extras_list = request.form.getlist('extras')
    delivery_type = request.form.get('deliveryType')
    sweetness = request.form.get('sweetness')
    delivery_cost = 0

    # --- 2. حساب الإجمالي ---
    
    base_price = PRICES.get(product_full_name, 0)
    item_total = base_price * quantity
    
    extras_cost = len(extras_list) * EXTRA_PRICE
    
    if delivery_type == 'delivery':
        delivery_cost = DELIVERY_PRICE
    
    # حساب الإجمالي الكلي (يشمل التوصيل والإضافات)
    total_pre_discount = item_total + extras_cost + delivery_cost
    
    # [التعديل هنا لإلغاء الخصم]: قيمة الخصم دائماً صفر
    discount = 0
        
    # [التعديل هنا لإلغاء الخصم]: الإجمالي النهائي هو نفسه الإجمالي قبل الخصم
    final_total = total_pre_discount
    

    # ===================================================
    #  4. حفظ الطلب في قاعدة البيانات
    # ===================================================

    new_order = Order(
        name=name,
        phone="",              # لأن فورمك ما يحتوي رقم هاتف حالياً
        email="",              # ولا بريد — ممكن نضيفهم لاحقاً
        address=address,       
        product=product_full_name,
        quantity=quantity,
        sweetness=int(sweetness),
        extras=",".join(extras_list),
        delivery_method=delivery_type,
        total=final_total
      
    )

    db.session.add(new_order)
    db.session.commit()

 # ===================================================
    # --- . عرض صفحة التأكيد مباشرة ) ---
    return render_template('confirmation.html', 
                            customer_name=name,
                            product_name=product_full_name,
                            quantity=quantity,
                            price=base_price,
                            extras=extras_list,
                            sweetness=sweetness,
                            
                            # تمرير جميع متغيرات الحساب (discount=0)
                            total_pre_discount=total_pre_discount,
                            discount=discount,
                            final_total=final_total,

                              address=address,
                            delivery_type=delivery_type,
            
        
                            pickup_date=pickup_date,
                            pickup_time=pickup_time,
                            delivery_cost=delivery_cost,
                            

                           
                           
                            )


# ===================================================
# 6. تشغيل التطبيق
# ===================================================

if __name__ == '__main__':
    application.run(debug=True)
