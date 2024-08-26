import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from datetime import datetime, timedelta

st.set_page_config(
    page_title="더 나은 내일을 위해, 오늘 당신의 문 앞으로 - 클링픽업",
    page_icon = "./images/image.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

image_url = "https://github.com/ASAcoss/llooggoo/blob/main/%ED%81%B4%EB%A7%81%ED%94%BD%EC%97%85_%EB%A1%9C%EA%B3%A0-removebg-preview.png?raw=true"

response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

image.save("./images/image.png")

# CSS 스타일 직접 정의
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@900&display=swap'); /* Poppins 폰트 임포트 */

    .stApp {
        background-image: url("https://images.unsplash.com/photo-1549490345-9f5fd7e6a2af?ixlib=rb-4.0.3&auto=format&fit=crop&w=1950&q=80");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: center;
        opacity: 0.9; /* 글씨를 가리지 않도록 반투명하게 설정 */
    }

    .banner {
        background-color: #2E7D32; /* CLING PICK-UP 글자 색상과 동일하게 배경색 설정 */
        color: white; /* 글씨 색상 */
        font-size: 28px; /* 글씨 크기 */
        padding: 15px 0; /* 배너 패딩 */
        text-align: center; /* 가운데 정렬 */
        font-weight: bold;
        font-family: 'Poppins', sans-serif; /* 세련된 폰트 적용 */
        border-radius: 15px; /* 배너의 모서리를 둥글게 */
        margin-top: 20px; /* 페이지 상단에서의 간격 */
        box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.15); /* 더 강한 그림자 추가 */
        position: relative;
    }
            
    .login-link {
        position: absolute;
        top: 50%;
        right: 20px;
        transform: translateY(-50%);
        font-size: 16px;
        color: green; /* 글씨 색상 초록색으로 설정 */
        background-color: white; /* 버튼 배경 흰색 */
        padding: 8px 16px;
        text-decoration: none;
        border-radius: 20px; /* 둥근 모서리 */
        font-weight: bold;
        font-family: 'Poppins', sans-serif;
        border: 2px solid #2E7D32; /* 초록색 테두리 */
        transition: background-color 0.3s ease, color 0.3s ease, transform 0.3s ease; /* 부드러운 전환 효과 */
    }

    .main-header {
        color: #2E7D32;
        font-family: 'Poppins', sans-serif; /* 동글동글한 글씨체 */
        font-size: 80px; /* 텍스트 크기 최대 설정 */
        font-weight: 900; /* 폰트 굵기 최대 */
        margin-top: 40px; /* 배너 아래쪽에 공간을 추가하기 위해 마진 설정 */
        text-align: center; /* 텍스트 중앙 정렬 */
    }

    .sub-header {
        font-size: 18px;
        color: #388E3C;
        margin-top: -10px;
    }

    .streamlit-expanderHeader {
        font-size: 1.2rem;
        font-weight: bold;
        color: #4CAF50;
        background-color: #E8F5E9;
        border-radius: 8px;
        padding: 10px;
        border: 2px solid #4CAF50;
    }

    .streamlit-expander {
        margin-bottom: 15px;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        background-color: rgba(255, 255, 255, 0.85); /* expander를 살짝 투명하게 설정 */
    }

    .emoji-container {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-left: 40px; /* 이모티콘을 오른쪽으로 이동 */
        font-size: 50px; /* 이모티콘 크기 증가 */
        margin-top: 20px; /* 이모티콘을 조금 더 아래로 이동 */
    }
    </style>
""", unsafe_allow_html=True)

# 상단 현수막 추가 (글자 간격 조정 및 로그인 버튼 추가)
st.markdown("""
    <div class='banner'>
        더 나은 내일을 위해, 오늘 당신의 문 앞으로
        <a href='#' class='login-link'>로그인</a>
    </div>
    """, unsafe_allow_html=True)

# 상단 로고 및 제목
st.markdown("""
    <h1 class='main-header'>
        CLING PICK-UP♻️
    </h1>
""", unsafe_allow_html=True)


# 세션 상태를 이용해 활성화된 탭을 추적
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = '수거 품목'

if 'next_clicked' not in st.session_state:
    st.session_state.next_clicked = False

# 탭 구성
tabs = st.tabs(["수거 요청","마이 페이지", "수거 가능한 품목"])

# 현재 활성화된 탭에 맞춰서 렌더링
with tabs[0]:
    if st.session_state.active_tab == '수거 품목':
        st.header("수거 품목")

        if 'cart' not in st.session_state:
            st.session_state.cart = []
        if 'total_price' not in st.session_state:
            st.session_state.total_price = 0.0
        if 'price_tracker' not in st.session_state:
            st.session_state.price_tracker = {}

        price = {
            "종이류": 1000.0,  # 1kg당 1000.0원
            "병류": 1000.0,     # 1kg당 1000.0원
            "고철류": 1000.0,   # 1kg당 1000.0원
            "캔류": 1000.0,     # 1kg당 1000.0원
            "비닐류": 1000.0,   # 1kg당 1000.0원
            "스티로폼류": 1000.0, # 1kg당 1000.0원
            "플라스틱류": 1000.0, # 1kg당 1000.0원
            "의류": 1000.0    # 1kg당 1000.0원
        }

        def add_to_cart(item_name, weight_key, price_per_kg, button_key):
            weight = st.number_input(f"{item_name} 무게 입력 (kg)", min_value=0.0, step=0.1, key=weight_key)
            if st.button(f"추가하기", key=button_key):
                if weight > 0:
                    weight = round(weight,2)
                    price = weight * price_per_kg
                    st.session_state.cart = [item for item in st.session_state.cart if not item.startswith(item_name)]
                    st.session_state.cart.append(f"{item_name}: {weight} kg          + {price} 원")
                    if item_name in st.session_state.price_tracker:
                        st.session_state.total_price -= st.session_state.price_tracker[item_name]  # 기존 가격 제거
                    st.session_state.total_price += price
                    st.session_state.price_tracker[item_name] = price

        # 첫 번째 열
        col1, col2 = st.columns(2)
        with col1:
            with st.expander("**종이류**"):
                st.write("종이 1kg 당 1,000원")
                add_to_cart("종이류", "paper_weight", price["종이류"], "add_paper")

        with col2:
            with st.expander("**플라스틱류**"):
                st.write("플라스틱 1kg 당 1,000원")
                add_to_cart("플라스틱류", "plastic_weight", price["플라스틱류"], "add_plastic")

        # 두 번째 열
        col3, col4 = st.columns(2)
        with col3:
            with st.expander("**비닐류**"):
                st.write("비닐 1kg 당 1,000원")
                add_to_cart("비닐류", "vinyl_weight", price["비닐류"], "add_vinyl")

        with col4:
            with st.expander("**캔류**"):
                st.write("캔 1kg 당 1,000원")
                add_to_cart("캔류", "can_weight", price["캔류"], "add_can")

        # 세 번째 열
        col5, col6 = st.columns(2)
        with col5:
            with st.expander("**병류**"):
                st.write("병 1kg 당 1,000원")
                add_to_cart("병류", "bottle_weight", price["병류"], "add_bottle")

        with col6:
            with st.expander("**스티로폼류**"):
                st.write("스티로폼 1kg 당 1,000원")
                add_to_cart("스티로폼류", "styrofoam_weight", price["스티로폼류"], "add_styrofoam")

        # 네 번째 열
        col7, col8 = st.columns(2)
        with col7:
            with st.expander("**고철류**"):
                st.write("고철 1kg 당 1,000원")
                add_to_cart("고철류", "metal_weight", price["고철류"], "add_metal")

        with col8:
            with st.expander("**의류**"):
                st.write("의류 1kg 당 1,000원")
                add_to_cart("의류", "clothes_weight", price["의류"], "add_clothes")

        # 장바구니 표시
        st.divider()
        with st.expander("**나의 장바구니🛒**", expanded=True):
            st.write("**장바구니에 담긴 품목**")
            if st.session_state.cart:
                for item in st.session_state.cart:
                    st.write(f"- {item}")
                st.write(f"**총 환급액: {st.session_state.total_price:.2f} 원**")
            else:
                st.write("장바구니가 비어 있습니다.")

        if not st.session_state.next_clicked:
            if st.button("Next"):
                st.session_state.next_clicked = True

        else:
            st.divider()
            address = st.text_input("쓰레기 수거 주소:")

            today = datetime.now().date()
            min_pickup_date = today + timedelta(days=2)

            pickup_date = st.date_input(
                "수거 희망 날짜를 선택하세요:",
                min_value=min_pickup_date,
                value=min_pickup_date
            )
            request = st.text_input("요청사항")

            if st.session_state.cart and address and pickup_date:
                if st.button("수거 요청하기"):
                    st.success("수거 요청이 완료되었습니다!")
            
            else:
                st.warning("주소와 날짜를 입력해주세요.")


with tabs[1]:
    st.subheader("마이 페이지")
    st.markdown("""
    <style>
    .profile-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 20px;
    }

    .profile-pic {
        width: 300px;
        height: 300px;
        border-radius: 50%;
        background-color: #f0f0f0;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 100px;
        color: #a0a0a0;
    }

    .earnings-box {
        background-color: #e0f7df;
        border: 2px solid #34c759;
        border-radius: 10px;
        width: 400px; /* 정사각형 모양을 위해 폭과 높이를 동일하게 설정 */
        height: 300px; /* 높이를 더 늘려서 정사각형처럼 보이도록 설정 */
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        margin-left: 20px;
        margin-top: 20px;
    }

    .earnings-title {
        font-size: 24px;
        font-weight: bold;
        color: black;
        text-align : left;
        margin-bottom: 10px;
    }

    .earnings-box .points {
        font-size: 70px;
        font-weight: bold;
        color: #34c759;
    }

    .earnings-box .label {
        font-size: 30px;
        color: #34c759;
        font-weight: normal;
    }

    .profile-name {
        font-size: 24px;
        font-weight: bold;
        margin-top: 10px;
    }

    .profile-email {
        font-size: 16px;
        color: #888;
        margin-bottom: 20px;
    }

    .notification {
        background-color: #e6f4ea;
        border: 1px solid #34c759;
        padding: 10px;
        border-radius: 10px;
        font-size: 14px;
        color: #34c759;
        margin-bottom: 20px;
        text-align: center;
    }

    .section-title {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 10px;
        color: #444;
    }

    .info-box {
        background-color: #f7f7f7;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        border: 1px solid #ddd;
    }

    .info-label {
        font-size: 14px;
        color: #666;
    }

    .info-value {
        font-size: 16px;
        font-weight: bold;
    }

    </style>
    """, unsafe_allow_html=True)

    # 프로필 섹션
    st.markdown("<div class='profile-container'>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("<div class='profile-pic'>🧑</div>", unsafe_allow_html=True)  # 기본 프로필 사진 대체

    with col2:
        st.markdown("""
        <div class='earnings-title'>나의 누적 수익</div>
        <div class='earnings-box'>
            <span class='points'>2,400</span>
            <span class='label'>점</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='profile-name'>웃음코드</div>", unsafe_allow_html=True)
    st.markdown("<div class='profile-email'>oasis_hackaton@naver.com</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # 알림 박스
    st.markdown("<div class='notification'>[알림] 축하드려요!! 저번달보다 1,000원 더 벌었어요!</div>", unsafe_allow_html=True)

    # 내 프로필 섹션
    st.markdown("<div class='section-title'>내 프로필</div>", unsafe_allow_html=True)
    st.markdown("<div class='info-box'><span class='info-label'>이름:</span> <span class='info-value'>웃음코드</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='info-box'><span class='info-label'>전화번호:</span> <span class='info-value'>+82 10-1***-5***</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='info-box'><span class='info-label'>저장된 주소:</span> <span class='info-value'>광주광역시 동구 라마다 호텔 아주 좋네요 굿:)</span></div>", unsafe_allow_html=True)

    # 보안 설정 섹션
    st.markdown("<div class='section-title'>내 쿠폰함</div>", unsafe_allow_html=True)
    with st.expander("사용 가능한 쿠폰"):
        st.write("-환급액 10% 추가")

with tabs[2]:
    stuffs = [
        {
            "name" : "종이류",
            "types" : "신문지, 책, 종이상자류, 달력, 포장지, 우유팩 등",
            "image_url" : "https://i.namu.wiki/i/oWuh4wWXuVEkkv6lisNqNmgi25-xTwlDfemXU6Dy7_Anm1661QsQ1N849Sr7onuGrbaPgCPhj9jsfGAgZO65nPYt7REcDxPGTXnHTGrVmNRRxlvg6ILu4F9cuzi0GC47OqnXxeIbx5VWm-_QEQ2yuw.webp"
        },
        {
            "name" : "플라스틱류",
            "types" : "PET, PE, PP, PS, PSP 재질의 용기 포장재 등",
            "image_url" : "https://i.namu.wiki/i/fYWWlw7G45k10-CL5aj9x92s4APEIOAr8g4VJELedsPtC6UAwIzhRvBv8UKxMHppCFX0MkhkplnHHfJxhGYrf5B9-um9hp0RWAOhWhdNZJKTjnoXN6rdT3ApHFXmmtV1ahxHYgY-4QgCvUsbiTOgkQ.webp"
        },
        {
            "name" : "비닐류",
            "types" : "비닐봉투, 과자&라면봉지, 위생팩",
            "image_url" : "https://i.namu.wiki/i/FwuAwX2i2KGb5tKH3dsqnpHbn4gdrAcy9ObK9RYRDw7faRvgd5Jc13iYtdVCKx4lDwElXLgeZnEMVNnJbo294vmf-pzcRpTr0rZRD9OBFb5A_vAU2Wo4XAZvJFLIA9yXQ-p5sy84MbHSyIS1ysYh9A.webp"
        },
        {
            "name" : "캔류",
            "types" : "음료캔, 식료용캔, 방충용캔, 부탄가스용기 등",
            "image_url" : "https://i.namu.wiki/i/4tDZnZcrQewv8pqHBam1OpnTSq-LiNpU4sASAmeokzFUeLTUbdnrI8EysY8x2LIM9HMqf2ZCyaq-IfIADxoI8kZPynjTlnuXyMrWHw7NK61M26WbKNFQ1QL-w28uD4WaiBzUgc40NjXCgVur1t3OeQ.webp"
        },
        {
            "name" : "병류",
            "types" : "음료수병, 술병, 형광등 등",
            "image_url" : "https://i.namu.wiki/i/lPObCeQ6dxDhxpYjvgqmwrNal9UGSeG9KG4rjuWIMbs-grcmhiP8jL3_T8WBaOgutMRTJa0SoTwqtU0a-o-5dVSKFbhoSBGSunpKMb3BW6sMANgf0HYB4ijTWh-RS2BkkHwX1ypRjljnF3Ab70Ybwg.webp"
        },
        {
            "name" : "스티로폼류",
            "types" : "스티커나 테이프가 제거된 스티로폼 포장용기(흰색)",
            "image_url" : "https://i.namu.wiki/i/n3VvCVl4MwNUUx7amxF6dqr8psw7-bSLqhjd7_P2Gw3JgVEiSCLB1AISOq15X6ZEO0N32r-I2eEkPzvoiu8DkZJmioVWlCNJZJFZA1oeFveC96YjA09kgTXT8N-ntoOSMTozx2BDiTobOHSdIL_baQ.webp"
        },
        {
            "name" : "고철류",
            "types" : "공구, 철사, 양은, 알루미늄, 스텐, 구리 등 \n 고무나 플라스틱이 합성되어 있는 제품은 불가",
            "image_url" : "https://i.namu.wiki/i/sazmMbNdzuJNyf8aQFTSenFfB5WI-CLmpCrSdRmkOIeoDNTriL_7mwi0wMk2rtW-kCArYaL_Lao8uUPOJMxO09py_VOOWP54WvulZ1eaPijIDetuJWoNkLolJZesiuFHyn5i-xQHxmVegTJNKkRTIw.webp"
        },
        {
            "name" : "의류",
            "types" : "헌옷(투명 비닐에 담아 배출) \n 솜이불류는 불가",
            "image_url" : "https://i.namu.wiki/i/syzjtWws2iU24kwR6lm44n_1N6vK4KvyY_NwOCQnDoPCPq2_EZtQa0Oce6epM-uAY7z7rSE_jCc2M8t5atMK54vKzQOb6GKrBN9Hmd04256IMaDAvgbS8SoymMufhaGOIQgQPQcR7xnOhdYsSgOXeQ.webp"
        }
    ]

    cols = st.columns(4)
    for i in range(0, len(stuffs), 4):
        row_stuffs = stuffs[i:i+4]
        cols = st.columns(4)
        for j in range(len(row_stuffs)):
            with cols[j]:
                stuff = row_stuffs[j]
                with st.expander(label=f"**{stuff['name']}**", expanded = True):
                    st.image(stuff["image_url"])
                    st.write(stuff["types"])
