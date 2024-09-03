import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
def load_dataset(file_path):
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully!")
    print(df.head())
    return df
def generate_visualization(df, plot_type, x_col, y_col=None):
    if plot_type == 'line':
        plt.plot(df[x_col], df[y_col])
        plt.title(f'{x_col} vs {y_col}')
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.show()
    elif plot_type == 'scatter':
        fig = px.scatter(df, x=x_col, y=y_col, title=f'{x_col} vs {y_col}')
        fig.show()
    elif plot_type == 'bar':
        fig = px.bar(df, x=x_col, y=y_col, title=f'{x_col} vs {y_col}')
        fig.show()  # Create and display a bar chart
    elif plot_type == 'pairplot':
        sns.pairplot(df)
        plt.show()
    else:
        print("Invalid plot type. Choose from 'line', 'scatter', 'bar', or 'pairplot'.")
def main():
    file_path = 'cars_info.csv'
    df = load_dataset(file_path)
    print("Available columns:", df.columns.tolist())
    plot_type = input("Enter the type of plot (line, scatter, bar, pairplot): ").strip().lower()
    x_col = input("Enter the column name for the X-axis: ").strip()
    if plot_type != 'pairplot':
        y_col = input("Enter the column name for the Y-axis: ").strip()
        generate_visualization(df, plot_type, x_col, y_col)
    else:
        generate_visualization(df, plot_type, x_col)
if __name__ == "__main__":
    main()