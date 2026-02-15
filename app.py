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
    # وضع النصوص في قائمة (List) لتجنب أخطاء السطور الطويلة
    steps = [
        "جاري فحص بروتوكول الإنترنت...",
        "تم اختراق الـ Kernel... الوصول للملفات",
        "الاسم الكامل: محمد البلوشي",
        "الموقع: سلطنة عمان - السويق",
        "الحساب: l9_.ooi",
        "كشف محادثات خديجة أحمد (kh_adija000)",
        "كشف رسايل سمية البلوشي (suma_alb98)",
        "أفا يا دنجوان السويق.. سلملي عليهم!",
        "إرسال نسخة لـ وضاح الحوسني وزكريا..."
    ]
    
    for m in steps:
        log += ">>> " + m + "\n"
        t.code(log)
        time.sleep(2.5)

    st.write("---")
    try:
        st.image("victim.png")
    except:
        st.error("⚠️ تم التقاط صورة وجهك!")

    # نصوص التحقير مقسمة لضمان عدم انقطاع السطر
    st.error("بانت حقيقتك يا محمد البلوشي!")
    
    st.warning("ما شاء الله.. مسوي مطوع وأنت مع خديجة وسمية؟")
    
    st.info("صورك ورسايلك صارت عند أهلكم وعند المدرسين وضاح وزكريا.")
    
    st.write("سلملي على حسابك l9_.ooi وعلى هيبتك في السويق!")

    timer = st.empty()
    for i in range(15, 0, -1):
        timer.markdown(f"<h1 style='color:red;text-align:center;'>تدمير الذاكرة: {i}</h1>", unsafe_allow_html=True)
        time
