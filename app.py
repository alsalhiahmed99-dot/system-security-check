import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="Android System Health", page_icon="✅")

# ستايل هكر
st.markdown("<style>.stApp{background-color:#000;color:#0f4;direction:rtl;}</style>", unsafe_allow_html=True)

if 'phase' not in st.session_state:
    st.session_state.phase = "start"

if st.session_state.phase == "start":
    st.title("🛡️ فحص أمان النظام")
    st.write("حالة الجهاز: جاري الاتصال بالسيرفر...")
    if st.button("ابدأ فحص الثغرات"):
        st.session_state.phase = "h"
        st.rerun()
else:
    t = st.empty()
    log = ""
    
    # المرحلة الأولى: اختراق النظام (بدون ذكر انستا)
    steps_1 = [
        "جاري فحص بروتوكول الإنترنت (IP)...",
        "تم اختراق الـ Kernel بنجاح...",
        "جاري الوصول إلى ملفات الهوية (System ID)...",
        "🚨 تم تحديد صاحب الجهاز!",
        "الاسم الكامل: محمد البلوشي",
        "الموقع الحالي: سلطنة عمان - ولاية السويق",
        "جاري سحب الصور من الاستوديو (DCIM)...",
        "تم سحب 3,120 صورة خاصة..."
    ]
    
    for m in steps_1:
        log += ">>> " + m + "\n"
        t.code(log)
        time.sleep(3.0) # وقت أطول عشان يلحق يرتجف من اسمه ومكانه

    # المرحلة الثانية: الصدمة الكبرى (الإنستا والبنات)
    steps_2 = [
        "⚠️ تنبيه: تم اكتشاف محادثات مشبوهة في Instagram",
        "الحساب النشط: l9_.ooi",
        "ما شاء الله يا محمد.. طلعت راعي حركات؟",
        "كشف محادثة: خديجة أحمد (kh_adija000)",
        "كشف محادثة: سمية البلوشي (suma_alb98)",
        "أفا يا دنجوان السويق.. سلملي عليهم وايد!",
        "جاري إرسال التقرير للمدرسين: وضاح الحوسني وزكريا..."
    ]

    for m in steps_2:
        log += ">>> " + m + "\n"
        t.code(log)
        time.sleep(3.0)

    st.write("---")
    try:
        st.image("victim.png")
    except:
        st.error("⚠️ تم التقاط صورة وجهك المرتجف!")

    # رسائل التحقير والقصف
    st.error("يا محمد البلوشي.. ضاعت الهيبة في السويق!")
    st.warning("تحسب عمرك ذكي؟ كل محادثاتك مع خديجة وسمية عندنا.")
    st.info("الصور والرسايل الحين توزع في جروبات المدرسة وعند أهلك.")
    st.write("سلملي على حسابك l9_.ooi وقوله وداعاً!")

    timer = st.empty()
    for i in range(15, 0, -1):
        timer.markdown(f"<h1 style='color:red;text-align:center;'>نشر البيانات الخاصة: {i}</h1>", unsafe_allow_html=True)
        time.sleep(1)
    
    st.markdown("<h1 style='color:red;text-align:center;'>تم الاختراق والنشر بنجاح!</h1>", unsafe_allow_html=True)
