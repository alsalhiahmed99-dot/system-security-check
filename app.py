import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="Android System Health", page_icon="✅")

# ستايل هكر
st.markdown("<style>.stApp{background-color:#000;color:#0f4;direction:rtl;}</style>", unsafe_allow_html=True)

if 'phase' not in st.session_state:
    st.session_state.phase = "start"

if st.session_state.phase == "start":
    st.title("🛡️ نظام فحص أمان أجهزة أندرويد")
    st.write("حالة الجهاز: جاري التحقق من الثغرات...")
    if st.button("بدء الفحص الشامل"):
        st.session_state.phase = "h"
        st.rerun()
else:
    t = st.empty()
    log = ""
    
    # المرحلة الأولى: كشف الهوية (الرعب التدريجي)
    steps_1 = [
        "جاري فحص بروتوكول الإنترنت الخاص بك...",
        "تم تجاوز الجدار الناري بنجاح...",
        "🚨 تم تحديد صاحب الجهاز!",
        "الاسم الكامل: محمد البلوشي",
        "الموقع: سلطنة عمان - ولاية السويق",
        "جاري سحب الصور من الاستوديو... تم سحب 3,120 صورة"
    ]
    
    for m in steps_1:
        log += ">>> " + m + "\n"
        t.code(log)
        time.sleep(3.0) # نعطيه وقت عشان يرتجف

    # المرحلة الثانية: كشف المستور (التحقير والقصف)
    steps_2 = [
        "⚠️ تنبيه: تم اكتشاف محادثات مشبوهة في Instagram",
        "الحساب النشط: l9_.ooi",
        "ما شاء الله يا محمد.. طلعت راعي حركات؟",
        "كشف محادثة: خديجة أحمد (kh_adija000)",
        "كشف محادثة: سمية البلوشي (suma_alb98)",
        "أفا يا دنجوان السويق.. سلملي عليهم وايد!",
        "إرسال التقرير للمدرسين: وضاح الحوسني وزكريا..."
    ]

    for m in steps_2:
        log += ">>> " + m + "\n"
        t.code(log)
        time.sleep(3.0)

    st.write("---")
    
    # رسائل التهديد الأخيرة
    st.error("يا محمد البلوشي.. ضاعت الهيبة في السويق!")
    st.warning("كل محادثاتك مع خديجة وسمية صارت عندنا الحين.")
    st.info("الصور والرسايل الحين توزع في جروبات المدرسة.")

    # مؤقت التدمير (قمة الرعب)
    timer_area = st.empty()
    for i in range(10, 0, -1):
        timer_area.markdown(f"<h1 style='color:red;text-align:center;'>نشر الفضيحة وتدمير الجهاز: {i}</h1>", unsafe_
