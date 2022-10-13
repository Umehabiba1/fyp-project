import streamlit as st
from streamlit_option_menu import option_menu
from keras.models import load_model
import cv2  
import numpy as np 
from PIL import Image, ImageOps

# Modify app name and Icon
# Config Function 
st.set_page_config(page_title='CROP DETECTION APP', page_icon='🎇', layout='wide', initial_sidebar_state='auto')

# Hide Menu and Footer
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """   
st.markdown(hide_menu_style, unsafe_allow_html=True)



st.title("🎇Crop Detection App🎇")
st.markdown('---')

with st.sidebar:
    selected = option_menu(
        menu_title='MY APP',
        options= ['ABOUT APP', 'MEMBERS','DETAIL', 'DETECTION'],
        icons = ['app-indicator', 'people-fill','arrow-90deg-right', 'star-half'],
        
        menu_icon = 'toggle-on',
        default_index = 0,
        orientation = 'vertical',
    )


if selected == 'ABOUT APP':
    img3 = Image.open('farm.jpg')
    st.title("~~~~~~~~~~~~ABOUT APP~~~~~~~~~~~~~")
    st.markdown('---')
    st.image(img3, use_column_width=True)
    st.markdown("#### **This is a Crop Detection App. This app is made using Streamlit, Keras and Python. This app is made for the purpose of detecting the crop based on the image of the crop. This app is made for the final year project.**")
    st.markdown('---')
    st.title("🎇HOW TO USE🎇")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### **1. Go to the sidebar.**")
        st.markdown("#### **2. Select the option 'DETECTION'.**")
        st.markdown("#### **3. Upload the image of the crop**")
        st.markdown("#### **4. The detected crop's name will be displayed.**")
    with c2:
        img4 = Image.open('use.jpeg')
        st.image(img4, width=100)
    st.markdown('---')



if selected == 'MEMBERS':
    st.title("~~~~~~~~~~~~~~~MEMBERS~~~~~~~~~~~~~~~")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### **Um-E-Habiba (GL)**")
        st.markdown("#### **18SW78**")
        img1 = Image.open('Habiba.jpeg')
        st.image(img1, width=200)
        
    with col2:
        st.markdown("#### **Areej jawed**")
        st.markdown("#### **18SW101**")
        img2 = Image.open('Areej.jpeg')
        st.image(img2, width=200)
        
    with col3:
        st.markdown("#### **Ansharah Siddique**")
        st.markdown("#### **18SW132**")
        img3 = Image.open('Ansharah.jpeg')
        st.image(img3, width=200)
        
    st.markdown('---')


if selected == 'DETAIL':
    st.title("Know About The Crops")
    st.markdown('---')
    st.markdown("## **Select the crop**")
    option= st.selectbox('', ('Wheat', 'Rice','Jute','Sugarcane','Maize'))
    if option=='Wheat':
        st.title("Wheat")
        wheat = Image.open('wheat.jpeg')
        st.image(wheat, use_column_width= True)
        st.markdown("#### **Wheat is one of the oldest and most important of the cereal crops. Of the thousands of varieties known, the most important are common wheat, used to make bread cake, crackers, cookies, pastries, and flours. Additionally, some wheat is used by industry for the production of starch, paste, malt, dextrose, gluten, alcohol, and other products.**")
        st.markdown("#### **Wheat is grown on more land area than any other food crop (220.4 million hectares or 545 million acres, 2014). World trade in wheat is greater than for all other crops combined. In 2020, world production of wheat was 761 million tonnes (1.7 trillion pounds), making it the second most-produced cereal after maize. Since 1960, world production of wheat and other grain crops has tripled and is expected to grow further through the middle of the 21st century.**")
        st.markdown('---')
        
        st.title("Wheat In Pakistan")
        st.markdown("#### **In Pakistan, spring wheat is grown as a Rabi crop in the Sindh, Punjab, NWFP, and Balochistan provinces. In the northern parts of Balochistan, some winter wheat is cultivated on a small scale. The wheat-growing area was 8.371 million hectares and production was 18.90 million tons in 1997-80. The major production area is in Punjab (71.17 %), followed by the Sindh province (13.38 %). However, the yield per acre is slightly higher in Sindh (2,410 kg) as compared to Punjab (2,316 kg).**")
        st.markdown("#### **In Punjab, wheat is mostly grown on irrigated land. Wheat production from rainfed areas is about 10 %. However, weather causes year-to-year fluctuations in crop production. Good rainfall means a good wheat crop. In the Sindh province, wheat is grown mostly on irrigated land. The small portion of unirrigated wheat depends on the retreat of the Indus river flood waters.Pakistan imports about 2 million tons of wheat at a cost of 8 billion rupees.**")


    elif option=='Rice':
        st.title("Rice")
        rice = Image.open('rice.jpg')
        st.image(rice, use_column_width= True)
        st.markdown("#### **Rice is the seed of the grass species Oryza sativa (Asian rice) or less commonly Oryza glaberrima (African rice). The name wild rice is usually used for species of the genera Zizania and Porteresia, both wild and domesticated, although the term may also be used for primitive or uncultivated varieties of Oryza. As a cereal grain, domesticated rice is the most widely consumed staple food for over half of the world's human population,[Liu 1] especially in Asia and Africa. It is the agricultural commodity with the third-highest worldwide production, after sugarcane and maize.**")
        st.markdown("#### **Rice cultivation is well-suited to countries and regions with low labor costs and high rainfall, as it is labor-intensive to cultivate and requires ample water. However, rice can be grown practically anywhere, even on a steep hill or mountain area with the use of water-controlling terrace systems**")
        st.markdown('---')
        st.title("Rice In Pakistan")
        st.markdown("#### **Pakistan is the world's 10th largest producer of rice. Pakistan's exports make up more than 8% of world's total rice trade.[1] It is an important crop in the agriculture economy of Pakistan. Rice is an important Kharif crop. In 2019, Pakistan produced 7.5 million tonnes of rice and ranked 10th in largest rice producing countries. In 2016/17, Pakistan produced 6.7 million tonnes, of which around 4 million were exported, mainly to neighbouring countries, the Middle East and Africa. Rice is grown in fertile lands of Punjab, Sindh and Balochistan region where millions of farmers rely on rice cultivation as their major source of employment. Among the most famous varieties grown in Pakistan include the Basmati, known for its flavour and quality. Pakistan is a major producer of this variety**")


    elif option=='Jute':
        st.title("Jute")
        jute = Image.open('jute.jpg')
        st.image(jute, use_column_width= True)
        st.markdown("#### **Jute is one of the most important natural fibers after cotton in terms of cultivation and usage. Cultivation is dependent on the climate, season, and soil. Almost 85% of the world's jute cultivation is concentrated in the Ganges Delta. This fertile geographic region is shared by both Bangladesh and India (mainly West Bengal). China also has a dominating place in jute cultivation. On a smaller scale, Thailand, Myanmar (Burma), Pakistan, Nepal, and Bhutan also cultivate jute.**")
        st.markdown("#### **The suitable climate for growing jute is a warm and wet climate, which is offered by the monsoon climate during the fall season, immediately followed by summer. Temperatures ranging to more than 25 °C and relative humidity of 70%–90% are favorable for successful cultivation. Jute requires 160–200 cm of rainfall yearly.Plain land or gentle slope or low land is ideal for jute cultivation. Since the jute seeds are small in size, land should be finely tilled, which can be done by careful ploughing.**")
        st.markdown('---')
        st.title("Jute In Pakistan")
        st.markdown("#### **The industry depends entirely on imported raw jute procured from Bangladesh as its exclusive source for raw material. Jute is a Kharif crop. It has a cultivation period of 120-150 days. It is sown from March to May and harvested from June to September. During FY21, Pakistan’s raw jute imports stood at PKR 8,491mln as compared to PKR 4,852mln in FY20, an increase of 75%. The increase came on the back of significantly higher import prices due to decline in raw jute production in Bangladesh.**")
        
    elif option=='Sugarcane':
        st.title("Sugarcane")
        sugarcane = Image.open('sugarcane.jpg')
        st.image(sugarcane, use_column_width= True)
        st.markdown("#### **Sugarcane, (Saccharum officinarum), perennial grass of the family Poaceae, primarily cultivated for its juice from which sugar is processed. Most of the world’s sugarcane is grown in subtropical and tropical areas. The plant is also grown for biofuel production, especially in Brazil, as the canes can be used directly to produce ethyl alcohol (ethanol).**")
        st.markdown("#### **Sugarcane is grown in various kinds of soils, such as red volcanic soils and alluvial soils of rivers. The ideal soil is a mixture of sand, silt, and clay particles, with a measure of organic material. The land is plowed and left to weather for a time before subsoiling (stirring up the subsoil) is carried out. The crop demands a well-drained soil, and drains—on the surface, underground, or both—are provided according to the topographic conditions of the fields.**")
        
        st.markdown('---')
        st.title("Sugarcane In Pakistan")
        st.markdown("#### **Sugarcane is an important cash crop of Pakistan. It is mainly grown for sugar and sugary production. It is an important source of income and employment for the farming community of the country. It also forms essential item for industries like sugar, chip board, paper, barrages, confectionery, uses in chemicals, plastics, paints, synthetics, fiber, insecticides and detergents. Sugarcane production in the country has increased over time. In 1988, the area under sugarcane was 878 x 103 hectares which increased to 886 x 103 hectares in 1992 and sugarcane production increased for 36976 x 103 tons in 1988 to 38059 x 103 tons in 1992. Despite expansion in production over years, increase in the productivity per unit of area has been very low in Pakistan. The average sugarcane production in the country required static between 45-50 tons/ha, which is very much low compared to the cane production by other countries. The average yield of sugarcane in the world is around 60 metric tons/ha, while India and Egypt are getting around 66 tons and 105 tons/has, respectively. In this way, Egypt with highest cane yield in the world is getting about 142 per cent high-yield than Pakistan. India with almost similar soil and climatic conditions is obtaining about 53 per cent higher cane yield than Pakistan. As it is one of the cash crops of the country, therefore, efforts should be made to improve its productivity. As a result of these efforts, substantial improvement can take place in its yield. Improved seed production, quality control and distribution depends largely upon the availability of skilled and competent local manpower, which is present in insufficient in most developing countries..**")
        st.markdown("#### **In order to increase the production of sugar cane several steps were taken by the Govt. and the sugar mill association to help formers.**")

    elif option=='Maize':
        st.title("Maize")
        maize = Image.open('maize.jpeg')
        st.image(maize, use_column_width= True)
        st.markdown("#### **Maize has become a staple food in many parts of the world, with the total production of maize surpassing that of wheat or rice. In addition to being consumed directly by humans (often in the form of masa), maize is also used for corn ethanol, animal feed and other maize products, such as corn starch and corn syrup. The six major types of maize are dent corn, flint corn, pod corn, popcorn, flour corn, and sweet corn.Sugar-rich varieties called sweet corn are usually grown for human consumption as kernels, while field corn varieties are used for animal feed, various corn-based human food uses (including grinding into cornmeal or masa, pressing into corn oil, fermentation and distillation into alcoholic beverages like bourbon whiskey), and as feedstocks for the chemical industry. Maize is also used in making ethanol and other biofuels.**")
        st.markdown("#### **Maize is widely cultivated throughout the world, and a greater weight of maize is produced each year than any other grain.In 2021, total world production was 1.2 billion tonnes. Maize is the most widely grown grain crop throughout the Americas, with 384 million metric tons grown in the United States alone in 2021.[citation needed] Genetically modified maize made up 85% of the maize planted in the United States in 2009.Subsidies in the United States help to account for its high level of cultivation of maize and its position as the largest producer in the world.**")
        
        st.markdown('---')
        st.title("Maize In Pakistan")
        st.markdown("#### **Maize is Pakistan’s third most important cereal following wheat and rice, encompassing an area of 1.3 million hectares. Maize productivity is also among the highest in South Asia, with national yields reaching almost 5 tons per hectare.**")
        st.markdown("#### **The bulk (99%) of total production comes from two major provinces, with NWFP accounting for 51% of the total area and 31% of total production and Punjab contributing 48% of the area and 69% of total maize grain production. A small amount (1.0%) is produced in the provinces of Sindh and Baluchistan. Though not included in Pakistan’s official statistics, maize is an important crop in Azad Jammu Kashmir, with about 0.122 million ha of maize being planted during autumn. Similarly, an increasingly important and high yielding sector is the spring maize produced in Punjab, which covers around 0.10 million ha and produces about 0.71 million tons of maize grain. Approximately 66% of the maize in Pakistan has access to irrigation; the remainder is farmed under strictly rain-fed conditions. Eighty four percent of the maize production in Pakistan is concentrated in two principal geographic clusters, consisting of 11 districts in NWFP/Northern Punjab and 9 districts in the central Punjab.**")
        










if selected == 'DETECTION':
    st.title("🎇DETECTION🎇")
    st.set_option('deprecation.showfileUploaderEncoding', False)
    
    st.markdown("## **Upload the image of the crop**")
    file_in = st.file_uploader("", type=["jpg", "png", "jpeg"])
    model_final = load_model('crop_inception.h5')

    def f_crop_pred(A, model_final):
        size = (224, 224)
        image = ImageOps.fit(A, size, Image.ANTIALIAS)
        img = np.asarray(image)
        img = img/255.0
        img_reshape = img.reshape(1,224,224,3)
        pred = model_final.predict(img_reshape).argmax()
        
        dict_pred2lab = {0:'jute', 1:'maize', 2:'rice', 3:'sugarcane', 4:'wheat'}
        
        lab_text = dict_pred2lab[pred]
        
        st.success(lab_text)
        
        return lab_text

    if file_in is None:
        st.write("Please upload an image file")
    else:
        image = Image.open(file_in)
        st.markdown("---")
        st.title("I M A G E")
        st.image(image, use_column_width=True)
        st.write("")
        st.markdown("---")
        st.title("🎇D E T E C T E D__C R O P🎇")
        f_crop_pred(image, model_final)

    

