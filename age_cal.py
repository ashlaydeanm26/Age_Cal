import streamlit as st
from datetime import date, datetime

# Page Setup
st.set_page_config(page_title="🧓 Ultimate Age Calculator", layout="centered")
st.title("🧓 Age Calculator")
st.write("Find your exact age in any format — from years down to microseconds!")

# Input: Date of Birth
birth_date = st.date_input(
    "📅 Select your Date of Birth",
    min_value=date(1900, 1, 1),
    max_value=date.today()
)

# Input: Output Format
format_option = st.radio(
    "🧭 Choose the format to display your age:",
    ("Years", "Months", "Weeks", "Days", "Hours", "Minutes", "Seconds", "Microseconds")
)

# Calculate Button
if st.button("Calculate Age"):
    now = datetime.now()
    birth_datetime = datetime.combine(birth_date, datetime.min.time())

    if birth_datetime > now:
        st.error("❌ Date of birth cannot be in the future.")
    else:
        delta = now - birth_datetime
        days = delta.days
        seconds = delta.total_seconds()
        microseconds = delta.total_seconds() * 1_000_000
        weeks = days // 7
        months = (now.year - birth_date.year) * 12 + now.month - birth_date.month
        years = now.year - birth_date.year

        # Adjust years if birthday hasn't occurred yet this year
        if (now.month, now.day) < (birth_date.month, birth_date.day):
            years -= 1

        hours = int(seconds // 3600)
        minutes = int(seconds // 60)

        # Display result based on chosen format
        if format_option == "Years":
            st.success(f"🎉 Your age is: **{years} years**")
        elif format_option == "Months":
            st.success(f"🗓️ Your age is: **{months} months**")
        elif format_option == "Weeks":
            st.success(f"📅 Your age is: **{weeks} weeks**")
        elif format_option == "Days":
            st.success(f"🕰️ Your age is: **{days} days**")
        elif format_option == "Hours":
            st.success(f"⏰ Your age is: **{hours:,} hours**")
        elif format_option == "Minutes":
            st.success(f"⏱️ Your age is: **{minutes:,} minutes**")
        elif format_option == "Seconds":
            st.success(f"⏲️ Your age is: **{int(seconds):,} seconds**")
        elif format_option == "Microseconds":
            st.success(f"🧬 Your age is: **{int(microseconds):,} microseconds**")

