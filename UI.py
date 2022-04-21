import streamlit as st
import os


st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 350px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 350px;
        margin-left: -350px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.sidebar.title("CSP Project")

Mode=st.sidebar.selectbox('Choose mode',
['About Project','Website',"Crop Variation","Team"]
)

if Mode =='Team':
    st.title("Our Team")

    st.image(os.path.join('./images','Apples.jpeg'),width=200)
    st.markdown("""
    <style>
            #id2{
            background-color: Dodgerblue;
            border: 10px,solid,black;
            color: white;
            padding: 2px 6px;
            font-size: 16px;
            # cursor: pointer;
            }
            #id2:hover {
                color: black;
                background-color:royalblue;
                text-decoration: underline;
            }
            #id3 {
                    font-family: 'Times New Roman', Times, serif;
                    padding-left: 20px;
                    font-size: 16px;
                    color: white;
                    border:1px,solid;
                    margin:1px;
                    padding:2px 6px;
            }
    </style>
    <a  href="https://www.linkedin.com/in/pallerla-bharath-kumar-08a888212"  target="_blank"><button id="id2">Subramanyan</button></a>
    <p id="id3">Associate Professor, Department of  Computer Science and Engineering<br>Kalasalingam Academy of Research and Education <br>Krishnankoil, India</p>
    """,unsafe_allow_html=True)

    st.image(os.path.join('./images','Apples.jpeg'),width=200)
    st.markdown("""
    <style>
            #id2{
            background-color: Dodgerblue;
            border: 10px,solid,black;
            color: white;
            padding: 2px 6px;
            font-size: 16px;
            # cursor: pointer;
            }
            #id2:hover {
                color: black;
                background-color:royalblue;
                text-decoration: underline;
            }
            #id3 {
                    font-family: 'Times New Roman', Times, serif;
                    padding-left: 20px;
                    font-size: 16px;
                    color: white;
                    border:1px,solid;
                    margin:1px;
                    padding:2px 6px;
            }
    </style>
    <a  href="https://www.linkedin.com/in/pallerla-bharath-kumar-08a888212"  target="_blank"><button id="id2">P.Bharath Kumar</button></a>
    <p id="id3">Student, Department of  Computer Science and Engineering<br>Kalasalingam Academy of Research and Education <br>Krishnankoil, India</p>
    """,unsafe_allow_html=True)

    st.image(os.path.join('./images','Apples.jpeg'),width=200)
    st.markdown("""
    <style>
            #id2{
            background-color: Dodgerblue;
            border: 10px,solid,black;
            color: white;
            padding: 2px 6px;
            font-size: 16px;
            # cursor: pointer;
            }
            #id2:hover {
                color: black;
                background-color:royalblue;
                text-decoration: underline;
            }
            #id3 {
                    font-family: 'Times New Roman', Times, serif;
                    padding-left: 20px;
                    font-size: 16px;
                    color: white;
                    border:1px,solid;
                    margin:1px;
                    padding:2px 6px;
            }
    </style>
    <a  href="https://www.linkedin.com/in/pallerla-bharath-kumar-08a888212"  target="_blank"><button id="id2">V.Sai Sumanth</button></a>
    <p id="id3">Student, Department of  Computer Science and Engineering<br>Kalasalingam Academy of Research and Education <br>Krishnankoil, India</p>
    """,unsafe_allow_html=True)

    st.image(os.path.join('./images','Apples.jpeg'),width=200)
    st.markdown("""
    <style>
            #id2{
            background-color: Dodgerblue;
            border: 10px,solid,black;
            color: white;
            padding: 2px 6px;
            font-size: 16px;
            # cursor: pointer;
            }
            #id2:hover {
                color: black;
                background-color:royalblue;
                text-decoration: underline;
            }
            #id3 {
                    font-family: 'Times New Roman', Times, serif;
                    padding-left: 20px;
                    font-size: 16px;
                    color: white;
                    border:1px,solid;
                    margin:1px;
                    padding:2px 6px;
            }
    </style>
    <a  href="https://www.linkedin.com/in/pallerla-bharath-kumar-08a888212"  target="_blank"><button id="id2">V.Vishal</button></a>
    <p id="id3">Student, Department of  Computer Science and Engineering<br>Kalasalingam Academy of Research and Education <br>Krishnankoil, India</p>
    """,unsafe_allow_html=True)

    st.image(os.path.join('./images','Apples.jpeg'),width=200)
    st.markdown("""
    <style>
            #id2{
            background-color: Dodgerblue;
            border: 10px,solid,black;
            color: white;
            padding: 2px 6px;
            font-size: 16px;
            # cursor: pointer;
            }
            #id2:hover {
                color: black;
                background-color:royalblue;
                text-decoration: underline;
            }
            #id3 {
                    font-family: 'Times New Roman', Times, serif;
                    padding-left: 20px;
                    font-size: 16px;
                    color: white;
                    border:1px,solid;
                    margin:1px;
                    padding:2px 6px;
            }
    </style>
    <a  href="https://www.linkedin.com/in/pallerla-bharath-kumar-08a888212"  target="_blank"><button id="id2">P.Vamshi Krishna</button></a>
    <p id="id3">Student, Department of  Computer Science and Engineering<br>Kalasalingam Academy of Research and Education <br>Krishnankoil, India</p>
    """,unsafe_allow_html=True)





if Mode =='Crop Variation':
    st.markdown("""
        <img id="id1" src="https://www.researchgate.net/profile/Amit-Thorat/publication/263151012/figure/tbl1/AS:674345483522051@1537787900838/Composition-and-growth-in-agriculture-in-India.png" alt="its dream" width="600px" height="400px" usemap="#bharath">

        """,
        unsafe_allow_html=True)
    st.write("")
    st.markdown('''
        <style>
            #id2{
            background-color: DodgerBlue;
            border: 10px,solid,black;
            color: white;
            padding: 2px 6px;
            font-size: 16px;
            cursor: pointer;
            }
            #id2:hover {
                color: black;
                background-color:royalblue;
                text-decoration: underline;
            }
        </style>
        <a  href="https://agricoop.nic.in/en/all-india-crop-situation"  target="_blank"><button id="id2">Details of crop prices</button></a>

                ''',unsafe_allow_html=True)


if Mode =='About Project':

    st.image(os.path.join('./images','about.jpg'),use_column_width=True)
    st.markdown(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>Document</title>
            <style>
                .class1 {
                    font-family: 'Times New Roman', Times, serif;
                    font-size: 50px;
                    font-weight: bold;
                    color:lightseagreen;
                }
                .class2 {
                    padding-left: 300px;
                    font-style: italic;
                    color:crimson;
                }
                .classmain {
                    display: flex;
                    flex-flow: column;
                    text-align: center;
                }
                ul {
                    list-style: disc;
                }
                #id1 {
                    font-family: 'Times New Roman', Times, serif;
                    padding-left: 20px;
                    font-size: 30px;
                    color: cornflowerblue;
                }
                #id2 {
                    font-family: 'Times New Roman', Times, serif;
                    padding-left: 20px;
                    font-size: 30px;
                    color: cornflowerblue;
                }
                p{
                    padding-left: 20px;
                }
            </style>
            <link rel="stylesheet" href="crop.css">
        </head>
        <body>
            <div class="classmain">
                <div class="class1"><u>Easy Groceries</u></div>
                <div class="class2">by TEAM AGRO </div>
            </div>
            <p id="id1"><strong><u>Vision:</u></strong></p>
            <p>
            <ul>
                <li>
                    Traditional agricultural value chains involve multiple
                    intermediaries between farmers and consumers.
                    Typically, farmers sell their produce at the farm
                    gates to middlemen. Produce then passes through
                    multiple intermediaries before reaching the end
                    customer. As a result, farmers receive only a small
                    proportion of the price paid by the end consumer as
                    each intermediary in the value chain earns a margin. 
                </li>
                <li>
                    Agri e-commerce provides an opportunity to
                    streamline the agricultural value chain and reduce
                    inefficiencies in the distribution of farm produce. It
                    represents a new way for farmers to sell their produce
                    to an array of buyers, including agri businesses,
                    retailers, restaurants and consumers. 
                </li>
                <li>
                    Agri e-commerce
                    also increases farmers’ access to new markets and
                    adds transparency to the value chain. It enables
                    farmers to bypass several intermediaries, resulting in
                    higher income for the farmers, reduced wastage, and
                    the potential to deliver fresher produce to customers. 
                    Such benefits are especially significant in developing
                    regions, where more than 97% of people employed in
                    agriculture live and where the sector’s contribution to
                    GDP is in double digits.   
                </li>
                <li>
                    In addition our team has developed an e-commerce website. The customers are encouraged to buy
                    the products which are directly from the fields.
                </li>
            </ul>
            </p>
            <p id="id2"><strong><u>Note:</u></strong></p>
            <ul>
                <li>In this application we are using Razorpay for creating a Ecommerce website. 
                StreamLit is to create the Web Graphical User Interface (GUI) 
                </li>
            </ul>
        </body>
        </html>
        """, unsafe_allow_html=True)


if Mode =='Website':
    # st.image(os.path.join('./images','about.jpg'),use_column_width=True)
    st.markdown("""
        <img id="id1" src="https://www.globalsign.com/application/files/2516/0498/6435/General_Banner_Online_Shopping_Blog_1_APAC_2020_09_03.jpg" alt="its dream" width="600px" height="400px" usemap="#bharath">

        """,
        unsafe_allow_html=True)
    st.write("")
    st.markdown('''
        <style>
            #id2{
            background-color: DodgerBlue;
            border: 10px,solid,black;
            color: white;
            padding: 2px 6px;
            font-size: 16px;
            cursor: pointer;
            }
            #id2:hover {
                color: black;
                background-color:royalblue;
                text-decoration: underline;
            }
        </style>
        <a  href="https://neerajpokala143.wixsite.com/ecommrece"  target="_blank"><button id="id2">website link</button></a>
                ''',unsafe_allow_html=True)

if Mode =='Payment Page':
    # st.image(os.path.join('./images','about.jpg'),use_column_width=True)
    st.markdown("""
        <img id="id1" src="https://img.freepik.com/free-vector/concept-landing-page-credit-card-payment_52683-25084.jpg" alt="its dream" width="600px" height="400px" usemap="#bharath">

        """,
        unsafe_allow_html=True)
    st.write("")
    st.markdown('''
        <form action=https://dashboard.razorpay.com/app/paymentpages/pl_Iv1HuFopHEgOFR/payments#paymentpages>
        <style>
            #id2{
            background-color: red;
            border: 10px,solid,black;
            color: white;
            padding: 2px 6px;
            font-size: 16px;
            cursor: pointer;
            }
            #id2:hover {
                color: black;
                background-color:royalblue;
                text-decoration: underline;
            }
        </style>

        <input id="id2" type=submit here value="Payment Details"/>

        </form>

                ''',unsafe_allow_html=True)



    # st.markdown("<h1 style='text-align: center; color: skyblue; '>Easy Groceries </h1>", unsafe_allow_html=True)
    # st.markdown('''
    # In this application we are using **Razorpay** for creating a Ecommerce website. \n

    # '**StreamLit** is to create the Web Graphical User Interface (GUI) 
    # ''')
    # st.markdown(
    # """
    # <style>
    # [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
    #     width: 400px;
    # }
    # [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
    #     width: 400px;
    #     margin-left: -400px;
    # }
    # </style>
    # """,
    # unsafe_allow_html=True,
    # )
    # st.video('https://www.youtube.com/watch?v=KXkBZCe699A')

    # st.markdown('''
    #           # About Project \n 
    #             Hey this is ** Neeraj Pokala **. \n
                
                
    #             Also check me out on Social Media
    #             - [git-Hub](https://github.com/PallerlaBharathKumar) 
    #             - [LinkedIn](https://www.linkedin.com/in/pallerla-bharath-kumar-08a888212)
    #             - [Instagram](https://instagram.com/im.bharath__?utm_medium=copy_link)\n
    #             If you are interested in building more about Microsoft Azure then   [click here](https://azure.microsoft.com/en-in/)\n
    #             For any Troubleshooting and Further UI development feel free to DM me at --- pallerlabharath09@gmail.com
    #             ''')




# if Mode=='Crop Details':

#     selector=st.sidebar.selectbox('Choose Crop',
#     ['Apple','Corn','banana','Rice']
#     )
#     if selector=='Apple':
#         st.markdown("<h1 style='text-align: center; color: skyblue; '><u>Crops</u> </h1>", unsafe_allow_html=True)

#         #Apple
#         st.markdown("<h1 style='text-align: left; color: red; '><u>Apples</u> </h1>", unsafe_allow_html=True)
#         st.image(os.path.join('./images','image1.jpg'),width=250 )
#         st.markdown("<h4 style='text-align: left; color: yellow; '><u>About</u> </h4>", unsafe_allow_html=True)
#         st.markdown('''
#         Apples contain high content of fiber and vitamins in them \n
#         Apples are used as an ingredient in fruit salads or desserts like custards or else they can be prepared into milk shakes''')
        
#         st.markdown("""
#         <img id="id1" src="https://www.verywellhealth.com/thmb/VtIaA_plARsDh_sD5agmy7pOIxw=/1698x955/smart/filters:no_upscale()/apples-2-56a144bd3df78cf7726902c5.jpg" alt="its dream" width="600px" height="300px" usemap="#bharath">

#         """,
#         unsafe_allow_html=True)



#         st.markdown('''
#               # 
#                 <h4 style='text-align: left; color: mediumseagreen; '><u>seller</u></h4>
#                 Sold by AKD FRESH and delivered by AGRO  \n
#                 Secure Transaction Powered by RazorPay
#                 ''',unsafe_allow_html=True)

#         #submit button
#         st.markdown('''
#         <form action=https://rzp.io/l/Agrosevicesfirst>
#         <style>
#             #id2{
#             background-color: DodgerBlue;
#             border: 10px,solid,black;
#             color: white;
#             padding: 2px 6px;
#             font-size: 16px;
#             cursor: pointer;
#             }
#             #id2:hover {
#                 color: black;
#                 background-color:royalblue;
#                 text-decoration: underline;
#             }
#         </style>

#         <input id="id2" type=submit here value="Buy Now"/>

#         </form>

#                 ''',unsafe_allow_html=True)




#     if selector=='Corn':
#         #st.markdown("<h1 style='text-align: center; color: skyblue; '><u>Crops</u> </h1>", unsafe_allow_html=True)

#         #Apple
#         st.markdown("<h1 style='text-align: left; color: yellow; '><u>Corn</u> </h1>", unsafe_allow_html=True)
#         st.image(os.path.join('./images','image3.jpg'),width=250 )
#         st.markdown("<h4 style='text-align: left; color: purple; '><u>About</u> </h4>", unsafe_allow_html=True)
#         st.markdown('''
#         Apples contain high content of fiber and vitamins in them \n
#         Apples are used as an ingredient in fruit salads or desserts like custards or else they can be prepared into milk shakes''')
        
#         st.markdown('''
#               # 
#                 <h4 style='text-align: left; color: mediumseagreen; '><u>seller</u></h4>
#                 Sold by AKD FRESH and delivered by AGRO  \n
#                 Secure Transaction Powered by RazorPay
#                 ''',unsafe_allow_html=True)

#         #submit button
#         st.markdown('''
#         <form action=https://rzp.io/l/f1uaWjwH7J>
#         <style>
#             #id2{
#             background-color: DodgerBlue;
#             border: 10px,solid,black;
#             color: white;
#             padding: 2px 6px;
#             font-size: 16px;
#             cursor: pointer;
#             }
#             #id2:hover {
#                 color: black;
#                 background-color:royalblue;
#                 text-decoration: underline;
#             }
#         </style>

#         <input id="id2" type=submit here value="Buy Now"/>

#         </form>

#                 ''',unsafe_allow_html=True)



        