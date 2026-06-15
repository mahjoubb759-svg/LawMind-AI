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

# سطر الـ Credits ثابت دائماً باللغة الإنجليزية
fixed_credits = "💡 Developed by: <span class='team-names'>Mr. Elmahjoub Boumagout</span> & <span class='team-names'>Mrs. ASMA AHLBIHI</span>"

locales = {
    "en": {
        "vision_native": "is the first Moroccan and global platform that harnesses artificial intelligence to serve humanity in the field of law.",
        "badge": "100% Moroccan Product 🇲🇦",
        "select_lang": "Select Language", "select_country": "Select Country", "btn_enter": "Launch Intelligence", "placeholder": "Ask your strict legal question here...", "search_btn": "Consult System"
    },
    "ar": {
        "vision_native": "هي أول منصة مغربية وعالمية تسخر الذكاء الاصطناعي لخدمة البشرية في مجال القانون.",
        "badge": "منتج مغربي 100% 🇲🇦",
        "select_lang": "حدد اللغة", "select_country": "حدد الدولة", "btn_enter": "إطلاق الذكاء القانوني", "placeholder": "اطرح سؤالك القانوني الصارم هنا...", "search_btn": "استشارة النظام"
    },
    "fr": {
        "vision_native": "est la première plateforme marocaine et mondiale qui met l'intelligence artificielle au service de l'humanité dans le domaine du droit.",
        "badge": "Produit 100% Marocain 🇲🇦",
        "select_lang": "Choisir la Langue", "select_country": "Choisir le Pays", "btn_enter": "Lancer l'Intelligence", "placeholder": "Posez votre question juridique stricte ici...", "search_btn": "Consulter le Système"
    }
}
current_text = locales[st.session_state.lang]

if st.session_state.page == "landing":
    st.markdown('<p class="legal-logo">⚖️</p>', unsafe_allow_html=True)
    st.markdown('<p class="main-title">LawMind</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">AI Legal Intelligence</p>', unsafe_allow_html=True)
    
    st.markdown(f'<div class="vision-container"><p class="vision-text"> <b>LawMind</b> {current_text["vision_native"]}</p></div>', unsafe_allow_html=True)
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

    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(f'<div class="chat-bubble-user"><b>👤 المستشار:</b><br>{message["content"]}</div>', unsafe_allow_html=True)
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
            with st.spinner("Analyzing Legal Database & Core Knowledge..."):
                try:
                    # 🛠️ التعديل الجوهري: تحويل محرك الـ AI إلى مستشار قانوني عالمي صارم يمنع الخروج عن الثيم القانوني لأي دولة
                    system_prompt = (
                        f"You are a strict, hyper-focused Legal Expert AI core specialized in national and international laws, currently advising on {st.session_state.country} laws. "
                        f"CRITICAL RULE 1 (THEME GATEKEEPER): You must ONLY answer legal and law-related questions. If the user's inquiry is NOT related to law, legislation, crimes, contracts, or judicial systems (e.g., general cooking, programming, gossip, pop culture, sports), you must strictly decline to answer. Politely state that you are an AI Legal Intelligence system and cannot step outside the boundaries of legal consultation. "
                        f"CRITICAL RULE 2 (GLOBAL SCOPE): While your current focus is set to {st.session_state.country} based on user selection, you possess comprehensive expertise in global jurisdictions. Answer inquiries with high-quality formal legal analysis. "
                        f"CRITICAL RULE 3 (LANGUAGE MATCHING): You must write your professional response in the EXACT SAME LANGUAGE the user used to ask the question. If they ask in Arabic, reply in formal, eloquent legal Arabic."
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
                            {"role": "user", "content": f"PROVIDED DATA CONTEXT (IF APPLICABLE):\n{legal_context[:30000]}\n\nUSER LEGAL INQUIRY:\n{user_query}"}
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
