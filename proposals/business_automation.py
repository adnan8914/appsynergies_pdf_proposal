import streamlit as st
import datetime
from pdf_generator import generate_proposal

def render_ba_form():
    st.header("Business Automation")
    
    # Add currency selector
    currency = st.selectbox(
        "Select Currency",
        ["USD", "INR", "EUR"],
        key="ba_currency"
    )
    
    # Currency symbol based on selection
    currency_symbol = "₹" if currency == "INR" else ("€" if currency == "EUR" else "$")
    
    col1, col2 = st.columns(2)
    with col1:
        client_name = st.text_input("Client Name", key="ba_name")
        contact_no = st.text_input("Contact Number", key="ba_contact")
        email_id = st.text_input("Email ID", key="ba_email_id")
    with col2:
        proposal_date = st.date_input("Date", datetime.datetime.now(), key="ba_date")
        validity_date = st.date_input("Validity Date", key="ba_validity")

    # Mutually Agreed Points
    mutually_agreed_points = st.text_area("Mutually Agreed Points", key="ba_points")
    
    # Week 1 Details
    st.header("Week 1 Details")
    week1_descrptn = st.text_area("Week 1 Description", key="ba_week1_desc")
    week1_price = st.number_input(f"Week 1 Price ({currency_symbol})", 
        min_value=0.0, step=100.0, format="%.2f")

    # Future Services Pricing
    st.header("Future Services Pricing")
    col1, col2 = st.columns(2)
    with col1:
        ai_auto_price = st.number_input(f"AI Automations Price ({currency_symbol})", 
            min_value=0.0, step=100.0, format="%.2f")
        whts_price = st.number_input(f"WhatsApp Automation Price ({currency_symbol})", 
            min_value=0.0, step=100.0, format="%.2f")
        crm_price = st.number_input(f"CRM Setup Price ({currency_symbol})", 
            min_value=0.0, step=100.0, format="%.2f")
        email_price = st.number_input(f"Email Marketing Setup Price ({currency_symbol})", 
            min_value=0.0, step=100.0, format="%.2f")
        make_price = st.number_input(f"Make/Zapier Automation Price ({currency_symbol})", 
            min_value=0.0, step=100.0, format="%.2f")
    with col2:
        firefly_price = st.number_input(f"Firefly Meeting Price ({currency_symbol})", 
            min_value=0.0, step=100.0, format="%.2f")
        chatbot_price = st.number_input(f"AI Chatbot Price ({currency_symbol})", 
            min_value=0.0, step=100.0, format="%.2f")
        pdf_gen_pr = st.number_input(f"PDF Generation Price ({currency_symbol})", 
            min_value=0.0, step=100.0, format="%.2f")
        ai_mdl_price = st.number_input(f"AI Social Media Price ({currency_symbol})", 
            min_value=0.0, step=100.0, format="%.2f")
        cstm_ai_price = st.number_input(f"Custom AI Models Price ({currency_symbol})", 
            min_value=0.0, step=100.0, format="%.2f")

    # Display totals with correct currency
    total_price = (week1_price + ai_auto_price + whts_price + crm_price + email_price + 
                  make_price + firefly_price + chatbot_price + pdf_gen_pr + 
                  ai_mdl_price + cstm_ai_price)
    
    st.subheader("Cost Summary")
    st.write(f"Total Amount: {currency_symbol} {total_price:,.2f}")

    replacements = {
        "{client_name}": client_name,
        "{contact_no}": contact_no,
        "{email_id}": email_id,
        "{date}": proposal_date.strftime("%d/%m/%Y"),
        "{sign_date}": proposal_date.strftime("%d/%m/%Y"),
        "{validity_date}": validity_date.strftime("%d/%m/%Y"),
        "{mutually_agreed_points}": mutually_agreed_points,
        "{week1_descrptn}": week1_descrptn,
        "{week1_price}": f"{currency_symbol} {week1_price:,.2f}",
        "{ai_auto_price}": f"{currency_symbol} {ai_auto_price:,.2f}",
        "{whts_price}": f"{currency_symbol} {whts_price:,.2f}",
        "{crm_price}": f"{currency_symbol} {crm_price:,.2f}",
        "{email_price}": f"{currency_symbol} {email_price:,.2f}",
        "{make_price}": f"{currency_symbol} {make_price:,.2f}",
        "{firefly_price}": f"{currency_symbol} {firefly_price:,.2f}",
        "{chatbot_price}": f"{currency_symbol} {chatbot_price:,.2f}",
        "{pdf_gen_pr}": f"{currency_symbol} {pdf_gen_pr:,.2f}",
        "{ai_mdl_price}": f"{currency_symbol} {ai_mdl_price:,.2f}",
        "{cstm_ai_price}": f"{currency_symbol} {cstm_ai_price:,.2f}"
    }

    if st.button("Generate BA Proposal", key="ba_generate"):
        result = generate_proposal("Business Automations", client_name, replacements)
        if result:
            file_data, file_name, mime_type = result
            st.download_button(
                label=f"Download {file_name}",
                data=file_data,
                file_name=file_name,
                mime=mime_type
            ) 
