from altair.vegalite.v4.api import value
import streamlit as st
from pytube import YouTube
import qr_maker

st.set_page_config(page_title="金融科技專題 - 自動生成摘要與總結", page_icon=':smiley:',  # ':crescent-​moon:'
                    layout='centered', initial_sidebar_state="auto")#"collapsed")

st.title("金融科技專題:文本生成-市場焦點機器人")

with st.beta_expander('本題, 有四組隊伍(18人)實作【文字探勘】的應用。總結,各組表現評語:',expanded=False):
    with st.beta_container():
        st.info('題目設有__三定錨__, 分別是: ①新聞爬蟲、②文章摘要、③生成簡報。分組討論-特色發展。')
        st.write('__突發事件新聞__考驗決策者，需有效率地__縮短決策時間__。自動收集社群新聞、__精簡摘要__、匯整數據圖表、製作報告__過程自動化__,就很重要。__化繁為簡__提升__專注__才有**執行力**。__自動化__可**減少勞力**。')
        st.info('【第一組】引用先進的__生成摘要__模型(BART)、視覺化__市場情緒__、匯整金融__數據圖表__、**自動化**報告生成。建構較為__完整__、__實用__(如, 研究員晨報、商情報告、金融監理態度...)。')

        st.write('但這還不夠, 新聞是否被__主力__置入了__偏見__?')
        st.info('【第二組】發展了__無偏見新聞__的處理。還有, 應用__情緒計算__在分析__ESG__的議題。')

        st.write('在無特定方向中找潛力方向？決策者最想預知__那些是具潛力發展的議題__，值得持續關注。')
        st.info('【第三組】先用Google Trend找出__群眾熱搜趨勢__、挖掘**潛在議題**、輔助決策-__超前佈署__。')

        st.info('【第四組】從__公司__新聞角度, 計算__新聞情緒__與__股價__進行比對分析。')
        st.write('綜合這四組發展__不同特色__的拼圖及解方, 但__目前__以第一組的__完整度__、__實用性__較高。')

yt_url= {'第1組-3分鐘-廣告.市場焦點機器人':['https://youtu.be/7xnzMr0B3b8',
            'https://docs.google.com/presentation/d/1pRoNldhsNV0JASts5NCjtUZW37ZCSJCkKcaZ97cgmio/edit'],
         '第1組-10分鐘-遴選.市場焦點機器人':['https://www.youtube.com/watch?v=Is2hGoqxx3k', 
            'https://docs.google.com/presentation/d/1pRoNldhsNV0JASts5NCjtUZW37ZCSJCkKcaZ97cgmio/edit'],
         '第2組-3分鐘-廣告.市場焦點機器人':['https://youtu.be/4i5B8hfvl6w',
            'https://github.com/yuchiahung/Fintech-2021-T2',
            'https://github.com/grangier/python-goose','https://www.reddit.com/r/stocks/'],
         '第2組-15分鐘介紹.市場焦點機器人':['https://youtu.be/gW8CkxQubj4',
            'https://github.com/cindy861103/FinTech'],
         '第3組-3分鐘-廣告.市場焦點機器人':['https://youtu.be/lDfDV1I2Pr4',
            'https://github.com/cindy861103/FinTech',
            'https://fintech-2021-t2.herokuapp.com/'],
         '第3組-15分鐘介紹.市場焦點機器人':['https://youtu.be/OBavep3gY_E',
            'https://github.com/cindy861103/FinTech',
            'https://docs.google.com/presentation/d/1wCp_DuqziA7V7OuUwSwhDqLeb1roQEePMqJO-Lh9V6k/edit?pli=1#slide=id.gdebbf90703_0_0'],
         '第4組-3分鐘-廣告.市場焦點機器人':['https://www.youtube.com/watch?v=sia8o_xN8ag'],
         '第4組-15分鐘介紹.市場焦點機器人':['https://www.youtube.com/watch?v=YFBpGaHVnz8',
            'https://docs.google.com/presentation/d/1MQPhJ3Q6MLSdl_gpJ3P4SDaCDUg-nHPyVTtCBlZ2FWY/edit']}

titles, urls = yt_url.keys(), yt_url.values()
with st.sidebar.beta_container():
    st.image('images/NanShan_Logo.png', width=256)
    st.markdown('''<h1 style="float: left;">南山人壽.投資-台大-東吳</h>''', unsafe_allow_html=True)
    st.write('Mentor: Jack & Taylor')
    
    title = st.selectbox('請選擇-各組專題成果影片: ', list(titles), 0)
    url = yt_url[title][0]

    qr_size = 5 #st.slider('Slide me', min_value = 6, max_value = 12, value = 6)
    qr_name = qr_maker.qr_code(link=url, logo=False,  size=qr_size)
    st.image(qr_name, caption=f'{title} - Youtube')

    #logo_file = st.file_uploader("./images/NanShan-New-Small.png")
    #open("./images/logo.png", "wb").write(logo_file.getbuffer())
    #hyper_link = 'https://fintech2021-youtube.herokuapp.com/'
    hyper_link = 'https://fintech2021-inv.herokuapp.com/'
    qr_name = qr_maker.qr_code(link=hyper_link, logo=False,  size=qr_size)
    st.image(qr_name, caption=hyper_link)


if url != '':
    #st_player(url)
    yt = YouTube(url)
    #raw_data = urllib.request.urlopen(yt.thumbnail_url).read()
    #image = Image.open(io.BytesIO(raw_data))#.resize((200, 200))
    #st.image(image)#, width=300)
    st.markdown(f'<h3 style="float: left;">{yt.title}</h3><a href={url}><img style="float: right;" src={yt.thumbnail_url} width="700"/></a>', unsafe_allow_html=True)

    #st.write('Understanding the Stream Object')
    #print(yt.streams)

    st.subheader('''Length: {:.2f} Minutes  ||   Rating: {} '''.format(yt.length/60.0 , yt.rating))
    video = yt.streams

    values = ['lowest','highest',"720p", "480p", "360p", "240p", "144p"]
    default_ix = values.index('highest')
    #desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

    with st.sidebar.beta_container():
        resolution_level = st.selectbox('Resolution Level ?', values, index=default_ix)
        #st.write('Chosing a Stream Object to Download')

    if len(video) > 0:
        downloaded , download_audio = False , False
        #yt_file = f'{title}.mp4'
        #yt_file =st.text_input('Download the video to :',yt_file)
        download_video = st.button("Download Video",)
        #if yt.streams.filter(only_audio=True):
        #    with st.sidebar.beta_container():
        #        download_audio = st.button("Download Audio Only")
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
