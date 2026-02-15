import streamlit as st
import time
import random

# إعدادات الصفحة - اسم يوحي بالأمان التام
st.set_page_config(page_title="Android System Health Check", page_icon="✅")

# ستايل هكر يتحول من أبيض (أمان) إلى أحمر (خطر)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FF41; font-family: 'Courier New', monospace; direction: rtl; }
    .stCode { background-color: #050505; color: #00FF41 !important; border: 1px solid #00FF41; }
    </style>
    """, unsafe_allow_html=True)

if 'phase' not in st.session_state:
    st.session_state.phase = "start"

if st.session_state.phase == "start":
    st.title("🛡️ فحص أمان النظام")
    st.write("حالة الجهاز: غير معروف")
    st.write("موقع الدخول: جاري التحديد...")
    if st.button("ابدأ فحص الهوية الرقمية"):
        st.session_state.phase = "hacking"
        st.rerun()

else:
    t = st.empty()
    log = ""
    # خطوات الرعب: من مجهول إلى محمد البلوشي
    steps = [
        "جاري فحص بروتوكول الإنترنت...",
        "تعذر تحديد الهوية... محاولة تجاوز الجدار الناري",
        "تم اختراق الـ Kernel... الوصول إلى ملفات النظام",
        "جاري سحب بيانات البطاقة الشخصية...",
        "🚨 تم تحديد الهدف بنجاح!",
        "الاسم الكامل: محمد البلوشي",
        "الموقع: سلطنة عمان - شمال الباطنة - السويق",
        "الحساب النشط: l9_.ooi",
        "جاري سحب صور الاستوديو (4,291 صورة)...",
        "تم الوصول إلى محادثات 'الخزي'...",
        "ما شاء الله.. وطلعت خبير في البنات يا محمد؟",
        "سحب صور خديجة أحمد (kh_adija000)...",
        "سحب رسايل سمية البلوشي (suma_alb98)...",
        "أفا يا دنجوان السويق.. سلملي عليهم وايد!",
        "إرسال نسخة لـ وضاح الحوسني وزكريا البلوشي الحين..",
        "فتح الكاميرا الأمامية.. تم التقاط صورة وجهك المرتجف"
    ]
    
    for s in steps:
        log += ">>> " + s + "\n"
        t.code(log)
        time.sleep(2.5)

    st.write("---")
    
    try:
        st.image("victim.png")
    except:
        st.error("⚠️ تم سحب صورة وجهك من الكاميرا فوراً!")

    st.audio("https://www.soundjay.com/buttons/beep-01a.mp3")
    
    # رسالة التحقير والصدمة
    st.markdown("<div style='border:5px solid red;padding:25px;text-align:center;background-color:#1a0000;'>", unsafe_allow_html=True)
    st.markdown("<h1 style='color:red;'>بانت حقيقتك يا محمد البلوشي!</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:20px;'>
