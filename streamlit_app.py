import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt

from functools import reduce
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

st.header(":rainbow[You are at a Fabulous site]")

ind_sel = st.sidebar.selectbox("Please select the desired Indices", options=['NIFTY','None'], index=1, key='indice_sel1')

file1=st.file_uploader("kindly upload your file here", key='file_upload')

if file1 is not None:
    data=pd.read_excel(file1)

#data=pd.read_excel('C:\\Users\\Dell\\Desktop\\Excel_files\\12_06_2024.xlsx', sheet_name='NIFTY')

data=data.replace('-',0)
data1 = data.copy()

my_strike1= 18000           # strikes for bar charts of OI and Chnage OI
my_strike2= 25000           # strikes for bar charts of OI and Chnage OI

stk_ind1= 2
stk_ind2= 8

range_01= range(my_strike1,my_strike2,50)

data_bt=data1[data1.STRIKE.between(my_strike1, my_strike2)]

strike_option11= data1['STRIKE'].unique()  #  Select the selection option range of strike in OI  and change OI tabs
time_option11= data1['Time'].unique()

final_data=data_bt[['Time','CALL_OI','PUT_OI','CALL_CHNG','PUT_CHNG','CALL_LTP','PUT_LTP','STRIKE','CALL_VOLUME','PUT_VOLUME','Spot_Price', 'CALL_VOLUME', 'PUT_VOLUME']] 

def nifty():
    col1, col2=st.columns(2)
    with col1: 
        sort_data=data_bt[['Time','CALL_OI','PUT_OI','CALL_CHNG','PUT_CHNG','CALL_LTP','PUT_LTP','STRIKE','CALL_VOLUME','PUT_VOLUME','Spot_Price']] 
        cl_time_list1 =data1['Time'].unique()           # selecting unique time for the selected data
        begning_time1= st.selectbox("select the begning Time", options=cl_time_list1, key='time_sel')
        filter= sort_data[sort_data['Time'] == begning_time1]
        filter_background=filter.style.background_gradient(cmap='Oranges', subset=['CALL_OI','PUT_OI','CALL_CHNG', 'PUT_CHNG','CALL_VOLUME','PUT_VOLUME','CALL_LTP','PUT_LTP','Spot_Price',]).format(precision=2)  
        st.dataframe(filter_background, hide_index=True, column_order=['Time','CALL_OI','CALL_CHNG','CALL_VOLUME','CALL_LTP','STRIKE','PUT_LTP','PUT_VOLUME','PUT_CHNG','PUT_OI','Spot_Price'], use_container_width=True)
    
    with col2:
        sort_data=data_bt[['Time','CALL_OI','PUT_OI','CALL_CHNG','PUT_CHNG','CALL_LTP','PUT_LTP','STRIKE','CALL_VOLUME','PUT_VOLUME','Spot_Price']] 
        cl_time_list2=data1['Time'].sort_values(ascending=False).unique()
        last_time1= st.selectbox("select the begning Time", options=cl_time_list2, key='time_se2')
        filter= sort_data[sort_data['Time'] == last_time1]
        filter_background=filter.style.background_gradient(cmap='Blues', subset=['CALL_OI','PUT_OI','CALL_CHNG', 'PUT_CHNG','CALL_VOLUME','PUT_VOLUME','CALL_LTP','PUT_LTP','Spot_Price']).format(precision=2)  
        st.dataframe(filter_background, hide_index=True, column_order=['Time','CALL_OI','CALL_CHNG','CALL_VOLUME','CALL_LTP','STRIKE','PUT_LTP','PUT_VOLUME','PUT_CHNG','PUT_OI','Spot_Price'], use_container_width=True)

OI_strike_one=2
OI_strike_two=4
OI_strike_three=5
OI_strike_four=6
OI_strike_five=7
OI_strike_six=8

def tab_nifty():
    exp1=st.expander("Details of price")
    with exp1:
        tab1, tab2, tab3, tab4, tab5,tab6, tab7=st.tabs(['OI Data', 'CHNG OI Data','OI Chart', 'CHNG OI Chart','Chart OI Second','Chart CHNG Second','strike target'])
# OI data
        with tab1:
            col1, col2, col3, col4, col5, col6=st.columns(6)
        
        with col1:
            stk1=st.selectbox("Strke_one", options=range_01, key='stk_01', index=OI_strike_one)
            final_data_OI=final_data[final_data['STRIKE']==stk1]
            final_data1=final_data_OI[['Time','CALL_OI','PUT_OI']].sort_values(by='Time', ascending=False).style.background_gradient(cmap='Blues', subset=['CALL_OI', 'PUT_OI']).format(precision=2)
            st.dataframe(final_data1, hide_index=True, use_container_width=True)

        with col2:
            stk2=st.selectbox("Strke_two", options=range_01, key='stk_02', index=OI_strike_two)
            final_data_OI=final_data[final_data['STRIKE']==stk2]
            final_data1=final_data_OI[['Time','CALL_OI','PUT_OI']].sort_values(by='Time', ascending=False).style.background_gradient(cmap='Blues', subset=['CALL_OI', 'PUT_OI']).format(precision=2)
            st.dataframe(final_data1, hide_index=True, use_container_width=True)
        
        with col3:
            stk3=st.selectbox("Strke_three", options=range_01, key='stk_03', index=OI_strike_three)
            final_data_OI=final_data[final_data['STRIKE']==stk3]
            final_data1=final_data_OI[['Time','CALL_OI','PUT_OI']].sort_values(by='Time', ascending=False).style.background_gradient(cmap='Blues', subset=['CALL_OI', 'PUT_OI']).format(precision=2)
            st.dataframe(final_data1, hide_index=True, use_container_width=True)

        with col4:
            stk4=st.selectbox("Strke_four", options=range_01, key='stk_04', index=OI_strike_four)
            final_data_OI=final_data[final_data['STRIKE']==stk4]
            final_data1=final_data_OI[['Time','CALL_OI','PUT_OI']].sort_values(by='Time', ascending=False).style.background_gradient(cmap='Blues', subset=['CALL_OI', 'PUT_OI']).format(precision=2)
            st.dataframe(final_data1, hide_index=True, use_container_width=True)

        with col5:
            stk5=st.selectbox("Strke_five", options=range_01, key='stk_05', index=OI_strike_five)
            final_data_OI=final_data[final_data['STRIKE']==stk5]
            final_data1=final_data_OI[['Time','CALL_OI','PUT_OI']].sort_values(by='Time', ascending=False).style.background_gradient(cmap='Blues', subset=['CALL_OI', 'PUT_OI']).format(precision=2)
            st.dataframe(final_data1, hide_index=True, use_container_width=True)

        with col6:
            stk6=st.selectbox("Strke six", options=range_01, key='stk_06', index=OI_strike_six)
            final_data_OI=final_data[final_data['STRIKE']==stk6]
            final_data1=final_data_OI[['Time','CALL_OI','PUT_OI']].sort_values(by='Time', ascending=False).style.background_gradient(cmap='Blues', subset=['CALL_OI', 'PUT_OI']).format(precision=2)
            st.dataframe(final_data1, hide_index=True, use_container_width=True)

# change OI data

        with tab2:
            col11, col12, col13, col14, col15, col16=st.columns(6)
            with col11:
                CHNG1=st.selectbox("strike one", options=range_01, key='CHNG_01', index=OI_strike_one)
                final_data_OI=final_data[final_data['STRIKE']==CHNG1]
                final_data1=final_data_OI[['Time','CALL_CHNG','PUT_CHNG']].sort_values(by='Time', ascending=False).style.background_gradient(cmap='Blues', subset=['CALL_CHNG', 'PUT_CHNG']).format(precision=2)
                st.dataframe(final_data1, hide_index=True, use_container_width=True)

            with col12:
                CHNG2=st.selectbox("strike two", options=range_01, key='CHNG_02', index=OI_strike_two)
                final_data_OI=final_data[final_data['STRIKE']==CHNG2]
                final_data1=final_data_OI[['Time','CALL_CHNG','PUT_CHNG']].sort_values(by='Time', ascending=False).style.background_gradient(cmap='Blues', subset=['CALL_CHNG', 'PUT_CHNG']).format(precision=2)
                st.dataframe(final_data1, hide_index=True, use_container_width=True)
            
            with col13:
                CHNG3=st.selectbox("strike three", options=range_01, key='CHNG_03', index=OI_strike_three)
                final_data_OI=final_data[final_data['STRIKE']==CHNG3]
                final_data1=final_data_OI[['Time','CALL_CHNG','PUT_CHNG']].sort_values(by='Time', ascending=False).style.background_gradient(cmap='Blues', subset=['CALL_CHNG', 'PUT_CHNG']).format(precision=2)
                st.dataframe(final_data1, hide_index=True, use_container_width=True)

            with col14:
                CHNG4=st.selectbox("strike four", options=range_01, key='CHNG_04', index=OI_strike_four)
                final_data_OI=final_data[final_data['STRIKE']==CHNG4]
                final_data1=final_data_OI[['Time','CALL_CHNG','PUT_CHNG']].sort_values(by='Time', ascending=False).style.background_gradient(cmap='Blues', subset=['CALL_CHNG', 'PUT_CHNG']).format(precision=2)
                st.dataframe(final_data1, hide_index=True, use_container_width=True)

            with col15:
                CHNG5=st.selectbox("Strike five", options=range_01, key='CHNG_05', index=OI_strike_five)
                final_data_OI=final_data[final_data['STRIKE']==CHNG5]
                final_data1=final_data_OI[['Time','CALL_CHNG','PUT_CHNG']].sort_values(by='Time', ascending=False).style.background_gradient(cmap='Blues', subset=['CALL_CHNG', 'PUT_CHNG']).format(precision=2)
                st.dataframe(final_data1, hide_index=True, use_container_width=True)
        
            with col16:
                CHNG5=st.selectbox("strike six", options=range_01, key='CHNG_06', index=OI_strike_six)
                final_data_OI=final_data[final_data['STRIKE']==CHNG5]
                final_data1=final_data_OI[['Time','CALL_CHNG','PUT_CHNG']].sort_values(by='Time', ascending=False).style.background_gradient(cmap='Blues', subset=['CALL_CHNG', 'PUT_CHNG']).format(precision=2)
                st.dataframe(final_data1, hide_index=True, use_container_width=True)
    # OI Chart
    chart_strike_01=1
    chart_strike_02=8

    with tab3:
        strike_chart_OI_01=st.selectbox('Begning Strike', options=range_01, index=chart_strike_01, key='OI_chart_01')
        strike_chart_OI_02=st.selectbox('Begning Strike', options=range_01, index=chart_strike_02, key='OI_chart_02')
        sort_data=data_bt[['Time','CALL_OI','PUT_OI','CALL_CHNG','PUT_CHNG','CALL_LTP','PUT_LTP','STRIKE','CALL_VOLUME','PUT_VOLUME','Spot_Price']] 
        sort_data_chart=sort_data[sort_data.STRIKE.between(strike_chart_OI_01,strike_chart_OI_02)]
        cl_time_list2=sort_data['Time'].sort_values(ascending=False).unique()
        last_time_chart= st.selectbox("select the begning Time", options=cl_time_list2, key='time_chart_OI_2')
        filter= sort_data_chart[sort_data_chart['Time'] == last_time_chart]
        OI_chart=px.bar(filter, x='STRIKE', y=['CALL_OI', 'PUT_OI'], barmode='group')
        st.plotly_chart(OI_chart, use_container_width=True)
       

# CHNG OI Chart
    with tab4:
        strike_chart01=st.selectbox('Begning Strike', options=range_01, index=chart_strike_01, key='CHNG_chart_01')
        strike_chart02=st.selectbox('Begning Strike', options=range_01, index=chart_strike_02,key='CHNG_chart_02')
        sort_data=data_bt[['Time','CALL_OI','PUT_OI','CALL_CHNG','PUT_CHNG','CALL_LTP','PUT_LTP','STRIKE','CALL_VOLUME','PUT_VOLUME','Spot_Price']]
        sort_data=sort_data[sort_data.STRIKE.between(strike_chart01,strike_chart02)]
        cl_time_list2=data1['Time'].sort_values(ascending=False).unique()
        last_time_chart04= st.selectbox("select the begning Time", options=cl_time_list2, key='time_chart_03')
        filter= sort_data[sort_data['Time'] == last_time_chart04]
        CHNG_chart=px.bar(filter, x='STRIKE', y=['CALL_CHNG', 'PUT_CHNG'], barmode='group')
        st.plotly_chart(CHNG_chart, use_container_width=True)

# chart OI 2.0 

    with tab5:
        
        col91, col92, col93=st.columns(3)
        
        with col91:
            stk91=st.selectbox("Strike one", options=range_01, key='chart_01', index=OI_strike_one)
            final_data_chart=final_data[final_data['STRIKE']==stk91]
            final_data1=final_data_OI[['Time','STRIKE', 'CALL_OI','PUT_OI']]
            st.line_chart(final_data_chart, x='Time', y=['CALL_OI', 'PUT_OI'])

            stk96=st.selectbox("Strike four", options=range_01, key='chart_04', index=OI_strike_four)
            final_data_chart=final_data[final_data['STRIKE']==stk96]
            final_data1=final_data_OI[['Time','STRIKE', 'CALL_OI','PUT_OI']]
            st.line_chart(final_data_chart, x='Time', y=['CALL_OI', 'PUT_OI'])
            
        with col92:
            
            stk94=st.selectbox("Strike two", options=range_01, key='chart_02', index=OI_strike_two)
            final_data_chart=final_data[final_data['STRIKE']==stk94]
            final_data1=final_data_OI[['Time','STRIKE', 'CALL_OI','PUT_OI']]
            st.line_chart(final_data_chart, x='Time', y=['CALL_OI', 'PUT_OI'])
                            
            stk93=st.selectbox("Strike five", options=range_01, key='chart_05', index=OI_strike_five)
            final_data_chart=final_data[final_data['STRIKE']==stk93]
            final_data1=final_data_OI[['Time','STRIKE', 'CALL_OI','PUT_OI']]
            st.line_chart(final_data_chart, x='Time', y=['CALL_OI', 'PUT_OI'])

        with col93:
            stk92=st.selectbox("Strike three", options=range_01, key='chart_03', index=OI_strike_three)
            final_data_chart=final_data[final_data['STRIKE']==stk92]
            final_data1=final_data_OI[['Time','STRIKE', 'CALL_OI','PUT_OI']]
            st.line_chart(final_data_chart, x='Time', y=['CALL_OI', 'PUT_OI'])
                
            stk95=st.selectbox("Strike six", options=range_01, key='chart_06', index=OI_strike_six)
            final_data_chart=final_data[final_data['STRIKE']==stk95]
            final_data1=final_data_OI[['Time','STRIKE', 'CALL_OI','PUT_OI']]
            st.line_chart(final_data_chart, x='Time', y=['CALL_OI', 'PUT_OI'])
   
    with tab6:
        
        col101, col102, col103=st.columns(3)
        
        with col101:
            stk101=st.selectbox("Strike one", options=range_01, key='chart_21', index=OI_strike_one)
            final_data_chart=final_data[final_data['STRIKE']==stk101]
            final_data1=final_data_OI[['Time','STRIKE', 'CALL_CHNG','PUT_CHNG']]
            st.line_chart(final_data_chart, x='Time', y=['CALL_CHNG', 'PUT_CHNG'])

            stk105=st.selectbox("Strike four", options=range_01, key='chart_20', index=OI_strike_four)
            final_data_chart=final_data[final_data['STRIKE']==stk105]
            final_data1=final_data_OI[['Time','STRIKE', 'CALL_CHNG','PUT_CHNG']]
            st.line_chart(final_data_chart, x='Time', y=['CALL_CHNG', 'PUT_CHNG'])
            
        with col102:
            
            stk102=st.selectbox("Strike two", options=range_01, key='chart_22', index=OI_strike_two)
            final_data_chart=final_data[final_data['STRIKE']==stk102]
            final_data1=final_data_OI[['Time','STRIKE', 'CALL_CHNG','PUT_CHNG']]
            st.line_chart(final_data_chart, x='Time', y=['CALL_CHNG', 'PUT_CHNG'])
                            
            stk107=st.selectbox("Strike five", options=range_01, key='chart_23', index=OI_strike_five)
            final_data_chart=final_data[final_data['STRIKE']==stk107]
            final_data1=final_data_OI[['Time','STRIKE', 'CALL_CHNG','PUT_CHNG']]
            st.line_chart(final_data_chart, x='Time', y=['CALL_CHNG', 'PUT_CHNG'])

        with col103:
            stk103=st.selectbox("Strike three", options=range_01, key='chart_24', index=OI_strike_three)
            final_data_chart=final_data[final_data['STRIKE']==stk103]
            final_data1=final_data_OI[['Time','STRIKE', 'CALL_CHNG','PUT_CHNG']]
            st.line_chart(final_data_chart, x='Time', y=['CALL_CHNG', 'PUT_CHNG'])
                
            stk108=st.selectbox("Strike six", options=range_01, key='chart_25', index=OI_strike_six)
            final_data_chart=final_data[final_data['STRIKE']==stk108]
            final_data1=final_data_OI[['Time','STRIKE', 'CALL_CHNG','PUT_CHNG']]
            st.line_chart(final_data_chart, x='Time', y=['CALL_CHNG', 'PUT_CHNG'])


    with tab7:
        time_option12= data1['Time'].sort_values(ascending=False).unique()
        time=st.selectbox('Select time', options=time_option12, key='time01')
        filter=data_bt[data_bt['Time'] == time]
        #------------------------------------------

        put_max=filter['PUT_OI'].max()
        call_max=filter['CALL_OI'].max()
        put_volume_max=filter['PUT_VOLUME'].max()
        call_volume_max=filter['CALL_VOLUME'].max()
        call_CHNG_max=filter['CALL_VOLUME'].max()
        put_CHNG_max=filter['PUT_CHNG'].max()


        filter['Call_Per']=filter['CALL_OI']/call_max*100
        filter['Put_Per']=filter['PUT_OI']/put_max*100
        filter['Put_CHNG_Per']=filter['PUT_CHNG']/put_CHNG_max*100
        filter['Call_CHNG_Per']=filter['CALL_CHNG']/call_CHNG_max*100
        filter['Call_Volume_Per']=filter['CALL_VOLUME']/call_volume_max*100
        filter['Put_Volume_Per']=filter['PUT_VOLUME']/put_volume_max*100


        #------------------------------------------
        call_vol=filter['CALL_VOLUME'].max()
        put_vol=filter['PUT_VOLUME'].max()
        filter['call_price_vol']=filter['CALL_VOLUME']/call_vol*50 + filter['STRIKE']
        filter['put_price_vol']=filter['STRIKE']- filter['PUT_VOLUME']/put_vol*50 
        final_filter= filter.style.format(precision=0, subset=['call_price_vol','put_price_vol','PUT_LTP', 'CALL_LTP','Call_Per','Put_Per','Put_CHNG_Per','Call_CHNG_Per','Call_Volume_Per','Put_Volume_Per']).format(precision=2, subset=['Time']).background_gradient(cmap='Blues',subset=['call_price_vol','Call_Per','CALL_OI','Call_CHNG_Per','CALL_CHNG','Call_Volume_Per','CALL_VOLUME','CALL_LTP','PUT_LTP','Put_Volume_Per','PUT_VOLUME','PUT_CHNG','Put_CHNG_Per','PUT_OI','Put_Per','put_price_vol'])
        st.dataframe(final_filter, column_order=['Time','Call_Per','CALL_OI','Call_CHNG_Per','CALL_CHNG','Call_Volume_Per','CALL_VOLUME','CALL_LTP','call_price_vol','STRIKE','put_price_vol','PUT_LTP','Put_Volume_Per','PUT_VOLUME','PUT_CHNG','Put_CHNG_Per','PUT_OI','Put_OI_per'], use_container_width=True, hide_index=True)
       
        
if ind_sel == 'NIFTY':
    st.dataframe(nifty())
    st.dataframe(tab_nifty())
    exp=st.expander('Know range index')
    with exp:
        st.write(list(range_01))


        







