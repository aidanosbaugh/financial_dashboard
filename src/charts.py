import plotly.express as px


def allocation_chart(df):

    df = df.copy()
   
    df["Value"] = df["Price"] * df["Shares"]

    df["Gain/Loss"] = ((df["Price"] - df["Original Price"]) * df["Shares"])
    
    df["Return"] = (df["Gain/Loss"] / (df["Original Price"] * df["Shares"]) * 100)

    df["Allocation"] = (df["Value"] / df["Value"].sum() * 100)

    df["hover_text"] = (
        "<b>" + df["Ticker"] + "</b><br>" +
        "Value: $" + df["Value"].map("{:,.2f}".format) + "<br>" +
        "Allocation: " + df["Allocation"].map("{:.2f}%".format) + "<br>" +
        "Return: " + df["Return"].map("{:.2f}%".format)
    )


    fig = px.pie(
        df,
        values="Value",
        names="Ticker",
        hole=0.4,
        title="Portfolio Allocation"
    )


    fig.update_traces(
        hovertext=df["hover_text"],
        hovertemplate="%{hovertext}<extra></extra>",
        textinfo="percent"
    )


    return fig
