import PySimpleGUI as sg
import linear_layout as lin
import quadratic_layout as quad
import cubic_layout as cub
import reciprocal as res
import exponential as ex

linear_graph_layout = lin.layout_linear_graph
quadratic_graph_layout = quad.layout_quadratic_graph
cubic_graph_layout = cub.layout_cubic_graph
reciprocal_graph_layout = res.layout_reciprocal_graph
exponential_graph_layout = ex.layout_exponential_graph

layout = [
    [sg.TabGroup([
        [
            sg.Tab("Linear Graph", linear_graph_layout),
            sg.Tab("Quadratic Graph", quadratic_graph_layout),
            sg.Tab("Cubic Graph", cubic_graph_layout),
            sg.Tab("Reciprocal Graph", reciprocal_graph_layout),
            sg.Tab("Exponential Graph", exponential_graph_layout)
        ]
    ])]
]
