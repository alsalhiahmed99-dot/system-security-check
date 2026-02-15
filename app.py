import streamlit as st
import time

# إعدادات الصفحة - اسم يوحي بكارثة
st.set_page_config(page_title="CRITICAL SYSTEM FAILURE", page_icon="💀")

# ستايل هكر مظلم
st.markdown("<style>.stApp{background-color:#000;color:#0f4;direction:rtl;}</style>", unsafe_allow_html=True)

if 'phase' not in st.session_state:
    st.session_state.h = False

if not st.session_state.h:
    st.title("🛡️ نظام فحص أمان أجهزة أندرويد")
    st.write("حالة الجهاز: جاري التحقق من الثغرات...")
    if st.button("بدء الفحص العميق"):
        st.session_state.h = True
        st.rerun()
else:
    t = st.empty()
    log = ""
    
    # المرحلة الأولى: كشف الهوية
    steps_1 = [
        "جاري فحص بروتوكول الإنترنت...",
        "تم تجاوز الجدار الناري بنجاح...",
        "🚨 تم تحديد صاحب الجهاز!",
        "الاسم الكامل: محمد البلوشي",
        "الموقع: سلطنة عمان - ولاية السويق",
        "جاري سحب الصور... تم سحب 3,120 صورة"
    ]
    
    for m in steps_1:
        log += ">>> " + m + "\n"
        t.code(log)
        time.sleep(3.0)

    # المرحلة الثانية: كشف المستور (خديجة وسمية)
    steps_2 = [
        "⚠️ تنبيه: تم اكتشاف محادثات مشبوهة",
        "الحساب النشط: l9_.ooi",
        "ما شاء الله يا محمد.. طلعت راعي حركات؟",
        "كشف محادثة: خديجة أحمد (kh_adija000)",
        "كشف محادثة: سمية البلوشي (suma_alb98)",
        "أفا يا دنجوان السويق.. سلملي عليهم!",
        "إرسال التقرير للمدرسين: وضاح وزكريا..."
    ]

    for m in steps_2:
        log += ">>> " + m + "\n"
        t.code(log)
        time.sleep(3.0)

    st.write("---")
    st.error("يا محمد البلوشي.. ضاعت الهيبة في السويق!")
    st.warning("كل محادثاتك وصورك صارت عندنا الحين.")

    # المؤقت المرعب
    timer_area = st.empty()
    for i in range(15, 0, -1):
        txt = "نشر الفضائح وتصفير الذاكرة خلال: " + str(i)
        timer_area.error(txt)
        time.sleep(1)
    
    # النهاية المرعبة - شاشة الموت السوداء
    st.empty()
    st.markdown("<h1 style='text-align:center;color:red;font-size:100px;'>💀</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center;color:red;'>GAME OVER</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;color:white;'>تم نشر جميع البيانات بنجاح.</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;color:gray;'>سيتم إيقاف تشغيل الجهاز خلال 5 ثواني...</p>", unsafe_allow_html=True)
