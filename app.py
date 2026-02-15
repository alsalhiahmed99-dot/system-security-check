import streamlit as st
import time
import random

# إعدادات الصفحة
st.set_page_config(page_title="نظام الحماية الرقمية", page_icon="🛡️", layout="centered")

# ستايل الهكر الاحترافي
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FF41; font-family: 'Courier New', Courier, monospace; direction: rtl; }
    .stButton>button { background-color: #000000; color: #00FF41; border: 1px solid #00FF41; width: 100%; font-weight: bold; }
    .stError { background-color: #1a0000; color: #ff0000; border: 1px solid #ff0000; text-align: right; }
    </style>
    """, unsafe_allow_html=True)

if 'access_granted' not in st.session_state:
    st.session_state.access_granted = False

if not st.session_state.access_granted:
    st.title("🛡️ نظام الفحص الموحد")
    st.write("حالة الجهاز: غير محمي")
    if st.button("بدء فحص الثغرات"):
        st.session_state.access_granted = True
        st.rerun()

else:
    status_text = st.empty()
    terminal_logs = st.empty()
    logs = ""

    # قائمة العمليات (تأكد من نسخها كاملة مع علامات التنصيص)
    processes = [
        "جاري الاتصال بالسيرفر المركزي...",
        "اختراق الجدار الناري... تم",
        "صلاحيات المسؤول: تم الحصول عليها",
        "جاري سحب سجل المكالمات والرسائل...",
        "فتح الكاميرا الأمامية... وضع التخفي",
        "جاري رفع الصور إلى السيرفر...",
        "تشفير ملفات الجهاز بالكامل..."
    ]

    for p in processes:
        logs += f"> {p}\n"
        terminal_logs.code(logs, language="bash")
        time.sleep(random.uniform(2.0, 3.5))

    st.write("---")
    st.error("🚨 تم اختراق الخصوصية بن
