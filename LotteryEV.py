import streamlit as st

def calculate_ev(odds, payout, ticket_cost, tax_rate, instant_payout, num_tickets):
    # Adjust payout for instant payout option
    if instant_payout:
        payout /= 2

    # Adjust net payout for taxes
    net_payout = payout * (1 - tax_rate / 100)

    # Calculate EV for a single ticket
    effective_probability = 1 / odds
    ev_single_ticket = (effective_probability * net_payout) - ticket_cost

    # Calculate total EV for multiple tickets
    ev_total = ev_single_ticket * num_tickets
    return ev_single_ticket, ev_total, net_payout, effective_probability

def calculate_combined_probability(odds, num_tickets):
    # Probability of winning multiplied by the number of tickets
    return (1 / odds) * num_tickets

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
num_tickets = st.number_input("Enter the number of tickets you plan to purchase:", min_value=1, step=1, value=1)

# Instant Payout Option
instant_payout = st.checkbox("Take Instant Payout (Halves the Prize Pool)")

# Calculate EV and Combined Probability when the user presses the button
if st.button("Calculate EV"):
    ev_single_ticket, ev_total, net_payout, effective_probability = calculate_ev(
        odds, payout, ticket_cost, tax_rate, instant_payout, num_tickets
    )
    combined_probability = calculate_combined_probability(odds, num_tickets)

    # Display Results
    st.subheader("Lottery EV Analysis:")
    st.write(f"- **Odds of Winning:** 1 in {int(odds):,}")
    st.write(f"- **Adjusted Net Payout (after taxes):** ${net_payout:,.2f}")
    st.write(f"- **Effective Probability of Winning per Ticket:** {effective_probability:.10f}")
    st.write(f"- **Cost of a Single Ticket:** ${ticket_cost:.2f}")
    st.write(f"- **Number of Tickets Purchased:** {num_tickets}")
    st.write(f"- **Expected Value (EV) per Ticket:** ${ev_single_ticket:.2f}")
    st.write(f"- **Total Expected Value (EV) for {num_tickets} Tickets:** ${ev_total:.2f}")
    st.write(f"- **Combined Probability of Winning with {num_tickets} Tickets:** {combined_probability:.10f}")

    # Conclusion
    if ev_total > 0:
        st.success("This lottery is +EV for the total tickets purchased, meaning it is theoretically profitable to play.")
    else:
        st.error("This lottery is -EV for the total tickets purchased, meaning it is not profitable to play on average.")
