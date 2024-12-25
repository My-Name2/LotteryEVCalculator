import streamlit as st

def calculate_ev(odds, payout, ticket_cost, tax_rate, sharing_probability):
    # Adjust net payout and effective probability
    net_payout = payout * (1 - tax_rate / 100)
    effective_probability = (1 / odds) * (1 - sharing_probability)
    # Calculate EV
    ev = (effective_probability * net_payout) - ticket_cost
    return ev, net_payout, effective_probability

# Streamlit App
st.title("Lottery Expected Value (EV) Calculator")
st.write("""
Use this calculator to determine if participating in a lottery is +EV (positive expected value) or -EV (negative expected value).
""")

# User Inputs
odds = st.number_input("Enter the odds of winning (e.g., 292000000 for 1 in 292 million):", min_value=1.0, step=1.0, value=292000000.0)
payout = st.number_input("Enter the total payout amount (e.g., 1000000000 for $1 billion):", min_value=0.0, step=1000000.0, value=1000000000.0)
ticket_cost = st.number_input("Enter the cost of a single ticket (e.g., 2 for $2):", min_value=0.01, step=0.01, value=2.0)
tax_rate = st.number_input("Enter the tax rate on winnings as a percentage (e.g., 30 for 30%):", min_value=0.0, max_value=100.0, step=1.0, value=30.0)
sharing_probability = st.slider("Enter the probability of sharing the jackpot (e.g., 0.5 for 50%):", min_value=0.0, max_value=1.0, step=0.01, value=0.5)

# Calculate EV when the user presses the button
if st.button("Calculate EV"):
    ev, net_payout, effective_probability = calculate_ev(odds, payout, ticket_cost, tax_rate, sharing_probability)

    # Display Results
    st.subheader("Lottery EV Analysis:")
    st.write(f"- **Odds of Winning:** 1 in {int(odds):,}")
    st.write(f"- **Adjusted Net Payout (after taxes):** ${net_payout:,.2f}")
    st.write(f"- **Effective Probability of Winning (adjusted for sharing):** {effective_probability:.10f}")
    st.write(f"- **Cost of Ticket:** ${ticket_cost:.2f}")
    st.write(f"- **Expected Value (EV):** ${ev:.2f}")

    # Conclusion
    if ev > 0:
        st.success("This lottery is +EV, meaning it is theoretically profitable to play.")
    else:
        st.error("This lottery is -EV, meaning it is not profitable to play on average.")
