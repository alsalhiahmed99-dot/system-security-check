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
    st.write("حالة الجهاز: غير معروف")
    if st.button("ابدأ فحص الهوية"):
        st.session_state.phase = "h"
        st.rerun()
else:
    t = st.empty()
    log = ""
    # خطوات الاختراق مقسمة لضمان عدم حدوث SyntaxError
    m1 = "جاري فحص بروتوكول الإنترنت..."
    m2 = "تم اختراق الـ Kernel... الوصول للملفات"
    m3 = "الاسم الكامل: محمد البلوشي"
    m4 = "الموقع: سلطنة عمان - السويق"
    m5 = "الحساب: l9_.ooi"
    m6 = "كشف محادثات خديجة أحمد (kh_adija000)"
    m7 = "كشف رسايل سمية البلوشي (suma_alb98)"
    m8 = "أفا يا دنجوان السويق.. سلملي عليهم!"
    m9 = "إرسال نسخة لـ وضاح الحوسني وزكريا..."
    
    for m in [m1, m2, m3, m4, m5, m6, m7, m8, m9]:
        log += ">>> " + m + "\n"
        t.code(log)
        time.sleep(2.5)

    st.write("---")
    try:
        st.image("victim.png")
    except:
        st.error("تم التقاط صورة وجهك!")

    # نصوص التحقير (مقسمة لقطع صغيرة جداً)
    t1 = "بانت حقيقتك يا محمد البلوشي!"
    t2 = "ما شاء الله.. مسوي مطوع وأنت مع خديجة وسمية؟"
    t3 = "صورك ورسايلك صارت عند أهلكم وعند المدرسين وضاح وزكريا
