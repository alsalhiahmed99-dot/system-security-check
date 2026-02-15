import streamlit as st
import time
import random

# إعدادات الصفحة
st.set_page_config(page_title="Security Scanner", page_icon="🛡️")

# ستايل الهكر
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FF41; font-family: 'Courier New', Courier, monospace; direction: rtl; }
    .stButton>button { background-color: #000000; color: #00FF41; border: 1px solid #00FF41; width: 100%; }
    .stError { background-color: #1a0000; color: #ff0000; border: 1px solid #ff0000; text-align: right; }
    </style>
    """, unsafe_allow_html=True)

# نصوص المقلب (مكتوبة بطريقة تمنع أخطاء السنتكس)
msg_1 = "جاري الاتصال بالسيرفر المركزي..."
msg_2 = "اختراق الجدار الناري... تم"
msg_3 = "صلاحيات المسؤول: تم الحصول عليها"
msg_4 = "جاري سحب سجل المكالمات والرسائل..."
msg_5 = "فتح الكاميرا الأمامية... وضع التخفي"
msg_6 = "جاري رفع الصور إلى السيرفر..."
msg_7 = "تشفير ملفات الجهاز بالكامل..."
error_msg = "🚨 تم اختراق الخصوصية بنجاح 🚨"
warning_msg = "تم سحب كافة بياناتك بنجاح"
info_msg = "لا تغلق الصفحة، جاري تشفير الذاكرة..."

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
        logs += f"> {p}\n"
        terminal_logs.code(logs, language="bash")
        time.sleep(random.uniform(2.5, 4.0))

    st.write("---")
    st.error(error_msg)
    time.sleep(2)

    count_area = st.empty()
    for i in range(5, 0, -1):
        count_area.markdown(f"<h2 style='color:red; text-align:center;'>تدمير البيانات خلال {i}...</h2>", unsafe_allow_html=True)
        time.sleep(1)
    
    count_area.empty()
    
    try:
        st.image("victim.png", caption="IP: 156.190.42.11 | الحالة: تم الاختراق")
    except:
        st.error("تم سحب الصورة بنجاح")

    st.audio("https://www.soundjay.com/buttons/beep-01a.mp3")
    
    st.markdown(f"""
    <div style='border: 2px solid red; padding: 15px; text-align: center;'>
        <h2 style='color: red;'>{warning_msg}</h2>
        <p style='color: white;'>{info_msg}</p
