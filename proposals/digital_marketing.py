import streamlit as st
import datetime
from pdf_generator import generate_proposal

def render_dm_form():
    st.header("Digital Marketing")
    
    # Add currency selector
    currency = st.selectbox(
        "Select Currency",
        ["USD", "INR", "EUR"],
        key="dm_currency"
    )
    
    # Currency symbol based on selection
    currency_symbol = "₹" if currency == "INR" else ("€" if currency == "EUR" else "$")
    
    # Client Information
    st.subheader("Client Information")
    col1, col2 = st.columns(2)
    with col1:
        client_name = st.text_input("Client Name", key="dm_name")
        client_email = st.text_input("Client Email", key="dm_email")
        client_phone = st.text_input("Client Phone", key="dm_phone")
    with col2:
        proposal_date = st.date_input("Proposal Date", datetime.datetime.now(), key="dm_date")
        validity_date = st.date_input("Validity Date", 
                                    datetime.datetime.now() + datetime.timedelta(days=30), 
                                    key="dm_validity")

    # Team Size
    st.subheader("Team Allocation")
    col1, col2 = st.columns(2)
    with col1:
        dgm_no = st.number_input("Digital Marketing Executives", min_value=1, value=1, key="dm_dgm")
        pm_no = st.number_input("Project Managers", min_value=1, value=1, key="dm_pm")
    with col2:
        ba_no = st.number_input("Business Analysts", min_value=1, value=1, key="dm_ba")
        ui_ux_no = st.number_input("UI/UX Members", min_value=1, value=1, key="dm_uiux")
    
    # Digital Marketing Services Pricing
    st.subheader("Digital Marketing Services Pricing")
    col1, col2 = st.columns(2)
    with col1:
        marketing_strategy = st.number_input(f"Marketing Strategy (One Time) ({currency_symbol})", 
            min_value=0.0, step=100.0, format="%.2f")
        social_media_setup = st.number_input(f"Social Media Setup (One Time) ({currency_symbol})", 
            min_value=0.0, step=100.0, format="%.2f")
        creative_posts = st.number_input(f"Creative Posts - 10 per month ({currency_symbol})", 
            min_value=0.0, step=100.0, format="%.2f")
    with col2:
        paid_ads = st.number_input(f"Paid Ads - Meta + Google ({currency_symbol})", 
            min_value=0.0, step=100.0, format="%.2f")
        seo_cost = st.number_input(f"SEO ({currency_symbol})", 
            min_value=0.0, step=100.0, format="%.2f")
        organic_marketing = st.number_input(f"Organic Marketing ({currency_symbol})", 
            min_value=0.0, step=100.0, format="%.2f")
    
    # Calculate totals
    total_marketing_cost = (marketing_strategy + social_media_setup + 
                          creative_posts + paid_ads + seo_cost + organic_marketing)
    gst = total_marketing_cost * 0.18  # 18% GST
    total_amount = total_marketing_cost + gst
    advance = total_amount * 0.5
    balance = total_amount * 0.5
    
    # Display totals
    st.subheader("Cost Summary")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"Total Marketing Cost: {currency_symbol} {total_marketing_cost:,.2f}")
        st.write(f"GST (18%): {currency_symbol} {gst:,.2f}")
        st.write(f"Total Amount: {currency_symbol} {total_amount:,.2f}")
    with col2:
        st.write(f"Advance Payment: {currency_symbol} {advance:,.2f}")
        st.write(f"Balance Payment: {currency_symbol} {balance:,.2f}")
    
    replacements = {
        # Client Information
        "{client_name}": client_name,
        "{client_email}": client_email,
        "{client_phone}": client_phone,
        "{date}": proposal_date.strftime("%d/%m/%Y"),
        "{sign_date}": proposal_date.strftime("%d/%m/%Y"),
        "{validity_date}": validity_date.strftime("%d/%m/%Y"),
        
        # Team Size
        "{dgm_no}": str(dgm_no),
        "{pm_no}": str(pm_no),
        "{ba_no}": str(ba_no),
        "{ui_ux_no}": str(ui_ux_no),
        
        # Pricing
        "{m_s}": f"{currency_symbol} {marketing_strategy:,.2f}",
        "{SMP}": f"{currency_symbol} {social_media_setup:,.2f}",
        "{cp}": f"{currency_symbol} {creative_posts:,.2f}",
        "{pamg}": f"{currency_symbol} {paid_ads:,.2f}",
        "{seo}": f"{currency_symbol} {seo_cost:,.2f}",
        "{o_m}": f"{currency_symbol} {organic_marketing:,.2f}",
        "{t_m_c}": f"{currency_symbol} {total_marketing_cost:,.2f}",
        "{gst}": f"{currency_symbol} {gst:,.2f}",
        "{total_price}": f"{currency_symbol} {total_amount:,.2f}",
        "{advance}": f"{currency_symbol} {advance:,.2f}",
        "{balance}": f"{currency_symbol} {balance:,.2f}"
    }

    if st.button("Generate DM Proposal", key="dm_generate"):
        if not client_name:
            st.error("Please enter client name")
            return
            
        result = generate_proposal("Digital Marketing", client_name, replacements)
        if result:
            file_data, file_name, mime_type = result
            st.download_button(
                label=f"Download {file_name}",
                data=file_data,
                file_name=file_name,
                mime=mime_type
            ) 