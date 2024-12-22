import pandas as pd
import numpy as np
from smartmoneyconcepts import smc
from termcolor import colored
# import plotly.graph_objects as go

# pip install pandas
# pip install requests
# pip install termcolor

def print_c(text, color="red"):
     print(colored(text, color))

# Step 1: Create a Sample OHLC DataFrame
def generate_sample_data():
    symbol = "FTM"
    print_c('Step 1: File loaded successfully.')
    df = pd.read_csv(f"data/{symbol}.csv", parse_dates=["datetime"])
    # Convert column names to lowercase
    df.columns = df.columns.str.lower()
    # df.rename(columns={'price': 'close'}, inplace=True)

    numeric_columns = ["close", "open", "high", "low"]
    for col in numeric_columns:
        df[col] = df[col].replace({',': ''}, regex=True).astype(float)
    
    # Handle the "vol." column: Remove 'K', multiply by 1,000
    # df["vol."] = (
    #     df["vol."]
    #     .replace({'K': ''}, regex=True)  # Remove 'K'
    #     .replace({',': ''}, regex=True)  # Remove commas
    #     .astype(float) * 1_000           # Multiply by 1,000
    # )
    
    # df["change %"] = df["change %"].str.rstrip('%').astype(float)
    return df

# Step 2: Prepare the DataFrame
def main():
    # Generate and print the sample OHLCV data
    ohlcv_data = generate_sample_data()
    print_c("Sample OHLCV DataFrame:", 'green')
    print_c(ohlcv_data.head(), 'blue')
    print("============================")
    print_c("Step 2: Starting FVG calculation...")
    # FVG Calculation
    try:
        fvgResult = smc.fvg(ohlcv_data, join_consecutive=False)
        # print("\n FVG Result:", fvgResult)
        # print("\nFVG Columns:", fvgResult.columns)
        fvg_filtered_result = fvgResult.dropna(subset=['FVG'])

        if not fvg_filtered_result.empty:
            print("\nFiltered FVG Result (non-NaN values):")
            print_c(fvg_filtered_result, 'blue')
        else:
            print("\nNo valid Fair Value Gap (FVG) records found.")
    
    except Exception as e:
        print_c(f"Error occurred: {e}")

    print("============================")
    print_c("Step 3: SHL calculation...", 'green')
    # SHL Calculation
    try:
        shlResult = smc.swing_highs_lows(ohlcv_data, swing_length = 50)
        # print("\n SHL Result:", shlResult)
        # print("\nSHL Columns:", shlResult.columns)
        shl_filtered_result = shlResult.dropna(subset=['HighLow'])

        if not shl_filtered_result.empty:
            print("\nFiltered SHL Result (non-NaN values):")
            print_c(shl_filtered_result, 'blue')
        else:
            print("\nNo valid Swing Highs and Lows (SHL) records found.")
    
    except Exception as e:
        print_c(f"Error occurred: {e}")

    print("============================")
    print_c("Step 4: Break of Structure (BOS) & Change of Character (CHoCH) calculation...", 'green')
    # Break of Structure (BOS) & Change of Character (CHoCH) Calculation
    try:
        bosChochResult = smc.bos_choch(ohlcv_data, shlResult, close_break = True)
        # print("\n BOS_CHOCH Result:", bosChochResult)
        # print("\nBOS_CHOCH Columns:", bosChochResult.columns)
        bos_choch_filtered_result = bosChochResult.dropna(subset=['BOS'])

        if not bos_choch_filtered_result.empty:
            print("\nFiltered BOS_CHOCH Result (non-NaN values):")
            print_c(bos_choch_filtered_result, 'blue')
        else:
            print_c("\nNo valid Break of Structure (BOS) & Change of Character (CHoCH) Calculation (BOS_CHOCH) records found.")
    
    except Exception as e:
        print(f"Error occurred: {e}")

    print("============================")
    print_c("Step 5: Order Blocks calculation...", 'green')
    # Order Blocks (OB)
    # try:
    #     obResult = smc.ob(ohlcv_data, shlResult, close_mitigation = False)
    #     # print("\n OB Result:", obResult)
    #     print("\n OB Columns:", obResult.columns)
    #     bo_filtered_result = obResult.dropna(subset=['OB'])

    #     if not bo_filtered_result.empty:
    #         print("\nFiltered OB Result (non-NaN values):")
    #         print(bo_filtered_result)
    #     else:
    #         print("\nNo valid Order Blocks (OB) records found.")
    
    # except Exception as e:
    #     print(f"Error occurred: {e}")

    print("============================")
    print_c("Step 6: Liquidity calculation...", 'green')
    # Liquidity
    try:
        lqResult = smc.liquidity(ohlcv_data, shlResult, range_percent = 0.01)
        # print("\n Liquidity Result:", lqResult)
        # print("\nLiquidity Columns:", lqResult.columns)
        lq_filtered_result = lqResult.dropna(subset=['Liquidity'])

        if not lq_filtered_result.empty:
            print("\nFiltered Liquidity Result (non-NaN values):")
            print_c(lq_filtered_result, 'blue')
        else:
            print_c("\nNo valid Liquidity records found.")
    
    except Exception as e:
        print(f"Error occurred: {e}")

    print("============================")
    print_c("Step 7: Previous High And Low calculation...", 'green')
    # Previous High And Low
    # try:
    #     pHLResult = smc.previous_high_low(ohlcv_data, time_frame = "1D")
    #     # print("\n Previous High And Low Result:", pHLResult)
    #     print("\n Previous High And Low Columns:", pHLResult.columns)
    #     phHL_filtered_result = pHLResult.dropna(subset=['PreviousHigh'])

    #     if not phHL_filtered_result.empty:
    #         print("\nFiltered Previous High And Low Result (non-NaN values):")
    #         print(phHL_filtered_result)
    #     else:
    #         print("\nNo valid Previous High And Low records found.")
    
    # except Exception as e:
    #     print(f"Error occurred: {e}")

    print("============================")
    print_c("Step 8: Sessions calculation...", 'green')
    # Sessions
    # try:
    #     session = "London"
    #     start_time = "05:00"
    #     end_time = "19:00"
    #     sResult = smc.sessions(ohlcv_data, session, start_time, end_time, time_zone = "UTC")
    #     # print("\n Sessions:", sResult)
    #     print("\n Sessions:", sResult.columns)
    #     session_filtered_result = sResult.dropna(subset=['Sessions'])

    #     if not session_filtered_result.empty:
    #         print("\nFiltered Sessions (non-NaN values):")
    #         print(session_filtered_result)
    #     else:
    #         print("\nNo valid Sessions records found.")
    
    # except Exception as e:
    #     print(f"Error occurred: {e}")

    print("============================")
    print_c("Step 9: Retracments calculation...", 'green')
     # Retracements
    try:
        reResult = smc.retracements(ohlcv_data, shlResult)
        # print("\n Retracements:", reResult)
        # print("\nRetracements:", reResult.columns)
        retracement_filtered_result = reResult.dropna(subset=['Direction'])

        if not retracement_filtered_result.empty:
            print("\nFiltered Retracements (non-NaN values):")
            print_c(retracement_filtered_result, 'blue')
        else:
            print_c("\nNo valid Retracements records found.")
    
    except Exception as e:
        print(f"Error occurred: {e}")

    print("============================")
    # fig = go.Figure(data=[go.Candlestick(x=ohlcv_data['datetime'],
    #                                  open=ohlcv_data['open'],
    #                                  high=ohlcv_data['high'],
    #                                  low=ohlcv_data['low'],
    #                                  close=ohlcv_data['close'])])

    # # Set the title and labels
    # fig.update_layout(title="Candlestick Chart Example",
    #               xaxis_title="Date",
    #               yaxis_title="Price")

    # # Show the chart
    # fig.show()
    
    # Save the DataFrame for use with SMC or further processing
    # ohlcv_data.to_csv("sample_ohlcv.csv", index=True)  # Save with date index
    # print("\nData saved to 'sample_ohlcv.csv'")

if __name__ == "__main__":
    main()
