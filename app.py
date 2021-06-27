from altair.vegalite.v4.api import value
import streamlit as st
from pytube import YouTube
import qr_maker

st.set_page_config(page_title="金融科技專題 - 自動生成摘要與總結", page_icon=':smiley:',  # ':crescent-​moon:'
                    layout='centered', initial_sidebar_state="auto")#"collapsed")

st.title("金融科技專題:文本生成-市場焦點機器人")

yt_url= {'南山人壽-第1組-3分鐘-廣告.市場焦點機器人':['https://youtu.be/7xnzMr0B3b8'],
         '南山人壽-第1組-15分鐘-介紹.市場焦點機器人':['https://youtu.be/Is2hGoqxx3k'],
         '南山人壽-第2組-3分鐘-廣告.市場焦點機器人':['https://youtu.be/4i5B8hfvl6w'],
         '南山人壽-第2組-15分鐘介紹.市場焦點機器人':['https://youtu.be/gW8CkxQubj4'],
         '南山人壽-第3組-3分鐘-廣告.市場焦點機器人':['https://youtu.be/lDfDV1I2Pr4'],
         '南山人壽-第3組-15分鐘介紹.市場焦點機器人':['https://youtu.be/OBavep3gY_E'],
         '南山人壽-第4組-3分鐘-廣告.市場焦點機器人':['https://www.youtube.com/watch?v=sia8o_xN8ag'],
         '南山人壽-第4組-15分鐘介紹.市場焦點機器人':['https://www.youtube.com/watch?v=YFBpGaHVnz8'],
         '南山人壽-優勝組-3分鐘-廣告.運用機器學習於業務員風險偵測':['https://youtu.be/Kf7v187uUrA'],
         '南山人壽-優勝組-15分鐘介紹.運用機器學習於業務員風險偵測':['https://youtu.be/pt1ZoWrdNFw'],

         '國泰人壽-優勝組-3分鐘-廣告.人臉辨識技術-吸菸者':['https://youtu.be/aZO6bzMm__A'],
         '國泰人壽-優勝組-15分鐘介紹.人臉辨識技術-吸菸者':['https://youtu.be/w_4QGtyS2Ss'],
         '國泰人壽-優勝2組-3分鐘-廣告.Cathay Walker Plus企業版推動案':['https://youtu.be/vwwnVrAw6IU'],
         '國泰人壽-優勝2組-15分鐘介紹.Cathay Walker Plus企業版推動案':['https://youtu.be/E_mx8QvpIfk'],

         '玉山證券-優勝組-3分鐘-廣告.個人投資風險管家':['https://youtu.be/2FRqw1uEiac'],
         '玉山證券-優勝組-15分鐘介紹.個人投資風險管家':['https://youtu.be/iqn2AxEXt50'],
         '永豐金控-優勝組-3分鐘-廣告.AI挑選最佳基金':['https://youtu.be/GyuDfw4FKzg'],
         '永豐金控-優勝組-15分鐘介紹.AI挑選最佳基金':['https://youtu.be/9TEgCBaxdiM'],
         '台灣人壽-優勝組-3分鐘-廣告.花甲不孤單':['https://youtu.be/DYNIMNFeyUw'],
         '台灣人壽-優勝組-15分鐘介紹.花甲不孤單':['https://youtu.be/OSfNkZ1p7QU'],
         '安侯建業-優勝組-3分鐘-廣告.建立舞弊風險指標預警機制':['https://youtu.be/BNk6Kz-TD7I'],
         '安侯建業-優勝組-15分鐘介紹.建立舞弊風險指標預警機制':['https://youtu.be/J38fAyPl9vs'],
         '安侯建業-優勝2組-3分鐘-廣告.汽車保險創新模式行程保單':['https://youtu.be/z8i3ryjgN9k'],
         '安侯建業-優勝2組-15分鐘介紹.汽車保險創新模式行程保單':['https://youtu.be/eQxMPDXraso'],
         
         '野村投信-優勝組-3分鐘-廣告.理財機器人NomuraBot':['https://youtu.be/1XrKLYqYK-8'],
         '野村投信-優勝組-15分鐘介紹.理財機器人NomuraBot':['https://youtu.be/dCHV_nD3tlI'],
         '野村投信-優勝2組-3分鐘-廣告.網頁視覺化熱門字組分析':['https://youtu.be/jGYMHPYvXVA'],
         '野村投信-優勝2組-15分鐘介紹.網頁視覺化熱門字組分析':['https://youtu.be/m3-hq_hJMw8']
         }

titles, urls = yt_url.keys(), yt_url.values()
with st.sidebar.beta_container():
    st.image('images/NanShan_Logo.png', width=256)
    st.markdown('''<h1 style="float: left;">南山人壽.投資-台大-東吳</h>''', unsafe_allow_html=True)
    st.write('Mentor: Jack & Taylor')
    
    title = st.selectbox('請選擇-各組專題成果影片: ', list(titles), 0)
    url = yt_url[title][0]

    qr_size = 5 #st.slider('Slide me', min_value = 6, max_value = 12, value = 6)
    qr_name = qr_maker.qr_code(link=f"{url}", logo=False,  size=qr_size)
    st.image(qr_name, caption=f'{title} - Youtube')

    hyper_link = 'https://fintech2021-inv.herokuapp.com/'
    qr_name = qr_maker.qr_code(link=f"{hyper_link}", logo=False,  size=qr_size)
    st.image(qr_name, caption=f"{hyper_link}")


if url != '':
    yt = YouTube(url)

    st.markdown(f'<h3 style="float: left;">{yt.title}</h3><a href="{url}" TARGET="_blank"><img style="float: right;" src="{yt.thumbnail_url}" width="700"/></a>', unsafe_allow_html=True)

    st.subheader('''Length: {:.2f} Minutes  ||   Rating: {} '''.format(yt.length/60.0 , yt.rating))
    video = yt.streams

    values = ['lowest','highest',"720p", "480p", "360p", "240p", "144p"]
    default_ix = values.index('highest')

    with st.sidebar.beta_container():
        resolution_level = st.selectbox('Resolution Level ?', values, index=default_ix)

    if len(video) > 0:
        downloaded , download_audio = False , False
        download_video = st.button("Download Video",)
        if yt.streams.filter(only_audio=True):
            with st.sidebar.beta_container():
                download_audio = st.button("Download Audio Only")
        if download_video:
            #resolution_level = st.selectbox('resolution level ?', ['lowest','highest'])
            if resolution_level == 'lowest':
                video.get_lowest_resolution().download()
            else:
                if resolution_level == 'highest':
                    video.get_highest_resolution().download()
                else:
                    resolutions=["720p", "480p", "360p", "240p", "144p"]
                    video.get_by_resolution(resolutions[0]).download()

            downloaded = True
        if download_audio:
            #yt_file = f'{title}.mp3'
            #yt_file =st.text_input('Download the audio to :',yt_file)
            video.filter(only_audio=True).first().download()
            downloaded = True
        if downloaded:
            st.subheader("Download Complete")
    else:
        st.subheader("Sorry, this video can not be downloaded")
        