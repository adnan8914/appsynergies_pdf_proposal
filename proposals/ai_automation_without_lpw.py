import streamlit as st
import datetime
from pdf_generator import generate_proposal

def render_ai_automation_without_lpw_form():
    st.header("AI Automation without LPW")
    
    # Add currency selector
    currency = st.selectbox(
        "Select Currency",
        ["USD", "INR", "EUR"],
        key="ai_without_lpw_currency"
    )
    
    # Currency symbol based on selection
    currency_symbol = "₹" if currency == "INR" else ("€" if currency == "EUR" else "$")
    
    # Client Information
    st.subheader("Client Information")
    col1, col2 = st.columns(2)
    with col1:
        client_name = st.text_input("Client Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
    with col2:    
        country = st.text_input("Country")
        proposal_date = st.date_input("Proposal Date")
        validity_date = st.date_input("Validity Date", 
                                    value=proposal_date + datetime.timedelta(days=365),
                                    min_value=proposal_date,
                                    help="Proposal validity end date")

    # Project Pricing
    st.subheader("Project Pricing")
    col1, col2 = st.columns(2)
    with col1:
        ai_calling_price = st.number_input(f"AI Calling ({currency_symbol})", 
            min_value=0.0, step=100.0, format="%.2f")
        crm_price = st.number_input(f"CRM Automations ({currency_symbol})", 
            min_value=0.0, step=100.0, format="%.2f")
    with col2:
        manychat_price = st.number_input(f"ManyChat & Make Automation ({currency_symbol})", 
            min_value=0.0, step=100.0, format="%.2f")
        additional_price = st.number_input(f"Additional Features & Enhancements ({currency_symbol})", 
            min_value=0.0, step=100.0, format="%.2f")

    # Calculate totals
    total_price = ai_calling_price + crm_price + manychat_price + additional_price
    annual_maintenance = total_price * 0.10

    # Display totals with correct currency
    st.subheader("Cost Summary")
    st.write(f"Total Amount: {currency_symbol} {total_price:,.2f}")
    st.write(f"Annual Maintenance: {currency_symbol} {annual_maintenance:,.2f}")

    if st.button("Generate Proposal"):
        if not client_name:
            st.error("Please enter client name")
            return
            
        replacements = {
            "{client_name}": client_name,
            "{Email_address}": email,
            "{Phone_no}": phone,
            "{country_name}": country,
            "{date}": proposal_date.strftime("%d/%m/%Y"),
            "{sign_date}": proposal_date.strftime("%d/%m/%Y"),
            "{validity_date}": validity_date.strftime("%d/%m/%Y"),
            "{AI calling price}": f"{currency_symbol} {ai_calling_price:,.2f}",
            "{CRM Automation price}": f"{currency_symbol} {crm_price:,.2f}",
            "{Manychat price}": f"{currency_symbol} {manychat_price:,.2f}",
            "{Total amount}": f"{currency_symbol} {total_price:,.2f}",
            "{AM price}": f"{currency_symbol} {annual_maintenance:,.2f}",
            "{Additional}": f"{currency_symbol} {additional_price:,.2f}"
        }
        
        result = generate_proposal("AI Automation without LPW", client_name, replacements)
        
        if result:
            file_data, file_name, mime_type = result
            st.download_button(
                label="Download Proposal",
                data=file_data,
                file_name=file_name,
                mime=mime_type
            ) 
