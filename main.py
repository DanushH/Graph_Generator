import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import layouts
import validate_user_input as val

sg.theme("DarkBlack")
sg.set_options(font="Georgia 10")
plt.style.use("dark_background")

window = sg.Window("Graph Generator", layouts.layout, finalize=True, size=(1000, 650))

fig_linear = plt.figure(figsize=(8, 5))
fig_linear.add_subplot(111).grid(True)
figure_canvas_linear = FigureCanvasTkAgg(fig_linear, window["-GRAPH_LINEAR-"].TKCanvas)
figure_canvas_linear.draw()
figure_canvas_linear.get_tk_widget().pack()

fig_quadratic = plt.figure(figsize=(8, 5))
fig_quadratic.add_subplot(111).grid(True)
figure_canvas_quadratic = FigureCanvasTkAgg(
    fig_quadratic, window["-GRAPH_QUADRATIC-"].TKCanvas
)
figure_canvas_quadratic.draw()
figure_canvas_quadratic.get_tk_widget().pack()

fig_cubic = plt.figure(figsize=(8, 5))
fig_cubic.add_subplot(111).grid(True)
figure_canvas_cubic = FigureCanvasTkAgg(fig_cubic, window["-GRAPH_CUBIC-"].TKCanvas)
figure_canvas_cubic.draw()
figure_canvas_cubic.get_tk_widget().pack()

fig_reciprocal = plt.figure(figsize=(8, 5))
fig_reciprocal.add_subplot(111).grid(True)
figure_canvas_reciprocal = FigureCanvasTkAgg(
    fig_reciprocal, window["-GRAPH_RECIPROCAL-"].TKCanvas
)
figure_canvas_reciprocal.draw()
figure_canvas_reciprocal.get_tk_widget().pack()

fig_exponential = plt.figure(figsize=(8, 5))
fig_exponential.add_subplot(111).grid(True)
figure_canvas_exponential = FigureCanvasTkAgg(
    fig_exponential, window["-GRAPH_EXPONENTIAL-"].TKCanvas
)
figure_canvas_exponential.draw()
figure_canvas_exponential.get_tk_widget().pack()

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    # linear graph functionality
    m_linear = values["-INPUT_M_LINEAR-"]
    c_linear = values["-INPUT_C_LINEAR-"]
    x_start_linear = values["-INPUT_X_START_LINEAR-"]
    x_end_linear = values["-INPUT_X_END_LINEAR-"]

    is_valid_linear = m_linear and c_linear and x_start_linear and x_end_linear

    if event == "-CREATE_TABLE_LINEAR-":
        if is_valid_linear:
            # clear previous data
            table_data = []
            window["-TABLE_LINEAR-"].update(table_data)

            x_values, y_values = val.validate_linear(
                m_linear, c_linear, x_start_linear, x_end_linear
            )
            table_data.extend([[x, y] for x, y in zip(x_values, y_values)])
            window["-TABLE_LINEAR-"].update(table_data)

    if event == "-CREATE_GRAPH_LINEAR-":
        if is_valid_linear:
            for ax in fig_linear.axes:
                ax.clear()
            figure_canvas_linear.draw()
            figure_canvas_linear.get_tk_widget().pack()
            x_values, y_values = val.validate_linear(
                m_linear, c_linear, x_start_linear, x_end_linear
            )
            axes = fig_linear.axes
            axes[0].grid(True)
            axes[0].plot(x_values, y_values, linestyle="-", color="blue", marker="o")
            figure_canvas_linear.draw()
            figure_canvas_linear.get_tk_widget().pack()

    if event == "-CLEAR_TABLE_LINEAR-":
        window["-INPUT_M_LINEAR-"].update("")
        window["-INPUT_C_LINEAR-"].update("")
        window["-INPUT_X_START_LINEAR-"].update("")
        window["-INPUT_X_END_LINEAR-"].update("")
        window["-TABLE_LINEAR-"].update([])
        for ax in fig_linear.axes:
            ax.clear()
        figure_canvas_linear.draw()
        figure_canvas_linear.get_tk_widget().pack()

    if event == "-CLEAR_GRAPH_LINEAR-":
        for ax in fig_linear.axes:
            ax.clear()
        figure_canvas_linear.draw()
        figure_canvas_linear.get_tk_widget().pack()

    # quadratic graph functionality
    a_quadratic = values["-INPUT_A_QUADRATIC-"]
    b_quadratic = values["-INPUT_B_QUADRATIC-"]
    c_quadratic = values["-INPUT_C_QUADRATIC-"]
    x_start_quadratic = values["-INPUT_X_START_QUADRATIC-"]
    x_end_quadratic = values["-INPUT_X_END_QUADRATIC-"]

    is_valid_quadratic = (
        a_quadratic
        and b_quadratic
        and c_quadratic
        and x_start_quadratic
        and x_end_quadratic
    )

    if event == "-CREATE_TABLE_QUADRATIC-":
        if is_valid_quadratic:
            # clear previous data
            table_data = []
            window["-TABLE_QUADRATIC-"].update(table_data)

            x_values, y_values = val.validate_quadratic(
                a_quadratic,
                b_quadratic,
                c_quadratic,
                x_start_quadratic,
                x_end_quadratic,
            )
            table_data.extend([[x, y] for x, y in zip(x_values, y_values)])
            window["-TABLE_QUADRATIC-"].update(table_data)

    if event == "-CREATE_GRAPH_QUADRATIC-":
        if is_valid_quadratic:
            # reomve previous graph
            for ax in fig_quadratic.axes:
                ax.clear()
            figure_canvas_quadratic.draw()
            figure_canvas_quadratic.get_tk_widget().pack()

            x_values, y_values = val.validate_quadratic(
                a_quadratic,
                b_quadratic,
                c_quadratic,
                x_start_quadratic,
                x_end_quadratic,
            )
            axes = fig_quadratic.axes
            axes[0].grid(True)
            axes[0].plot(x_values, y_values, linestyle="-", color="blue", marker="o")
            figure_canvas_quadratic.draw()
            figure_canvas_quadratic.get_tk_widget().pack()

    if event == "-CLEAR_TABLE_QUADRATIC-":
        window["-INPUT_A_QUADRATIC-"].update("")
        window["-INPUT_B_QUADRATIC-"].update("")
        window["-INPUT_C_QUADRATIC-"].update("")
        window["-INPUT_X_START_QUADRATIC-"].update("")
        window["-INPUT_X_END_QUADRATIC-"].update("")
        window["-TABLE_QUADRATIC-"].update([])
        for ax in fig_quadratic.axes:
            ax.clear()
        figure_canvas_quadratic.draw()
        figure_canvas_quadratic.get_tk_widget().pack()

    if event == "-CLEAR_GRAPH_QUADRATIC-":
        for ax in fig_quadratic.axes:
            ax.clear()
        figure_canvas_quadratic.draw()
        figure_canvas_quadratic.get_tk_widget().pack()

    # cubic graph functionality
    a_cubic = values["-INPUT_A_CUBIC-"]
    b_cubic = values["-INPUT_B_CUBIC-"]
    c_cubic = values["-INPUT_C_CUBIC-"]
    d_cubic = values["-INPUT_D_CUBIC-"]
    x_start_cubic = values["-INPUT_X_START_CUBIC-"]
    x_end_cubic = values["-INPUT_X_END_CUBIC-"]

    is_valid_cubic = (
        a_cubic and b_cubic and c_cubic and d_cubic and x_start_cubic and x_end_cubic
    )

    if event == "-CREATE_TABLE_CUBIC-":
        if is_valid_cubic:
            # clear previous data
            table_data = []
            window["-TABLE_CUBIC-"].update(table_data)

            x_values, y_values = val.validate_cubic(
                a_cubic,
                b_cubic,
                c_cubic,
                d_cubic,
                x_start_cubic,
                x_end_cubic,
            )

            table_data.extend([[x, y] for x, y in zip(x_values, y_values)])
            window["-TABLE_CUBIC-"].update(table_data)

    if event == "-CREATE_GRAPH_CUBIC-":
        if is_valid_cubic:
            # reomve previous graph
            for ax in fig_cubic.axes:
                ax.clear()
            figure_canvas_cubic.draw()
            figure_canvas_cubic.get_tk_widget().pack()

            x_values, y_values = val.validate_cubic(
                a_cubic,
                b_cubic,
                c_cubic,
                d_cubic,
                x_start_cubic,
                x_end_cubic,
            )
            axes = fig_cubic.axes
            axes[0].grid(True)
            axes[0].plot(x_values, y_values, linestyle="-", color="blue", marker="o")
            figure_canvas_cubic.draw()
            figure_canvas_cubic.get_tk_widget().pack()

    if event == "-CLEAR_TABLE_CUBIC-":
        window["-INPUT_A_CUBIC-"].update("")
        window["-INPUT_B_CUBIC-"].update("")
        window["-INPUT_C_CUBIC-"].update("")
        window["-INPUT_D_CUBIC-"].update("")
        window["-INPUT_X_START_CUBIC-"].update("")
        window["-INPUT_X_END_CUBIC-"].update("")
        window["-TABLE_CUBIC-"].update([])
        for ax in fig_cubic.axes:
            ax.clear()
        figure_canvas_cubic.draw()
        figure_canvas_cubic.get_tk_widget().pack()

    if event == "-CLEAR_GRAPH_CUBIC-":
        for ax in fig_cubic.axes:
            ax.clear()
        figure_canvas_cubic.draw()
        figure_canvas_cubic.get_tk_widget().pack()

    # reciprocal graph functionality
    a_reciprocal = values["-INPUT_A_RECIPROCAL-"]
    x_start_reciprocal = values["-INPUT_X_START_RECIPROCAL-"]
    x_end_reciprocal = values["-INPUT_X_END_RECIPROCAL-"]

    is_valid_reciprocal = a_reciprocal and x_start_reciprocal and x_end_reciprocal

    if event == "-CREATE_TABLE_RECIPROCAL-":
        if is_valid_reciprocal:
            # clear previous data
            table_data = []
            window["-TABLE_RECIPROCAL-"].update(table_data)

            x_values_1, x_values_2, y_values_1, y_values_2 = val.validate_reciprocal(
                a_reciprocal,
                x_start_reciprocal,
                x_end_reciprocal,
            )
            table_data.extend([[x, y] for x, y in zip(x_values_1, y_values_1)])
            table_data.extend([[x, y] for x, y in zip(x_values_2, y_values_2)])
            window["-TABLE_RECIPROCAL-"].update(table_data)

    if event == "-CREATE_GRAPH_RECIPROCAL-":
        if is_valid_reciprocal:
            # Remove previous plot data
            axes = fig_reciprocal.axes
            axes[0].clear()

            x_values_1, x_values_2, y_values_1, y_values_2 = val.validate_reciprocal(
                a_reciprocal,
                x_start_reciprocal,
                x_end_reciprocal,
            )
            axes[0].grid(True)
            axes[0].plot(x_values_1, y_values_1, linestyle="-", color="blue")
            axes[0].plot(x_values_2, y_values_2, linestyle="-", color="blue")
            figure_canvas_reciprocal.draw_idle()

    if event == "-CLEAR_TABLE_RECIPROCAL-":
        window["-INPUT_A_RECIPROCAL-"].update("")
        window["-INPUT_X_START_RECIPROCAL-"].update("")
        window["-INPUT_X_END_RECIPROCAL-"].update("")
        window["-TABLE_RECIPROCAL-"].update([])
        for ax in fig_reciprocal.axes:
            ax.clear()
        figure_canvas_reciprocal.draw()
        figure_canvas_reciprocal.get_tk_widget().pack()

    if event == "-CLEAR_GRAPH_RECIPROCAL-":
        for ax in fig_reciprocal.axes:
            ax.clear()
        figure_canvas_reciprocal.draw()
        figure_canvas_reciprocal.get_tk_widget().pack()

    # exponential graph functionality
    a_exponential = values["-INPUT_A_EXPONENTIAL-"]
    k_exponential = values["-INPUT_K_EXPONENTIAL-"]
    x_start_exponential = values["-INPUT_X_START_EXPONENTIAL-"]
    x_end_exponential = values["-INPUT_X_END_EXPONENTIAL-"]

    is_valid_exponential = (
        a_exponential and k_exponential and x_start_exponential and x_end_exponential
    )

    if event == "-CREATE_TABLE_EXPONENTIAL-":
        if is_valid_exponential:
            # clear previous data
            table_data = []
            window["-TABLE_EXPONENTIAL-"].update(table_data)

            x_values, y_values = val.validate_exponential(
                a_exponential, k_exponential, x_start_exponential, x_end_exponential
            )
            table_data.extend([[x, y] for x, y in zip(x_values, y_values)])
            window["-TABLE_EXPONENTIAL-"].update(table_data)

    if event == "-CREATE_GRAPH_EXPONENTIAL-":
        if is_valid_exponential:
            for ax in fig_exponential.axes:
                ax.clear()
            figure_canvas_exponential.draw()
            figure_canvas_exponential.get_tk_widget().pack()
            x_values, y_values = val.validate_exponential(
                a_exponential, k_exponential, x_start_exponential, x_end_exponential
            )
            axes = fig_exponential.axes
            axes[0].grid(True)
            axes[0].plot(x_values, y_values, linestyle="-", color="blue")
            figure_canvas_exponential.draw()
            figure_canvas_exponential.get_tk_widget().pack()

    if event == "-CLEAR_TABLE_EXPONENTIAL-":
        window["-INPUT_A_EXPONENTIAL-"].update("")
        window["-INPUT_K_EXPONENTIAL-"].update("")
        window["-INPUT_X_START_EXPONENTIAL-"].update("")
        window["-INPUT_X_END_EXPONENTIAL-"].update("")
        window["-TABLE_EXPONENTIAL-"].update([])
        for ax in fig_exponential.axes:
            ax.clear()
        figure_canvas_exponential.draw()
        figure_canvas_exponential.get_tk_widget().pack()

    if event == "-CLEAR_GRAPH_EXPONENTIAL-":
        for ax in fig_exponential.axes:
            ax.clear()
        figure_canvas_exponential.draw()
        figure_canvas_exponential.get_tk_widget().pack()

window.close()
