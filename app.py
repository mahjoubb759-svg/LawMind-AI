import streamlit as st
import google.generativeai as genai
import os

# 1. إعدادات الصفحة الأساسية بالمظهر العريض الفخم
st.set_page_config(page_title="LawMind | AI Legal Intelligence", page_icon="⚖️", layout="wide")

# 2. تصميم الـ Frontend الاحترافي المطور مع إخفاء القائمة الجانبية وأدوات المنصة والشعارات السفلية
st.markdown("""
    <style>
    /* 🔴 إخفاء القائمة الجانبية بالكامل (System Status) */
    [data-testid="stSidebar"] {
        display: none !important;
    }
    [data-testid="stSidebarCollapseButton"] {
        display: none !important;
    }
    
    /* 🔴 إخفاء شريط Tعديل العلوي وزر Manage App السفلي للجمهور */
    #MainMenu, footer, header, [data-testid="stDecoration"] {
        visibility: hidden !important;
        display: none !important;
    }
    
    /* 🔴 إخفاء شريط Hosted with Streamlit السفلي المزعج والزر العائم على الهواتف */
    .viewerBadge_container__1QSob, [data-testid="stViewerBadge"], .styles_viewerBadge__NiTeF {
        display: none !important;
        visibility: hidden !important;
    }
    
    /* إخفاء أي أزرار عائمة أو عناصر تابعة لـ Streamlit في أسفل الشاشة */
    div[class^="viewerBadge"] {
        display: none !important;
    }
    
    /* تصحيح الهوامش العلوية والسفلية ليتمركز الموقع بشكل فخم */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
        max-width: 1000px !important;
        margin: 0 auto !important;
    }

    /* إعدادات الخلفية العامة والألوان */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
    }
    
    /* لوغو الميزان الرقمي المتحرك */
    .legal-logo {
        text-align: center !important;
        display: block;
        font-size: 5rem;
        background: linear-gradient(to right, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
        animation: pulse 3s infinite alternate;
    }
    
    /* العنوان الرئيسي للمنصة */
    .main-title {
        text-align: center !important;
        display: block;
        font-size: 3.5rem !important;
        font-weight: 800;
        letter-spacing: 2px;
        background: linear-gradient(to right, #ffffff, #94a3b8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 0px;
        margin-bottom: 5px;
    }
    
    /* العنوان الفرعي */
    .sub-title {
        text-align: center !important;
        display: block;
        color: #38bdf8;
        font-size: 1.2rem;
        font-weight: 400;
        text-transform: uppercase;
        letter-spacing: 4px;
        margin-bottom: 15px;
    }
    
    /* حاوية ونص الرؤية ليتمركز بدقة */
    .vision-container {
        text-align: center !important;
        width: 100%;
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .vision-text {
        text-align: center !important;
        color: #94a3b8;
        font-size: 1.2rem;
        font-weight: 400;
        max-width: 800px;
        line-height: 1.8;
        border-bottom: 1px solid rgba(148, 163, 184, 0.1);
        padding-bottom: 25px;
    }
    
    /* حاوية شارة منتج مغربي */
    .badge-container {
        display: flex;
        justify-content: center;
        width: 100%;
        margin-bottom: 35px;
    }
    .moroccan-badge {
        text-align: center !important;
        color: #065F46 !important;
        font-size: 0.95rem;
        font-weight: bold;
        background-color: #D1FAE5;
        padding: 6px 18px;
        border-radius: 50px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* إطار عرض أسماء المطورين المتمركز في المنتصف تماماً */
    .credits-container {
        display: flex;
        justify-content: center;
        width: 100%;
        margin-top: 50px;
    }
    .team-credits {
        text-align: center !important;
        padding: 15px 30px;
        background: rgba(30, 41, 59, 0.4);
        border-radius: 15px;
        border: 1px solid rgba(148, 163, 184, 0.05);
        width: fit-content;
        font-size: 1rem;
        color: #e2e8f0;
    }
    .team-names {
        color: #38bdf8;
        font-weight: bold;
    }
    
    /* صناديق الاختيار للغة والدولة */
    .selection-box {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(148, 163, 184, 0.1);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }
    .selection-box:hover {
        transform: translateY(-5px);
        border-color: #38bdf8;
        box-shadow: 0 15px 35px rgba(56, 189, 248, 0.2);
    }
    
    @keyframes pulse {
        0% { transform: scale(1); opacity: 0.9; }
        100% { transform: scale(1.05); opacity: 1; }
    }
    
    /* تصحيح الأزرار لتتمركز هندسياً بشكل مستقيم ومفرود وثابت */
    .stButton {
        display: flex !important;
        justify-content: center !important;
        width: 100% !important;
        margin-top: 15px !important;
        margin-bottom: 15px !important;
    }
    .stButton>button {
        background: linear-gradient(90deg, #0284c7 0%, #4f46e5 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 12px 50px !important;
        font-weight: bold !important;
        font-size: 1.1rem !important;
        transition: all 0.3s ease !important;
        white-space: nowrap !important;
        width: auto !important;
        min-width: 250px !important;
        box-shadow: 0 4px 15px rgba(2, 132, 199, 0.2) !important;
    }
    .stButton>button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 0 25px rgba(56, 189, 248, 0.5) !important;
    }
    
    /* فقاعات الشات المستوحاة من ChatGPT */
    .chat-bubble-user {
        background-color: #1e293b;
        padding: 15px 20px;
        border-radius: 20px 20px 0px 20px;
        margin-bottom: 15px;
        border: 1px solid rgba(56, 189, 248, 0.2);
        max-width: 80%;
        margin-left: auto;
    }
    .chat-bubble-ai {
        background-color: #0f172a;
        padding: 20px;
        border-radius: 20px 20px 20px 0px;
        margin-bottom: 15px;
        border: 1px solid rgba(129, 140, 248, 0.2);
        max-width: 80%;
    }
    .footer-custom {
        text-align: center;
        margin-top: 50px;
        color: #64748b;
        font-size: 0.85rem;
    }
    </style>
""", unsafe_allow_html=True)

# 3. إدارة جلسات الذاكرة المؤقتة للتنقل بمرونة بين الواجهات
if "page" not in st.session_state: st.session_state.page = "landing"
if "lang" not in st.session_state: st.session_state.lang = "ar"
if "country" not in st.session_state: st.session_state.country = "Morocco"
if "chat_history" not in st.session_state: st.session_state.chat_history = []

# 🔐 جلب مفتاح Google Gemini السري بأمان عبر خزنة السيرفر لمنع الحظر
if "gemini" in st.secrets:
    GEMINI_API_KEY = st.secrets["gemini"]["api_key"]
    genai.configure(api_key=GEMINI_API_KEY)
else:
    GEMINI_API_KEY = ""

# قاموس الترجمة الفورية الديناميكية
locales = {
    "en": {
        "vision": "The <b>LawMind</b> platform is the first Moroccan and global platform that harnesses artificial intelligence to serve humanity in the field of law.",
        "badge": "100% Moroccan Product 🇲🇦",
        "credits": "💡 Developed by: <span class='team-names'>Mr. Elmahjoub Boumagout</span> & <span class='team-names'>Mrs. ASMA AHLBIHI</span>",
        "select_lang": "Select Language", "select_country": "Select Country", "btn_enter": "Launch Intelligence", "placeholder": "Ask your strict legal question here...", "search_btn": "Consult System", "status_sidebar": "System Status"
    },
    "ar": {
        "vision": "منصة <b>LawMind</b> هي أول منصة مغربية وعالمية تسخر الذكاء الاصطناعي لخدمة البشرية في مجال القانون.",
        "badge": "🇲🇦 منتج مغربي 100%",
        "credits": "💡 من إنجاز: <span class='team-names'>السيد Elmahjoub Boumagout</span> و <span class='team-names'>السيدة ASMA AHLBIHI</span>",
        "select_lang": "حدد اللغة", "select_country": "حدد الدولة", "btn_enter": "إطلاق الذكاء القانوني", "placeholder": "اطرح سؤالك القانوني الصارم هنا...", "search_btn": "استشارة النظام", "status_sidebar": "حالة النظام"
    },
    "fr": {
        "vision": "La plateforme <b>LawMind</b> est la première plateforme marocaine et mondiale qui met l'intelligence artificielle au service de l'humanité dans le domaine du droit.",
        "badge": "Produit 100% Marocain 🇲🇦",
        "credits": "💡 Développé par: <span class='team-names'>M. Elmahjoub Boumagout</span> & <span class='team-names'>Mme ASMA AHLBIHI</span>",
        "select_lang": "Choisir la Langue", "select_country": "Choisir le Pays", "btn_enter": "Lancer l'Intelligence", "placeholder": "Posez votre question juridique stricte ici...", "search_btn": "Consulter le Système", "status_sidebar": "État du Système"
    }
}
current_text = locales[st.session_state.lang]

# ====================================================================
# 🚪 الواجهة الأولى: صفحة الهبوط والإعدادات (Landing Page)
# ====================================================================
if st.session_state.page == "landing":
    st.markdown('<p class="legal-logo">⚖️</p>', unsafe_allow_html=True)
    st.markdown('<p class="main-title">LawMind</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">AI Legal Intelligence</p>', unsafe_allow_html=True)
    
    st.markdown(f'<div class="vision-container"><p class="vision-text">{current_text["vision"]}</p></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="badge-container"><span class="moroccan-badge">{current_text["badge"]}</span></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<div class="selection-box"><h3>🌐 {current_text["select_lang"]}</h3>', unsafe_allow_html=True)
        selected_lang_ui = st.selectbox("Language", ["العربية", "English", "Français"], index=["ar", "en", "fr"].index(st.session_state.lang), label_visibility="collapsed")
        if selected_lang_ui == "English": st.session_state.lang = "en"
        elif selected_lang_ui == "العربية": st.session_state.lang = "ar"
        elif selected_lang_ui == "Français": st.session_state.lang = "fr"
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown(f'<div class="selection-box"><h3>📍 {current_text["select_country"]}</h3>', unsafe_allow_html=True)
        selected_country_ui = st.selectbox("Country", ["Morocco 🇲🇦", "France 🇫🇷", "USA 🇺🇸"], index=["Morocco", "France", "USA"].index(st.session_state.country), label_visibility="collapsed")
        st.session_state.country = selected_country_ui.split()[0]
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.write(" ")
    if st.button(current_text["btn_enter"]):
        st.session_state.page = "chat"
        st.rerun()
            
    st.markdown(f'<div class="credits-container"><div class="team-credits">{current_text["credits"]}</div></div>', unsafe_allow_html=True)

# ====================================================================
# 🧠 الواجهة الثانية: منصة المحادثة والشات القانوني (Chat Interface)
# ====================================================================
elif st.session_state.page == "chat":
    st.markdown('<p class="legal-logo" style="font-size: 3rem;">⚖️</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="main-title" style="font-size: 2.2rem;">LawMind | {st.session_state.country} Bureau</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="sub-title" style="font-size: 0.9rem; margin-bottom: 20px;">AI Legal Intelligence</p>', unsafe_allow_html=True)

    @st.cache_data
    def load_specific_country_law(country):
        possible_paths = [
            os.path.join(f"legal_{country}", "law.txt"),
            "law.txt"
        ]
        for path in possible_paths:
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    return f.read()
        return None

    legal_context = load_specific_country_law(st.session_state.country)

    # عرض سجل المحادثة
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(f'<div class="chat-bubble-user"><b>👤:</b> {message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div><b>⚖️ LawMind AI:</b></div>', unsafe_allow_html=True)
            st.code(message["content"], language="text")

    st.write(" ")
    user_query = st.text_input(label="Legal Consultation Input", placeholder=current_text["placeholder"], key="user_legal_input", label_visibility="collapsed")
    
    search_button = st.button(current_text["search_btn"], key="execute_consultation_btn")

    if search_button and user_query:
        if legal_context is None:
            st.error(f"❌ Document Error: Please create a file named 'law.txt' inside the folder 'legal_{st.session_state.country}'.")
        elif not GEMINI_API_KEY:
            st.error("⚠️ Gemini API Key is missing in Secrets.")
        else:
            st.session_state.chat_history.append({"role": "user", "content": user_query})
            with st.spinner("Analyzing Database..."):
                try:
                    # صياغة الاستدعاء التقليدي الصافي المتوافق تماماً مع النسخ القديمة والحديثة للمكتبة دون مسارات معقدة
                    system_prompt = (
                        f"You are a hyper-strict Legal AI Core named 'LawMind | AI Legal Intelligence' specialized in {st.session_state.country} laws.\n"
                        f"You must answer ONLY and STRICTLY from the provided legal context text below. If the case is not available, reply exactly with: "
                        f"'This specific case is not available in our verified database for {st.session_state.country}.'"
                    )
                    
                    user_message = f"SYSTEM INSTRUCTIONS:\n{system_prompt}\n\nVERIFIED LEGAL DATABASE:\n{legal_context[:30000]}\n\nCITIZEN QUESTION:\n{user_query}"
                    
                    # الالتفاف حول مشكلة الإصدار عبر استخدام دالة تشغيل بسيطة ومباشرة
                    response = genai.generate_text(
                        model='models/text-bison-001', # هذا الموديل كلاسيكي ومضمون العمل على نظام v1beta القديم المثبت عندك
                        prompt=user_message,
                        temperature=0.0
                    )
                    
                    st.session_state.chat_history.append({"role": "assistant", "content": response.text})
                    st.rerun()
                except Exception as e:
                    # محاولة ثانية بالنموذج الاحتياطي في حال تعذر الأول
                    try:
                        model = genai.GenerativeModel('gemini-pro')
                        response = model.generate_content(user_message)
                        st.session_state.chat_history.append({"role": "assistant", "content": response.text})
                        st.rerun()
                    except Exception as e2:
                        st.error(f"System Error: {str(e2)}")

st.markdown('<p class="footer-custom">LawMind | AI Legal Intelligence • Powered by Moroccan Innovation 🇲🇦 • © 2026</p>', unsafe_allow_html=True)
