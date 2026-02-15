import streamlit as st
import time
import random

# إعدادات الصفحة
st.set_page_config(page_title="Security Scanner", page_icon="🛡️")

# ستايل الهكر
st.markdown("<style>.stApp { background-color: #000000; color: #00FF41; direction: rtl; }</style>", unsafe_allow_html=True)

# نصوص المقلب
msg_1 = "جاري الاتصال بالسيرفر المركزي..."
msg_2 = "اختراق الجدار الناري... تم"
msg_3 = "صلاحيات المسؤول: تم الحصول عليها"
msg_4 = "جاري سحب سجل المكالمات والرسائل..."
msg_5 = "فتح الكاميرا الأمامية... وضع التخفي"
msg_6 = "جاري رفع الصور إلى السيرفر..."
msg_7 = "تشفير ملفات الجهاز بالكامل..."

if 'access_granted' not in st.session_state:
    st.session_state.access_granted = False

if not st.session_state.access_granted:
    st.title("🛡️ نظام الفحص الموحد")
    if st.button("بدء فحص الثغرات"):
        st.session_state.access_granted = True
        st.rerun()
else:
    terminal_logs = st.empty()
    logs = ""
    processes = [msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7]

    for p in processes:
        logs += "> " + p + "\n"
        terminal_logs.code(logs)
        time.sleep(random.uniform(2.5, 4.0))

    st.write("---")
    st.error("🚨 تم اختراق الخصوصية بنجاح 🚨")
    time.sleep(2)

    count_area = st.empty()
    for i in range(5, 0, -1):
        count_area.header("تدمير البيانات خلال " + str(i) + "...")
        time.sleep(1)
    
    count_area.empty()
    
    try:
        st.image("victim.png", caption="الحالة: تم الاختراق بنجاح")
    except:
        st.error("تم سحب الصورة بنجاح")

    st.audio("https://www.soundjay.com/buttons/beep-01a.mp3")
    
    st.warning("تم سحب كافة بياناتك بنجاح")
    st.info("لا تغلق الصفحة، جاري تشفير الذا
