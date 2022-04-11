import pickle
import streamlit as st
pickle_in = open('bcn.pkl', 'rb')
bcn_clf = pickle.load(pickle_in)


@st.cache()
                        
def diagnostics(Clump_Thickness,Uniformity_of_Cell_Size,Uniformity_of_Cell_Shape,Marginal_Adhesion,Single_Epithelial_Cell_Size,Bare_Nuclei,Bland_Chromatin,Normal_Nucleoli,Mitoses):
    prediction = bcn_clf.predict([[Clump_Thickness,Uniformity_of_Cell_Size,Uniformity_of_Cell_Shape,Marginal_Adhesion,Single_Epithelial_Cell_Size,Bare_Nuclei,Bland_Chromatin,Normal_Nucleoli,Mitoses]])[0]
    if prediction == 0:
        report =  "Tumor is likely to be Benign (Non cancerous)"
        
    elif prediction == 1:
        report = "Tumor is likely to be Malignant (Cancerous)"
    return report


def main():
    st.title('BreastCancer Detection Model')

   

    Clump_Thickness =  st.slider("Clump Thickness", 0, 10)
    
    Uniformity_of_Cell_Size = st.slider(" Uniformity of Cell Size", 0, 10)
    
    Uniformity_of_Cell_Shape = st.slider(" Uniformity of Cell Shape", 0, 10)
    
    Marginal_Adhesion = st.slider("Marginal Adhesion", 0, 10)
    
    Single_Epithelial_Cell_Size = st.slider("Single Epithelial Cell Size", 0, 10)
    
    Bare_Nuclei = st.slider("Bare Nuclei", 0, 10)
    
    Bland_Chromatin = st.slider("Bland Chromatin", 0, 10)
    
    Normal_Nucleoli = st.slider("Normal Nucleoli", 0, 10)
    
    Mitoses = st.slider("Mitoses", 0, 10)
    
    result = ""
      
    if st.button("RESULT"):
        result = diagnostics(Clump_Thickness,Uniformity_of_Cell_Size,Uniformity_of_Cell_Shape,Marginal_Adhesion,Single_Epithelial_Cell_Size,Bare_Nuclei,Bland_Chromatin,Normal_Nucleoli,Mitoses)
        st.success(result)
        print("Just test")
    st.write('Written by JOSHUA PEREIRA')
if __name__ =='__main__':
    main()
 
    
