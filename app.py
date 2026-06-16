import streamlit as st
import requests
import json
import os

# 1. إعدادات الصفحة الأساسية بالمظهر العريض الاحترافي
st.set_page_config(page_title="LawMind | AI Legal Intelligence", page_icon="⚖️", layout="wide")

# 2. تصميم الـ Frontend الاحترافي المطور والمقاوم لتداخل النصوص
st.markdown("""
    <style>
    /* إخفاء القائمة الجانبية بالكامل وأدوات المنصة الافتراضية */
    [data-testid="stSidebar"], [data-testid="stSidebarCollapseButton"] {
        display: none !important;
    }
    #MainMenu, footer, header, [data-testid="stDecoration"] {
        visibility: hidden !important;
        display: none !important;
    }
    .viewerBadge_container__1QSob, [data-testid="stViewerBadge"], .styles_viewerBadge__NiTeF, div[class^="viewerBadge"] {
        display: none !important;
        visibility: hidden !important;
    }
    
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
        max-width: 1000px !important;
        margin: 0 auto !important;
    }

    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
    }
    
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
    
    .badge-container {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        margin-top: 10px;
        margin-bottom: 35px;
        clear: both;
    }
    
    .moroccan-badge {
        text-align: center !important;
        color: #065F46 !important;
        font-size: 0.95rem;
        font-weight: bold;
        background-color: #D1FAE5;
        padding: 8px 24px;
        border-radius: 50px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        display: inline-block;
        white-space: nowrap;
        unicode-bidi: plaintext !important;
    }
    
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
    
    .chat-bubble-user {
        background-color: #1e293b;
        padding: 15px 20px;
        border-radius: 20px 20px 0px 20px;
        margin-bottom: 20px;
        border: 1px solid rgba(56, 189, 248, 0.2);
        max-width: 85%;
        margin-left: auto;
        font-size: 1.1rem;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    .chat-bubble-ai {
        background-color: #0f172a;
        padding: 22px;
        border-radius: 20px 20px 20px 0px;
        margin-bottom: 20px;
        border: 1px solid rgba(129, 140, 248, 0.3);
        max-width: 85%;
        font-size: 1.1rem;
        line-height: 1.8;
        color: #f1f5f9;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
    }
    .ai-header {
        color: #818cf8;
        font-weight: bold;
        margin-bottom: 8px;
    }
    .footer-custom {
        text-align: center;
        margin-top: 50px;
        color: #64748b;
        font-size: 0.85rem;
    }
    </style>
""", unsafe_allow_html=True)

if "page" not in st.session_state: st.session_state.page = "landing"
if "lang" not in st.session_state: st.session_state.lang = "ar"
if "country" not in st.session_state: st.session_state.country = "Morocco"
if "chat_history" not in st.session_state: st.session_state.chat_history = []

# 🔐 قراءة مفتاح OpenAI بأمان
OPENAI_API_KEY = ""
if "openai" in st.secrets:
    OPENAI_API_KEY = st.secrets["openai"]["api_key"].strip()

# اللقب التكريمي لـ "أسماء" ليعكس الاحترافية والوضع الاجتماعي الصحيح Ms.
fixed_credits = "💡 Developed by: <span class='team-names'>Mr. Elmahjoub Boumagout</span> & <span class='team-names'>Ms. ASMA AHLBIHI</span>"

# نصوص الرؤية واللغات المتعددة مع إضافة مفتاح "user_label" المترجم ديناميكياً
locales = {
    "en": {
        "vision_html": "<b>LawMind</b> is the first Moroccan platform that harnesses artificial intelligence to serve humanity in the field of legal consultations.",
        "badge": "100% Moroccan Product 🇲🇦",
        "select_lang": "Select Language", "select_country": "Select Country Office", "btn_enter": "Launch Intelligence", "placeholder": "Ask your strict legal question here...", "search_btn": "Consult System",
        "user_label": "Me"
    },
    "ar": {
        "vision_html": "هي اول منصة مغربية تسخر الذكاء الاصطناعي لخدمة البشرية في مجال الاستشارات القانونية.",
        "badge": "منتج مغربي 100% 🇲🇦",
        "select_lang": "حدد اللغة", "select_country": "حدد مكتب الدولة", "btn_enter": "إطلاق الذكاء القانوني", "placeholder": "اطرح سؤالك القانوني الصارم هنا...", "search_btn": "استشارة النظام",
        "user_label": "أنا"
    },
    "fr": {
        "vision_html": "<b>LawMind</b> est la première plateforme marocaine qui met l'intelligence artificielle au service de l'humanité dans le domaine des consultations juridiques.",
        "badge": "Produit 100% Marocain 🇲🇦",
        "select_lang": "Choisir la Langue", "select_country": "Choisir le Bureau de Pays", "btn_enter": "Lancer l'Intelligence", "placeholder": "Posez votre question juridique stricte ici...", "search_btn": "Consulter le Système",
        "user_label": "Moi"
    },
    "es": {
        "vision_html": "<b>LawMind</b> es la primera plataforma marroquí que pone la inteligencia artificial al servicio de la humanidad en el campo de las consultas jurídicas.",
        "badge": "Producto 100% Marroquí 🇲🇦",
        "select_lang": "Seleccionar Idioma", "select_country": "Seleccionar Oficina de País", "btn_enter": "Iniciar Inteligencia", "placeholder": "Haga su pregunta legal estricta aquí...", "search_btn": "Consultar Sistema",
        "user_label": "Yo"
    },
    "de": {
        "vision_html": "<b>LawMind</b> ist die erste marokkanische Plattform, die künstliche Intelligenz im Dienste der Menschheit im Bereich der Rechtsberatung einsetzt.",
        "badge": "100% Marokkanisches Produkt 🇲🇦",
        "select_lang": "Sprache auswählen", "select_country": "Länderbüro auswählen", "btn_enter": "Intelligenz starten", "placeholder": "Stellen Sie hier Ihre strenge Rechtsfrage...", "search_btn": "System konsultieren",
        "user_label": "Ich"
    }
}
current_text = locales[st.session_state.lang]

supported_countries = ["Morocco 🇲🇦", "France 🇫🇷", "USA 🇺🇸", "Saudi Arabia 🇸🇦", "Egypt 🇪🇬", "Spain 🇪🇸", "UAE 🇦🇪"]

if st.session_state.page == "landing":
    st.markdown('<p class="legal-logo">⚖️</p>', unsafe_allow_html=True)
    st.markdown('<p class="main-title">LawMind</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">AI Legal Intelligence</p>', unsafe_allow_html=True)
    
    st.markdown(f'<div class="vision-container"><p class="vision-text">{current_text["vision_html"]}</p></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="badge-container"><span class="moroccan-badge">{current_text["badge"]}</span></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<div class="selection-box"><h3>🌐 {current_text["select_lang"]}</h3>', unsafe_allow_html=True)
        selected_lang_ui = st.selectbox("Language", ["العربية", "English", "Français", "Español", "Deutsch"], index=["ar", "en", "fr", "es", "de"].index(st.session_state.lang), label_visibility="collapsed")
        if selected_lang_ui == "English": st.session_state.lang = "en"
        elif selected_lang_ui == "العربية": st.session_state.lang = "ar"
        elif selected_lang_ui == "Français": st.session_state.lang = "fr"
        elif selected_lang_ui == "Español": st.session_state.lang = "es"
        elif selected_lang_ui == "Deutsch": st.session_state.lang = "de"
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown(f'<div class="selection-box"><h3>📍 {current_text["select_country"]}</h3>', unsafe_allow_html=True)
        clean_country_names = [c.split()[0] for c in supported_countries]
        default_country_idx = clean_country_names.index(st.session_state.country) if st.session_state.country in clean_country_names else 0
        
        selected_country_ui = st.selectbox("Country", supported_countries, index=default_country_idx, label_visibility="collapsed")
        st.session_state.country = selected_country_ui.split()[0]
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.write(" ")
    if st.button(current_text["btn_enter"]):
        st.session_state.page = "chat"
        st.rerun()
            
    st.markdown(f'<div class="credits-container"><div class="team-credits">{fixed_credits}</div></div>', unsafe_allow_html=True)

elif st.session_state.page == "chat":
    st.markdown('<p class="legal-logo" style="font-size: 3rem;">⚖️</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="main-title" style="font-size: 2.2rem;">LawMind | {st.session_state.country} Bureau</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="sub-title" style="font-size: 0.9rem; margin-bottom: 20px;">AI Legal Intelligence</p>', unsafe_allow_html=True)

    @st.cache_data
    def load_specific_country_law():
        if os.path.exists("law.txt"):
            try:
                with open("law.txt", "r", encoding="utf-8-sig") as f: return f.read()
            except:
                with open("law.txt", "r", encoding="utf-8", errors="ignore") as f: return f.read()
        return ""

    legal_context = load_specific_country_law()

    # عرض غرف المحادثة السابقة بشكل متناسق مع اللغة المختارة
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            # 🛠️ دمج المتغير الديناميكي هنا لقراءة اللفظ الصحيح لكلمة (أنا/Me/Moi...) طبقاً للغة الواجهة
            st.markdown(f'<div class="chat-bubble-user"><b>👤 {current_text["user_label"]}:</b><br>{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-bubble-ai"><div class="ai-header">⚖️ LawMind AI Intelligence:</div>{message["content"]}</div>', unsafe_allow_html=True)

    st.write(" ")
    with st.form(key="legal_form", clear_on_submit=True):
        user_query = st.text_input(label="Legal Consultation Input", placeholder=current_text["placeholder"], label_visibility="collapsed")
        search_button = st.form_submit_button(current_text["search_btn"])

    if search_button and user_query:
        if not OPENAI_API_KEY:
            st.error("⚠️ Configuration Error: OpenAI API Key is missing.")
        else:
            st.session_state.chat_history.append({"role": "user", "content": user_query})
            with st.spinner("Analyzing Legal Database & Universal Law Knowledge..."):
                try:
                    system_prompt = (
                        f"You are a strict, hyper-focused Legal Expert AI core specialized in international jurisprudence. "
                        f"Your default focus for this session is set to {st.session_state.country} laws. "
                        f"CRITICAL RULE 1 (DYNAMIC JURISDICTION): Analyze the user's question. If the user explicitly asks about the laws of another specific country (e.g., they are in the Morocco bureau but ask about France, USA, Egypt, etc.), you MUST override the default country and answer accurately according to the legal system of the country requested in their question. "
                        f"If they do not specify another country, answer strictly based on {st.session_state.country} laws, using the priority text database below if relevant information exists."
                        f"CRITICAL RULE 2 (THEME GATEKEEPER): You must ONLY answer legal and law-related questions. If the inquiry is outside the boundaries of law (e.g. cooking, programming, pop culture), politely decline to answer, stating that you are a dedicated AI Legal Intelligence system. "
                        f"CRITICAL RULE 3 (LANGUAGE MATCHING): You must write your professional response in the EXACT SAME LANGUAGE the user used to ask the question. If they ask in Arabic, reply in formal legal Arabic."
                    )
                    
                    api_url = "https://api.openai.com/v1/chat/completions"
                    headers = {
                        "Authorization": f"Bearer {OPENAI_API_KEY}",
                        "Content-Type": "application/json"
                    }
                    
                    payload = {
                        "model": "gpt-4o-mini",
                        "messages": [
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": f"PROVIDED DATA CONTEXT FOR {st.session_state.country} (PRIORITY IF APPLICABLE):\n{legal_context[:30000]}\n\nUSER LEGAL INQUIRY:\n{user_query}"}
                        ],
                        "temperature": 0.2
                    }
                    
                    response = requests.post(api_url, headers=headers, json=payload)
                    response_json = response.json()
                    
                    if 'choices' in response_json and response_json['choices']:
                        output_text = response_json['choices'][0]['message']['content']
                        st.session_state.chat_history.append({"role": "assistant", "content": output_text})
                        st.rerun()
                    elif 'error' in response_json:
                        st.error(f"🛑 OpenAI API Error: {response_json['error'].get('message')}")
                    else:
                        st.error(f"⚠️ Unexpected Server Response.")
                        
                except Exception as e:
                    st.error(f"System Error: {str(e)}")

st.markdown('<p class="footer-custom">LawMind | AI Legal Intelligence • Powered by Moroccan Innovation 🇲🇦 • © 2026</p>', unsafe_allow_html=True)
