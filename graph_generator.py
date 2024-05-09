import matplotlib.pyplot as plt

def generate_graph(x_values, y_values, title, x_label, y_label):
    plt.plot(x_values, y_values)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.show()

def save_graph(x_values, y_values, title, x_label, y_label, file_name):
    plt.plot(x_values, y_values)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.savefig(file_name)

x_values = [1, 2, 3, 4, 5]
y_values = [2, 4, 6, 8, 10]

generate_graph(x_values, y_values, "Sample Graph", "X-axis", "Y-axis")

save_graph(x_values, y_values, "Sample Graph", "X-axis", "Y-axis", "sample_graph.png")
