from altair.vegalite.v4.api import value
import streamlit as st
from pytube import YouTube

st.title("金融科技專題:文本生成-市場焦點機器人")

yt_url= {'第1組-3分鐘-廣告.市場焦點機器人':['https://youtu.be/7xnzMr0B3b8',
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
    
    title = st.selectbox('請選擇-專題成果影片: ', list(titles), 0)
    url = yt_url[title][0]
    if len(yt_url[title])>1:
        gits = '<a href="{git}" target="_blank">Github</a> | '.format(git=yt_url[title][1])
    else:
        gits = ''
    #st.info(f"{title} {url}")

#url = st.text_input(label='URL', value=url)

if url != '':
    #st.write(f'Getting the Data for the Youtube video \n{url}')
    yt = YouTube(url)
    #raw_data = urllib.request.urlopen(yt.thumbnail_url).read()
    #image = Image.open(io.BytesIO(raw_data))#.resize((200, 200))
    #st.image(image)#, width=300)
    st.markdown(f'<h3 style="float: left;">{gits}{yt.title}</h3><a href={url}><img style="float: right;" src={yt.thumbnail_url} width="700"/></a>', unsafe_allow_html=True)

    #st.write('Understanding the Stream Object')
    #print(yt.streams)

    st.subheader('''Length: {:.2f} Minutes  ||   Rating: {} '''.format(yt.length/60.0 , yt.rating))
    video = yt.streams

    values = ['lowest','highest',"720p", "480p", "360p", "240p", "144p"]
    default_ix = values.index('highest')

    with st.sidebar.beta_container():
        resolution_level = st.selectbox('Resolution Level ?', values, index=default_ix)
        #st.write('Chosing a Stream Object to Download')

    if len(video) > 0:
        downloaded , download_audio = False , False
        with st.sidebar.beta_container():
            download_video = st.button("Download Video")
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
            video.filter(only_audio=True).first().download()
            downloaded = True
        if downloaded:
            st.subheader("Download Complete")
    else:
        st.subheader("Sorry, this video can not be downloaded")
