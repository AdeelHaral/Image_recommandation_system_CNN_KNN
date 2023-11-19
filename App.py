!pip install streamlit
import streamlit as st
def upload_files(upload_files):
  try:
    with open(os.path.join('uploads',upload_files.name)) as f:
      f.write(upload_files.getbuffer())
      return 1
  except:
    return 0
def recommned(feature,feature_list):
  neigbor = NearestNeighbors(n_neighbors=6,algorithm='brute',metric='euclidean')
  neigbor.fit(feature_list)
  d,i = neigbor.kneighbors([features])
  return i


upload_file = st.file_uploader("choose an image")
print(upload_file)
if upload_file is not None:
  display_image= Image.open(upload_file)
  resize_img= display_image.resize((200,200))
  st.image(resized_img)
  features= extract_features(os.path.join('uploads',upload_file.name),model)
  indices = recommned(features,Fl)
  col1,col2,col3,col4,col5= st.beta_columns(5)
  with col1:
    st.images(fn[[i[0][0]]])
  with col2:
    st.images(fn[[i[0][2]]])
  with col4:
    st.images(fn[[i[0][3]]])
  with col5:
    st.images(fn[[i[0][4]]])
else:
    st.header("some err0r occured")
  st.title("Image bases Recommandation system")
