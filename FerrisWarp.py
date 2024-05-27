def use_ids(ids):
    responsibilities = []
    for id in ids:
        if id in data_dict:
            work_experiences = data_dict[id]['resume']['workExperience']
            person_responsibilities = '\n'.join([responsibility for experience in work_experiences for responsibility in experience['responsibilities']])
            responsibilities.append(person_responsibilities)
    
    df = pd.DataFrame({'responsibilities': responsibilities})


    for index, row in df.iterrows():
        st.markdown(f"""
        

            
{row[0]}


        

        """, unsafe_allow_html=True)
